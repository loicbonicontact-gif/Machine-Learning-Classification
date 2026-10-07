# Machine Learning : classification, régression et apprentissage non supervisé

Dépôt de formation Data Analyst (Simplon), issu d'un travail d'équipe (dépôt d'origine : `Salma-AZIZ/Machine-Learning-Mise-en-pratique`).

## Projet phare : CrediTrust Scoring

Scoring du risque de crédit pour une banque fictive : 5 modèles de classification comparés (régression logistique, arbre de décision, Random Forest, KNN, SVM), Random Forest retenu avec priorité au **rappel** pour détecter un maximum de mauvais payeurs, puis dashboard Streamlit avec simulateur de prêt en direct.

**Application en ligne : https://creditrust.streamlit.app**

Dossier du projet : [`classification/`](./classification/) (README détaillé, explications des choix, notebooks, dashboard).

## Structure du dépôt

| Dossier | Description |
|---|---|
| `classification/` | Projet CrediTrust Scoring (classification, dashboard Streamlit). |
| `regression/` | Régression (HabitatPlus, assurance santé). Dépôt Git indépendant, ignoré ici. |
| `apprentissage-non-supervise/` | Clustering : K-Means, coude, silhouette, hiérarchique, segmentation RFM, dashboard Streamlit. |
| `entrainement/` | Les 4 notebooks d'entraînement traités (`nb_01` à `nb_04`), avec leurs données. |
| `assets/` | Illustrations de cours partagées. |
| `docs/` | Documents perso (aide-mémoire, non suivi par Git). |

## Outils

Python, pandas, scikit-learn, Streamlit, Plotly, Jupyter.
