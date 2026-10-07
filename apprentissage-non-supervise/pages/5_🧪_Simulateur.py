import numpy as np
import pandas as pd
import streamlit as st

from rfm_pipeline import get_data, apply_presentation_style, RECOMMANDATIONS

st.set_page_config(page_title="Simulateur", layout="wide")
apply_presentation_style()
st.title("🧪 Simulateur de profil client")
st.write(
    "Entrez les indicateurs RFM d'un client fictif : le modèle K-means déjà entraîné "
    "lui attribue instantanément un segment et une action marketing recommandée."
)

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

col1, col2, col3 = st.columns(3)
sim_recence = col1.number_input("Récence (jours depuis le dernier achat)", min_value=0, value=30)
sim_frequence = col2.number_input("Fréquence (nombre de commandes)", min_value=1, value=5)
sim_montant = col3.number_input("Montant total dépensé (£)", min_value=0.0, value=500.0)

if st.button("Prédire le segment"):
    sim_log = pd.DataFrame(
        [[np.log1p(sim_recence), np.log1p(sim_frequence), np.log1p(sim_montant)]],
        columns=["Recence", "Frequence", "Montant"],
    )
    sim_scaled = pd.DataFrame(
        scaler.transform(sim_log), columns=["Recence", "Frequence", "Montant"]
    )
    predicted_cluster = kmeans.predict(sim_scaled)[0]
    predicted_segment = segment_names[predicted_cluster]
    st.info(f"Ce client appartient au segment : **{predicted_segment}**")
    st.info(f"💡 Action marketing recommandée : {RECOMMANDATIONS[predicted_segment]}")
