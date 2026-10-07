import streamlit as st
import plotly.express as px

from rfm_pipeline import get_data, apply_presentation_style, SEGMENT_COLORS

st.set_page_config(page_title="Boxplots", layout="wide")
apply_presentation_style()
st.title("📦 Distribution RFM par segment")
st.caption("Choisissez une variable pour comparer comment chaque segment se comporte.")

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

metric_choice = st.selectbox("Variable à comparer :", ["Recence", "Frequence", "Montant"])
fig_box = px.box(rfm, x="Segment", y=metric_choice, color="Segment",
                  color_discrete_map=SEGMENT_COLORS,
                  title=f"Distribution de {metric_choice} par segment")
st.plotly_chart(fig_box, width="stretch")
