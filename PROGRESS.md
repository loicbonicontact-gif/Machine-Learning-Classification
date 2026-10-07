# Progression — Dossier Machine Learning (vue globale)

## Fait
- Rangement du dossier (2026-10-07) : dossiers renommés en `classification/`, `regression/`, `apprentissage-non-supervise/` ; aide-mémoire déplacé dans `docs/` ; README mis à jour.
- Projet non supervisé : terminé (voir `apprentissage-non-supervise/PROGRESS.md`).

- Notebooks d'entraînement regroupés dans `entrainement/` (nb_01, nb_02, nb_04 + leurs données/images) ; notebooks de régression ajoutés en copie dans `entrainement/regression/`.

## Reste à faire
- Après push : si l'app `creditrust.streamlit.app` pointe vers l'ancien chemin `Machine Learning & Classification /dashboard/app.py`, changer le chemin du fichier principal en `classification/dashboard/app.py` dans Streamlit Cloud.
- Doublons voulus : `entrainement/regression/` copie `regression/notebooks/` (et titanic.csv, 2 images).
- Doublons connus, volontairement non supprimés : images de `classification/assets/` = `regression/assets/` ; `titanic.csv` identique dans les deux ; notebooks 01 et 02 présents dans les deux mais différents.

- `nb_01` (3 erreurs : `df_scaled`, syntaxe) et `nb_04 loic` (1 erreur de syntaxe f-string) ont des cellules d'exercice non terminées : ce n'est pas lié au déplacement.

## Décisions prises
- `regression/` garde son propre `.git` et reste ignoré par le dépôt principal.
- Aucun doublon supprimé sans accord.
