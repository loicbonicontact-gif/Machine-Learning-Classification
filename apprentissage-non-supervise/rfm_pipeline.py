from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "online_retail.csv"
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

N_CLUSTERS = 4

# Palette sans rouge ni vert (bleu, orange, violet, gris) pour les présentations.
SEGMENT_COLORS = {
    "Champions": "#0072B2",
    "Fidèles": "#E69F00",
    "Occasionnels": "#9467BD",
    "À Risque": "#6C757D",
}

RECOMMANDATIONS = {
    "Champions": "Programme de fidélité VIP, accès prioritaire aux nouveautés, remerciement personnalisé.",
    "Fidèles": "Ventes croisées (cross-sell), offres de montée en gamme (upsell), demande d'avis/parrainage.",
    "Occasionnels": "Emails de relance personnalisés, offres de bienvenue pour encourager un 2e achat.",
    "À Risque": "Campagne de réactivation (code promo ciblé), enquête de satisfaction pour comprendre le désengagement.",
}


def apply_presentation_style():
    """Agrandit le texte (captions, markdown, métriques) pour une lecture confortable en projection."""
    st.markdown(
        """
        <style>
        [data-testid="stCaptionContainer"] { font-size: 1.1rem !important; }
        .stMarkdown p, .stMarkdown li { font-size: 1.15rem !important; line-height: 1.5; }
        [data-testid="stMetricValue"] { font-size: 2rem !important; }
        [data-testid="stMetricLabel"] { font-size: 1.05rem !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df_clean = df.copy()
    df_clean = df_clean.dropna(subset=["CustomerID"])
    df_clean = df_clean[~df_clean["InvoiceNo"].astype(str).str.startswith("C")]
    df_clean = df_clean[(df_clean["Quantity"] > 0) & (df_clean["UnitPrice"] > 0)]
    df_clean = df_clean.drop_duplicates()
    df_clean["TotalPrice"] = df_clean["Quantity"] * df_clean["UnitPrice"]
    df_clean["CustomerID"] = df_clean["CustomerID"].astype(int)
    df_clean["InvoiceDate"] = pd.to_datetime(df_clean["InvoiceDate"])
    return df_clean


@st.cache_data
def build_rfm(df_clean: pd.DataFrame) -> pd.DataFrame:
    date_reference = df_clean["InvoiceDate"].max() + pd.Timedelta(days=1)

    recence = df_clean.groupby("CustomerID")["InvoiceDate"].max().reset_index()
    recence.columns = ["CustomerID", "DerniereDate"]
    recence["Recence"] = (date_reference - recence["DerniereDate"]).dt.days

    frequence = df_clean.groupby("CustomerID")["InvoiceNo"].nunique().reset_index()
    frequence.columns = ["CustomerID", "Frequence"]

    montant = df_clean.groupby("CustomerID")["TotalPrice"].sum().reset_index()
    montant.columns = ["CustomerID", "Montant"]

    rfm = recence.merge(frequence, on="CustomerID").merge(montant, on="CustomerID")
    rfm = rfm.drop(columns=["DerniereDate"])
    return rfm


@st.cache_resource
def run_clustering(rfm: pd.DataFrame):
    log_rfm = rfm.copy()
    log_rfm["Recence"] = np.log1p(log_rfm["Recence"])
    log_rfm["Frequence"] = np.log1p(log_rfm["Frequence"])
    log_rfm["Montant"] = np.log1p(log_rfm["Montant"])

    scaler = StandardScaler()
    scaled = scaler.fit_transform(log_rfm[["Recence", "Frequence", "Montant"]])
    scaled_df = pd.DataFrame(scaled, columns=["Recence", "Frequence", "Montant"])

    kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42)
    kmeans.fit(scaled_df)
    rfm = rfm.copy()
    rfm["Cluster"] = kmeans.labels_

    pca = PCA(n_components=2)
    coords = pca.fit_transform(scaled_df)
    pca_df = pd.DataFrame(coords, columns=["PCA1", "PCA2"])
    pca_df["Cluster"] = rfm["Cluster"].values

    return rfm, pca_df, scaler, kmeans, pca, pca.explained_variance_ratio_


def label_clusters(rfm: pd.DataFrame) -> dict:
    """Nomme les segments selon leurs moyennes réelles (R faible = récent, F/M élevés = bon client)."""
    means = rfm.groupby("Cluster")[["Recence", "Frequence", "Montant"]].mean()
    names = {}
    champions_id = means["Montant"].idxmax()
    names[champions_id] = "Champions"
    remaining = means.drop(index=champions_id)
    risque_id = remaining["Recence"].idxmax()
    names[risque_id] = "À Risque"
    remaining = remaining.drop(index=risque_id)
    fideles_id = remaining["Frequence"].idxmax()
    names[fideles_id] = "Fidèles"
    remaining = remaining.drop(index=fideles_id)
    for cid in remaining.index:
        names[cid] = "Occasionnels"
    return names


@st.cache_resource
def get_data():
    df_clean = load_and_clean(DATA_PATH)
    rfm = build_rfm(df_clean)
    rfm, pca_df, scaler, kmeans, pca, variance_ratio = run_clustering(rfm)
    segment_names = label_clusters(rfm)
    rfm["Segment"] = rfm["Cluster"].map(segment_names)
    pca_df["Segment"] = rfm["Segment"].values
    return rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names
