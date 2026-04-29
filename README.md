# Cartographie des médias — réseau de propriété

Visualisation interactive du réseau de propriété des médias québécois
(éditeurs, radiodiffuseurs, stations, publications, individus et holdings).

## Aperçu

- **490 nœuds** répartis en 9 types (Éditeur, Radiodiffuseur, Réseau, Holding,
  Plateforme, Fiducie, Individu, Station, Publication)
- **427 liens** de propriété (pourcentage ou statut)
- **Encodage visuel** :
  - Cercles pour les Éditeurs et Radiodiffuseurs, dont le diamètre est
    proportionnel à la racine carrée du montant déclaré (capital).
  - Rectangles gris pour les Stations et Publications.
  - Cercles rouges pour les Individus.
  - Couleurs distinctes pour les autres types (holdings, réseaux, etc.).

## Déploiement sur GitHub Pages

### Méthode rapide (recommandée)

1. Créer un nouveau dépôt GitHub (par exemple `cartographie-medias-qc`).
2. Téléverser `index.html` à la racine du dépôt.
3. Ouvrir l'onglet **Settings** → **Pages**.
4. Sous *Source*, choisir la branche `main` et le dossier `/ (root)`.
5. Cliquer sur **Save**. GitHub publiera la page à l'adresse
   `https://<utilisateur>.github.io/<nom-du-depot>/` (compter ~1 minute).

Le fichier `index.html` est entièrement autonome : D3.js (v7) et l'ensemble
des données sont incorporés à l'intérieur. Aucun serveur, aucune base de
données, aucun appel réseau au chargement (sauf les polices Google Fonts,
optionnelles — la page reste fonctionnelle si elles sont bloquées).

### Hébergement alternatif

Le même fichier fonctionne tel quel sur Netlify, Vercel, votre site
universitaire, ou en l'ouvrant simplement par double-clic dans un navigateur.

## Utilisation

| Geste                                | Effet                                            |
|--------------------------------------|--------------------------------------------------|
| Survol d'un nœud                     | Affiche la fiche détaillée et met en évidence les liens directs |
| Clic                                 | Verrouille la mise en évidence                   |
| Glisser-déposer un nœud              | Le repositionne dans la simulation               |
| Molette / pincement                  | Zoom                                             |
| Glisser le fond                      | Déplacement                                      |
| Champ de recherche                   | Filtre par nom, NEQ, ville ou activité           |
| Clic sur un type dans la légende     | Masque ou réaffiche les nœuds de ce type         |
| **Recentrer** / **Réorganiser**      | Restaure la vue ou relance la simulation         |
| **Geler la simulation**              | Fige les positions pour faire une capture d'écran |

## Mise à jour des données

Les données sont incorporées en JSON à l'intérieur de `index.html`,
juste après la balise `<script>const DATA = ...</script>`. Pour modifier
le réseau, deux options :

1. **Édition manuelle** : remplacer l'objet `DATA` par un nouveau JSON
   respectant la structure `{ nodes: [...], links: [...] }`.
2. **Régénération depuis CSV** : exécuter le script `build.py` (fourni
   séparément, sur demande) qui prend `noeuds.csv` et `liens.csv` et
   reconstruit `index.html`.

### Schéma des CSV sources

`noeuds.csv` (un nœud par ligne) :

```
type, montant, neq, nom1, jurForme, act1Code, act1Desc, act2Code,
act2Desc, localité, dateConsti, adr1, adr2, adr3, adr4
```

Le champ `montant` utilise la virgule comme séparateur décimal (format québécois).
Seuls les Éditeurs et Radiodiffuseurs portent un montant.

`liens.csv` (une relation par ligne) :

```
propriétaire, lien, propriété
```

Le champ `lien` peut être un pourcentage (avec virgule décimale) ou un
descripteur textuel (`Majoritaire`, `Non majoritaire`, `Associés`,
`commanditaire`).

## Compatibilité

Navigateurs modernes (Chrome, Firefox, Safari, Edge — versions
récentes). Le rendu reste utilisable sur mobile, mais l'expérience est
optimale sur écran large.

## Crédits techniques

- [D3.js](https://d3js.org) v7 (BSD 3-Clause)
- Polices : *Fraunces* et *Bricolage Grotesque* (Google Fonts, OFL)
- Données : colligées par Jean-Hugues Roy; sources : CRTC, Registre des entreprises, Collectif canadien de journalisme
- Génération du code : Claude
