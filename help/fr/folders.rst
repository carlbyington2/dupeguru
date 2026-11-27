Sélection des dossiers
======================

La première fenêtre que vous voyez au lancement de dupeGuru est la fenêtre de sélection des
dossiers. Cette fenêtre contient les informations de base dont dupeGuru a besoin pour démarrer
une analyse :

* Un choix du mode d'application
* Un choix du type d'analyse
* Les dossiers à analyser

Mode d'application
------------------

dupeGuru possède trois modes principaux : Standard, Musique et Image.

Le mode Standard convient à tout type de fichiers. Cela en fait le mode le plus polyvalent, mais
il est dépourvu des fonctionnalités spécialisées que possèdent les autres modes.

Le mode Musique n'analyse que les fichiers musicaux, mais il prend en charge la comparaison des
tags et sa fenêtre de résultats comporte de nombreuses colonnes d'information liées à l'audio.

Le mode Image n'analyse que les images, mais son type d'analyse par contenu est un puissant
comparateur flou capable de trouver des images similaires sans être strictement identiques.

Le choix d'un mode d'application ne change pas seulement les types d'analyse disponibles dans le
sélecteur ci-dessous, mais aussi les options disponibles dans le panneau des préférences. Par
conséquent, si vous voulez affiner votre analyse, assurez-vous d'ouvrir le panneau des
préférences **après** avoir sélectionné le mode d'application.

Type d'analyse
--------------

Ce sélecteur détermine le type d'analyse que nous allons effectuer. Voir :doc:`scan` pour plus de
détails sur les types d'analyse.

Liste des dossiers
------------------

Pour ajouter un dossier, cliquez sur le bouton **+**. Si vous avez déjà ajouté des dossiers, un
menu contextuel affichant la liste des dossiers récemment ajoutés apparaît. Vous pouvez cliquer
sur l'un d'eux pour l'ajouter directement à votre liste. Si vous cliquez sur le premier élément
du menu, **Ajouter un nouveau dossier...**, il vous sera demandé de choisir un dossier à ajouter.
Si vous n'avez jamais ajouté de dossier, aucun menu n'apparaît et il vous est directement demandé
de choisir un nouveau dossier à ajouter.

Une autre manière d'ajouter des dossiers à la liste consiste à les y glisser.

Pour retirer un dossier, sélectionnez-le et cliquez sur **-**. Si un sous-dossier est sélectionné
au moment du clic, le dossier sélectionné passera à l'état **exclu** (voir ci-dessous) au lieu
d'être retiré.

États des dossiers
------------------

Chaque dossier peut se trouver dans l'un de ces 3 états :

**Normal :**
    Les doublons trouvés dans ce dossier peuvent être supprimés.
**Référence :**
    Les doublons trouvés dans ce dossier **ne peuvent pas** être supprimés. Les fichiers de ce
    dossier ne peuvent se retrouver qu'en position de **référence** dans le groupe de doublons.
    Si plus d'un fichier provenant de dossiers de référence se retrouve dans le même groupe de
    doublons, un seul sera conservé. Les autres seront retirés du groupe.
**Exclu :**
    Les fichiers de ce répertoire ne seront pas inclus dans l'analyse.

L'état par défaut d'un dossier est, bien sûr, **Normal**. Vous pouvez utiliser l'état
**Référence** pour un dossier si vous voulez être certain de ne supprimer aucun fichier qu'il
contient.

Lorsque vous définissez l'état d'un répertoire, tous ses sous-dossiers héritent automatiquement
de cet état, sauf si vous définissez explicitement l'état d'un sous-dossier.

Pour modifier plusieurs dossiers à la fois, utilisez Ctrl-clic pour sélectionner des lignes
individuelles ou Maj-clic pour sélectionner une plage, comme dans la fenêtre de résultats.
Cliquez sur la cellule État de n'importe quelle ligne sélectionnée et choisissez Normal,
Référence ou Exclu. Le choix s'applique à chaque dossier sélectionné, tandis que la sélection et
les dossiers dépliés restent en place.

Par exemple, laissez Albums à Normal, dépliez-le, sélectionnez uniquement ses sous-dossiers
d'artistes, puis choisissez Référence. Albums reste Normal et les sous-dossiers plus profonds des
artistes héritent de Référence. Si un dossier parent et son enfant sont tous deux sélectionnés,
les deux reçoivent l'état choisi. Modifier l'état d'un parent réinitialise toujours les
surcharges de ses descendants selon les règles d'héritage habituelles.

Analyse
-------

Lorsque vous êtes prêt, cliquez sur le bouton **Analyser** pour lancer le processus d'analyse.
Une fois celui-ci terminé, les :doc:`results` vous seront présentés.
