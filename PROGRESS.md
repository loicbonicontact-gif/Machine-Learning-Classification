# Progression — Dossier Machine Learning (vue globale)

## Fait
- Rangement du dossier (2026-10-07) : dossiers renommés en `classification/`, `regression/`, `apprentissage-non-supervise/` ; aide-mémoire déplacé dans `docs/` ; README mis à jour.
- Projet non supervisé : terminé (voir `apprentissage-non-supervise/PROGRESS.md`).

- Notebooks d'entraînement regroupés dans `entrainement/` (nb_01, nb_02, nb_04 + leurs données/images) ; notebooks de régression ajoutés en copie dans `entrainement/regression/`.

- Tous les notebooks d'`entrainement/` sont traités et exécutés sans erreur (nb_01 et nb_04 corrigés ; régression nb_01/nb_02 remplis à partir des versions traitées de classification, même sujet).

## Reste à faire
- Après push : si l'app `creditrust.streamlit.app` pointe vers l'ancien chemin `Machine Learning & Classification /dashboard/app.py`, changer le chemin du fichier principal en `classification/dashboard/app.py` dans Streamlit Cloud.
- Doublons voulus : `entrainement/regression/` copie `regression/notebooks/` (+ titanic.csv, 2 images) ; nb_01 et nb_02 y sont les versions traitées (identiques à celles de `entrainement/classification/`). Les originaux vides restent dans `regression/` (dépôt indépendant, non modifié).
- Doublons connus, volontairement non supprimés : images de `classification/assets/` = `regression/assets/` ; `titanic.csv` identique dans les deux ; notebooks 01 et 02 présents dans les deux mais différents.


## Décisions prises
- `regression/` garde son propre `.git` et reste ignoré par le dépôt principal.
- Aucun doublon supprimé sans accord.
