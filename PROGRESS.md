# Progression — Dossier Machine Learning (vue globale)

## Fait
- Rangement du dossier (2026-10-07) : dossiers renommés en `classification/`, `regression/`, `apprentissage-non-supervise/` ; aide-mémoire déplacé dans `docs/` ; README mis à jour.
- Projet non supervisé : terminé (voir `apprentissage-non-supervise/PROGRESS.md`).

## Reste à faire
- Après push : si l'app `creditrust.streamlit.app` pointe vers l'ancien chemin `Machine Learning & Classification /dashboard/app.py`, changer le chemin du fichier principal en `classification/dashboard/app.py` dans Streamlit Cloud.
- Doublons connus, volontairement non supprimés : images de `classification/assets/` = `regression/assets/` ; `titanic.csv` identique dans les deux ; notebooks 01 et 02 présents dans les deux mais différents.

## Décisions prises
- `regression/` garde son propre `.git` et reste ignoré par le dépôt principal.
- Aucun doublon supprimé sans accord.
