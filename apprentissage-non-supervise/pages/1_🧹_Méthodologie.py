import streamlit as st

from rfm_pipeline import get_data, apply_presentation_style

st.set_page_config(page_title="Méthodologie", layout="wide")
apply_presentation_style()
st.title("🧹 Méthodologie")

rfm, pca_df, scaler, kmeans, pca, variance_ratio, segment_names = get_data()

st.markdown(
    """
    ### 1. Nettoyage des données brutes

    Sur 541 909 lignes de transactions, on retire :
    - les lignes **sans identifiant client** (`CustomerID` manquant),
    - les **commandes annulées** (numéro de facture commençant par "C"),
    - les **quantités ou prix négatifs/nuls** (erreurs de saisie),
    - les **doublons exacts**.

    ### 2. Construction des indicateurs RFM

    Pour chaque client, on calcule 3 indicateurs :
    - **Récence** : nombre de jours depuis son dernier achat (plus bas = mieux)
    - **Fréquence** : nombre de commandes distinctes (plus haut = mieux)
    - **Montant** : total dépensé en £ (plus haut = mieux)

    ### 3. Transformation des données

    Les montants et fréquences sont très étalés (quelques gros clients, beaucoup de petits).
    On applique une **transformation logarithmique** pour réduire cet effet, puis une
    **standardisation** (mettre toutes les variables à la même échelle) pour que le modèle
    ne favorise pas une variable à cause de son unité.

    ### 4. Clustering K-means

    L'algorithme **K-means** regroupe les clients en 4 groupes (clusters) en minimisant
    la distance entre les clients d'un même groupe. Le nombre K=4 a été choisi avec la
    **méthode du coude (Elbow)**.

    ### 5. PCA pour visualiser

    Impossible de représenter 3 dimensions (R, F, M) facilement sur un graphique.
    La **PCA** (Analyse en Composantes Principales) résume ces 3 variables en 2 axes
    tout en conservant un maximum d'information.
    """
)

st.info(
    f"✅ Pipeline exécuté sur {rfm.shape[0]:,} clients — "
    f"les 2 axes de la PCA expliquent {variance_ratio.sum() * 100:.1f}% de la variance totale."
)
