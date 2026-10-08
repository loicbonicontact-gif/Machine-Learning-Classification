# Segmentation Client RFM — GlobalShop Direct

Projet de formation Data Analyst (Simplon) : apprentissage non supervisé appliqué à la segmentation client par la méthode RFM (Récence, Fréquence, Montant), sur le jeu de données [Online Retail (UCI)](https://archive.ics.uci.edu/dataset/352/online+retail).

**Application en ligne (Streamlit) : https://loicbonicontact-gif-machi-apprentissage-non-superviseapp-mcu8oo.streamlit.app**

**Dashboard Looker Studio : https://datastudio.google.com/u/0/reporting/83a072e0-5402-487c-b203-37e15ee416e9/page/p_y10e3pq47d**

## Livrables

| # | Livrable | Emplacement |
|---|---|---|
| 1 | Notebook individuel (clustering + PCA, Mall Customers) | [`../entrainement/notebooks/nb_04_Apprentissage_Non_Supervisé loic.ipynb`](../entrainement/notebooks/nb_04_Apprentissage_Non_Supervisé%20loic.ipynb) |
| 2 | Notebook binôme (nettoyage, RFM, clustering, PCA sur `online_retail.csv`) | [`notebooks/online_retail_clustering_rfm.ipynb`](notebooks/online_retail_clustering_rfm.ipynb) |
| 2 | Code source du Dashboard Streamlit | [`app.py`](app.py), [`rfm_pipeline.py`](rfm_pipeline.py), [`pages/`](pages/) |
| 3 | Support de présentation (10 slides) | [`presentation/segmentation-rfm-globalshop.pdf`](presentation/segmentation-rfm-globalshop.pdf) |
| — | Dashboard complémentaire Looker Studio | [lien ci-dessus](https://datastudio.google.com/u/0/reporting/83a072e0-5402-487c-b203-37e15ee416e9/page/p_y10e3pq47d) |

## Démarche

1. **Nettoyage** des 541 909 transactions brutes (clients non identifiés, commandes annulées, quantités/prix non positifs, doublons retirés) → 392 692 transactions fiables, 4 338 clients.
2. **Construction des indicateurs RFM** (Récence, Fréquence, Montant) par client, transformation logarithmique puis standardisation.
3. **Clustering K-means** : comparaison de K=2 à K=10 (score de silhouette, stabilité, profils métier) → **K=4** retenu.
4. **PCA** : réduction à 2 axes, 93,9 % de variance expliquée, pour valider visuellement la séparation des 4 segments.
5. **Nommage métier** des segments : Champions, Fidèles, Occasionnels, À Risque, chacun avec une action marketing recommandée.

## Dashboard Streamlit

Pages : Méthodologie, KPI, PCA, Boxplots, Simulateur (saisie d'un profil RFM → segment assigné instantanément), Synthèse.

## Installation locale

```bash
pip install -r requirements.txt
streamlit run app.py
```
