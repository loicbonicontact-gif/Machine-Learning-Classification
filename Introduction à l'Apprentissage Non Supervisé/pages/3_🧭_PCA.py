import streamlit as st
import plotly.express as px

from rfm_pipeline import get_data, apply_presentation_style, SEGMENT_COLORS

st.set_page_config(page_title="PCA", layout="wide")
apply_presentation_style()
st.title("🧭 Visualisation des segments (PCA)")
st.caption("On résume 3 variables (R, F, M) en 2 axes pour pouvoir visualiser les segments sur un graphique.")

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

st.info(f"Ces 2 axes conservent **{variance_ratio.sum() * 100:.1f}%** de l'information initiale : "
        "on peut donc se fier à ce graphique pour juger si les segments sont bien séparés.")

fig_pca = px.scatter(
    pca_df, x="PCA1", y="PCA2", color="Segment",
    color_discrete_map=SEGMENT_COLORS,
    title="Clients projetés en 2D (PCA) par segment",
    opacity=0.6,
)
st.plotly_chart(fig_pca, width="stretch")
