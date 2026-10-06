# Progression — Introduction à l'Apprentissage Non Supervisé

## Contexte global (brief NexaData Consulting / GlobalShop Direct)
Le projet complet comporte 5 activités :
1. Notebook individuel sur Mall Customers (clustering + PCA) — **terminé**.
2. Notebook 2 en binôme : nettoyage + RFM sur `online_retail.csv` — **terminé**.
3. Clustering + PCA sur les données RFM, choix de K, profils métier (Champions, Fidèles, À Risque, Occasionnels) — **terminé**.
4. Dashboard Streamlit (`app.py`) : KPI, scatterplots PCA, boxplots par cluster, simulateur de profil client — **terminé**.
5. Support de présentation (10 slides HTML) + restitution orale — **terminé**, prêt pour la présentation.

## Fait
- **Activité 1 (Notebook 1)** : `notebooks/nb_04_Apprentissage_Non_Supervisé.ipynb` entièrement traité, de bout en bout.
  - Toutes les cellules de code manquantes complétées : K-means final (K=5), visualisations multi-variables, moyennes par cluster, dendrogramme, clustering hiérarchique agglomératif (K=5), comparaison K-means vs hiérarchique, PCA (2 composantes, variables numériques uniquement) et visualisation des clusters projetés en 2D.
  - Audité via Arena Mode : un écart trouvé et corrigé (PCA incluait `Gender` par erreur — corrigé, variance expliquée passée de ~60% à ~78%).
  - Exécuté intégralement : 0 erreur sur 128 cellules.
- **Activités 2 et 3 (Notebook perso)** : `notebooks/online_retail_clustering_rfm.ipynb` entièrement traité en binôme, pas à pas.
  - Nettoyage (annulations, CustomerID manquants, quantités/prix non positifs, doublons), construction RFM, transformation log + standardisation, K-means (K=4), profils moyens ET médians par cluster, visualisations, PCA (93,9% de variance en 2D), section clustering hiérarchique (dendrogramme + AgglomerativeClustering + comparaison avec K-means) complétée par moi à la demande de l'utilisateur.
  - Audité via Arena Mode à deux reprises : un écart trouvé (colonne résiduelle `DerniereDate` dans le tableau RFM) et corrigé. Conformité à l'énoncé revérifiée (moyennes ET médianes RFM demandées par le brief, ajoutées).
  - Exécuté intégralement : 0 erreur sur 66 cellules.
- **Notebook du binôme** : `notebooks/Client GlobalShop Direct.ipynb` — adapté pour lire `online_retail.csv` au lieu du `.xlsx` supprimé. Exécuté intégralement (0 erreur), exporte deux CSV dans `notebooks/exports/` : `globalshop_clients_segments.csv` (tous les clients + segment + recommandations) et `globalshop_pca_echantillon.csv` (1000 clients pour les graphiques PCA).
- **Activité 4 (Dashboard Streamlit)** : `app.py` + dossier `pages/` (architecture multipage native Streamlit, menu automatique dans la barre latérale).
  - Pipeline commun (nettoyage, RFM, K-means K=4, PCA) centralisé dans `rfm_pipeline.py`, mis en cache (`st.cache_data`/`st.cache_resource`) — calcul complet en ~1,8s sur 541k lignes.
  - Pages : Accueil (contexte), Méthodologie (explications pédagogiques), KPI, PCA, Boxplots, Simulateur (saisie RFM → segment + action marketing recommandée), Synthèse (conclusion orale).
  - Adapté pour une présentation orale : texte agrandi pour la projection, palette de couleurs sans rouge ni vert (accessibilité daltonisme) sur tous les graphiques.
  - Simulateur corrigé : le scaler/kmeans reçoit désormais un DataFrame avec noms de colonnes (plus de warning sklearn silencieux lors de la démo live).
- **Activité 5 (Support de présentation)** : deck de 10 slides HTML (Artifact Claude) — https://claude.ai/artifact/3RksBABD9JHBvF6sXvvtDN
  - Structure : couverture → contexte → démarche (5 étapes) → nettoyage → RFM → clustering K-means → PCA → KPI → segments (profils + actions marketing) → dashboard/conclusion.
  - Design retravaillé avec le skill UI/UX Pro Max : palette bleu marine/ambre/violet/gris (sans rouge ni vert), typographie Space Grotesk + IBM Plex Sans, pagination et notes orateur sur chaque slide.
  - Audité via Arena Mode (3 agents : Streamlit, exactitude des slides, cohérence cross-livrables) : 0 chiffre inventé, tous les chiffres vérifiés contre le pipeline réel. Corrections appliquées : notes orateur ajoutées sur toutes les slides, footer manquant corrigé sur la dernière slide.
  - **Artifact privé** : à partager depuis le menu Share de la page si besoin de l'ouvrir depuis un autre compte le jour de la présentation.

## Résultats clés obtenus
- **Notebook 1 (Mall Customers)** : K=5 optimal, PCA à 2 composantes (Age/Revenu/Score) capture ~78% de la variance.
- **Notebook RFM (Online Retail)** : K=4 optimal, PCA à 2 composantes capture 93,9% de la variance. Segments nommés automatiquement selon leurs moyennes réelles : Champions, Fidèles, Occasionnels, À Risque.

## Reste à faire
- Checklist avant la présentation : lancer le Streamlit en avance et cliquer sur chaque page pour chauffer le cache, vérifier l'accès à l'artifact slides depuis la salle de présentation, tester le simulateur une fois en live.
- Commits locaux en attente de push sur GitHub — à faire quand demandé par l'utilisateur (dernière instruction explicite : "ne fais rien je vais lui envoyer moi meme").

## Décisions prises
- K=5 retenu pour Mall Customers, K=4 retenu pour Online Retail RFM (choisi via méthode du coude).
- `Gender` exclue de la PCA sur Mall Customers (variables numériques uniquement).
- `Online_Retail.xlsx` converti en CSV (`online_retail.csv`) pour coller au nom de fichier attendu par le brief ; le fichier xlsx original a été supprimé après conversion.
- Section clustering hiérarchique du notebook personnel remplie directement par Claude (à la demande explicite de l'utilisateur), initialement prévue pour le binôme.
- Dashboard Streamlit : architecture multipage native (dossier `pages/`) plutôt qu'un script unique, pour correspondre à un vrai usage de présentation avec menu de navigation.
- Palette de couleurs du dashboard : bleu/orange/violet/gris (jamais rouge/vert) pour rester lisible par les personnes daltoniennes en présentation.
- Push GitHub différé : on reste en local pour l'instant.
