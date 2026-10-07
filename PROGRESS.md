# Progression — Dossier Machine Learning (vue globale)

## Fait
- Rangement du dossier (2026-10-07) : dossiers renommés en `classification/`, `regression/`, `apprentissage-non-supervise/` ; aide-mémoire déplacé dans `docs/` ; README mis à jour.
- Projet non supervisé : terminé (voir `apprentissage-non-supervise/PROGRESS.md`).

- Notebooks d'entraînement regroupés dans `entrainement/` (nb_01, nb_02, nb_04 + leurs données/images) ; notebooks de régression ajoutés en copie dans `entrainement/regression/`.

- Tous les notebooks d'`entrainement/` sont traités et exécutés sans erreur (nb_01 et nb_04 corrigés ; régression nb_01/nb_02 remplis à partir des versions traitées de classification, même sujet).

- `entrainement/` aplati : `notebooks/` (nb_01 à nb_04, suffixe « loic »), `data/`, `assets/`. 4 notebooks exécutés, 0 erreur. Anciens sous-dossiers supprimés (commit 112b368), poussé sur GitHub.

## Reste à faire
- Après push : si l'app `creditrust.streamlit.app` pointe vers l'ancien chemin `Machine Learning & Classification /dashboard/app.py`, changer le chemin du fichier principal en `classification/dashboard/app.py` dans Streamlit Cloud.
- `entrainement/notebooks/` : un seul exemplaire de chaque notebook ; les originaux de la régression restent dans `regression/` (dépôt indépendant, aussi traité et poussé).
- Doublons connus, volontairement non supprimés : images de `classification/assets/` = `regression/assets/` ; `titanic.csv` identique dans les deux ; notebooks 01 et 02 présents dans les deux mais différents.


## Décisions prises
- `regression/` garde son propre `.git` et reste ignoré par le dépôt principal.
- Aucun doublon supprimé sans accord.
