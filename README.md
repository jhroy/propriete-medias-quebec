# Deux manières d'explorer la propriété des médias au Québec

Ce répertoire contient le code et les données à la base de deux **infographies interactives** permettant d'explorer la propriété des médias au Québec&nbsp;:

## Par grappes de propriété
[![](images/grappes.png)](https://jhroy.github.io/propriete-medias-quebec/)

## Sur une carte
[![](images/carte.png)](https://jhroy.github.io/propriete-medias-quebec/carte/)

### Crédits techniques

- Données : colligées, compilées et vérifiées par Jean-Hugues Roy (avec l'utilisation de Claude, parfois, pour en vérifier la cohérence)
- Sources :
  - [Organigrammes de propriété du CRTC](https://crtc.gc.ca/ownership/fra/title_org.htm),
  - [Données ouvertes du Registre des entreprises (version du 1<sup>er</sup> avril 2026)](https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises),
  - Données sur les bénéficiaires du Collectif canadien de journalisme ([année 1 [2025]](https://cjc-ccj.ca/beneficiaires/beneficiaires-de-fonds-annee-1/), [année 2 [2026]](https://cjc-ccj.ca/beneficiaires/)),
  - [Carte des médias d'information du Québec du Centre d'études sur les médias](https://cem-admin.maps.arcgis.com/apps/dashboards/fdcbd1510de9413abba6eb783974bf08#).
- Géocodage via le script [**geo.py**](geo.py) mobilisant le [Référentiel québécois des adresses](https://www.donneesquebec.ca/recherche/dataset/referentiel-quebecois-des-adresses) du ministère des Ressources naturelles.
- Génération du code : Claude Code, mobilisant notamment [D3.js](https://d3js.org).

Version finale avant publication - 8 août 2026
