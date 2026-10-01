# Progression — Introduction à l'Apprentissage Non Supervisé

## Fait
- Notebook `nb_04_Apprentissage_Non_Supervisé.ipynb` entièrement traité, de bout en bout.
  - Toutes les cellules de code manquantes ont été complétées : application finale de K-means (K=5), visualisation des clusters (plusieurs combinaisons de variables), calcul des moyennes par cluster, dendrogramme, clustering hiérarchique agglomératif (K=5), visualisation et interprétation des clusters hiérarchiques, comparaison K-means vs hiérarchique, PCA (2 composantes) et visualisation des clusters projetés en 2D.
  - Toutes les questions du notebook (EDA + clustering + PCA) ont reçu une réponse rédigée directement dans le notebook (cellules markdown "> **Réponse** : ..."), basée sur les vrais résultats calculés (statistiques, inerties, moyennes de clusters, variance expliquée), pas des réponses génériques.
  - Le notebook a été exécuté intégralement avec `jupyter nbconvert --execute` : 0 erreur sur 128 cellules.

## Résultats clés obtenus
- K optimal choisi : **K=5** (coude de la courbe d'Elbow entre K=4 et K=5), cohérent entre K-means et clustering hiérarchique.
- 5 segments clients identifiés (ex. revenu élevé/score élevé = clients premium, revenu élevé/score faible = fort potentiel non activé, etc.).
- PCA à 2 composantes capture ~60% de la variance totale.

## Reste à faire
- Rien côté exercice technique. Possibilité (optionnelle) d'aller plus loin : coefficient de silhouette pour confirmer K=5, ou tester le clustering sans la variable `Gender` pour voir si les segments sont plus nets.

## Décisions prises
- K=5 retenu pour K-means et pour le clustering hiérarchique (nombre de clusters identique pour permettre la comparaison).
- `Gender` conservée (encodée en 0/1) parmi les variables de clustering, comme suggéré par les instructions du notebook.
