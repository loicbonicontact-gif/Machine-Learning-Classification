import streamlit as st

from rfm_pipeline import get_data, apply_presentation_style

st.set_page_config(page_title="Segmentation Client RFM", layout="wide")
apply_presentation_style()

st.title("🛒 Segmentation Client RFM — GlobalShop Direct")
st.caption("Mission NexaData Consulting pour GlobalShop Direct")

st.markdown(
    """
    ## 🎯 Contexte et objectif

    GlobalShop Direct souhaite mieux connaître ses clients pour adapter ses actions marketing.
    Nous avons analysé **541 909 transactions** e-commerce pour répondre à une question simple :

    > **Peut-on regrouper les clients en segments cohérents, sans connaître à l'avance leurs catégories ?**

    C'est un problème d'**apprentissage non supervisé** : on ne dit pas au modèle ce qu'est
    un "bon" ou "mauvais" client, on le laisse découvrir des groupes naturels dans les données.

    ## 🧭 Démarche suivie

    1. **Nettoyage des données** (annulations, valeurs manquantes, doublons retirées)
    2. **Construction des indicateurs RFM** : Récence, Fréquence, Montant par client
    3. **Clustering K-means** (K=4) pour regrouper les clients similaires
    4. **PCA** pour visualiser les 4 segments en 2 dimensions
    5. **Nommage métier** des segments (Champions, Fidèles, Occasionnels, À Risque)

    👉 Utilisez le **menu à gauche** pour parcourir chaque étape dans l'ordre pendant la présentation.
    """
)

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

st.divider()
st.subheader("Chiffres clés du projet")
col1, col2, col3 = st.columns(3)
col1.metric("Clients analysés", f"{rfm.shape[0]:,}")
col2.metric("Chiffre d'affaires total (£)", f"{rfm['Montant'].sum():,.0f}")
col3.metric("Segments identifiés", "4")
