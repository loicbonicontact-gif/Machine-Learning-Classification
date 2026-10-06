import streamlit as st

from rfm_pipeline import get_data, apply_presentation_style, RECOMMANDATIONS

st.set_page_config(page_title="Synthèse", layout="wide")
apply_presentation_style()
st.title("🎤 Synthèse — conclusion de la présentation")

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

st.markdown("### Les 4 segments identifiés et les actions marketing recommandées")

profils = rfm.groupby("Segment")[["Recence", "Frequence", "Montant"]].mean().round(1)
tailles = rfm["Segment"].value_counts()

for segment in profils.index:
    with st.container(border=True):
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.subheader(segment)
            st.metric("Nombre de clients", f"{tailles[segment]:,}")
        with col_b:
            st.write(
                f"Récence moyenne : **{profils.loc[segment, 'Recence']:.0f} jours** · "
                f"Fréquence moyenne : **{profils.loc[segment, 'Frequence']:.1f} commandes** · "
                f"Montant moyen : **£{profils.loc[segment, 'Montant']:,.0f}**"
            )
            st.info(f"💡 {RECOMMANDATIONS[segment]}")

st.divider()
st.markdown(
    """
    ### Message clé à retenir

    Sans connaître les clients à l'avance, le clustering K-means a permis de faire émerger
    4 profils cohérents et actionnables. GlobalShop Direct peut maintenant cibler chaque
    segment avec une action marketing adaptée plutôt que d'envoyer le même message à tous.
    """
)
