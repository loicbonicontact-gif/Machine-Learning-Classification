import streamlit as st

from rfm_pipeline import get_data, apply_presentation_style, SEGMENT_COLORS

st.set_page_config(page_title="KPI", layout="wide")
apply_presentation_style()
st.title("📊 Indicateurs clés")
st.caption("Vue d'ensemble de la base client avant de parler des segments.")

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

chiffre_affaires_total = rfm["Montant"].sum()
panier_moyen = rfm["Montant"].mean()
part_champions = (rfm["Segment"] == "Champions").mean() * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Clients uniques", f"{rfm.shape[0]:,}")
col2.metric("Chiffre d'affaires total (£)", f"{chiffre_affaires_total:,.0f}")
col3.metric("Panier moyen par client (£)", f"{panier_moyen:,.0f}")
col4.metric("% Clients Champions", f"{part_champions:.1f}%")

st.subheader("Répartition des clients par segment")
st.caption("Combien de clients dans chaque groupe trouvé par le clustering.")
st.bar_chart(rfm["Segment"].value_counts(), color="#0072B2")

st.subheader("Profil moyen par segment")
st.caption("Les chiffres qui justifient le nom donné à chaque segment.")
st.dataframe(rfm.groupby("Segment")[["Recence", "Frequence", "Montant"]].mean().round(1))
