Repriorisation des doublons
===========================

dupeGuru essaie de déterminer automatiquement quel doublon doit occuper la position de
référence de chaque groupe, mais il se trompe parfois. Dans de nombreux cas, un tri astucieux
des doublons avec les options « Valeurs delta » et « Doublons uniquement », en plus de l'action
« Faire de la sélection la référence », fait l'affaire, mais parfois une option plus puissante
est nécessaire. C'est là que la boîte de dialogue de repriorisation entre en jeu. Vous pouvez
l'ouvrir via l'élément « Repriorisation des résultats » du menu « Actions ».

Cette boîte de dialogue vous permet de choisir des critères selon lesquels un doublon de
référence sera sélectionné dans chaque groupe de doublons. La liste des critères disponibles se
trouve à gauche et la liste des critères que vous avez choisis à droite.

Un critère est une catégorie suivie d'un argument. Par exemple, « Taille (Plus grande) » signifie
que le doublon ayant la plus grande taille l'emporte. « Dossier (/foo/bar) » signifie que les
doublons situés dans ce dossier l'emportent. Pour ajouter un critère à la liste de droite,
sélectionnez d'abord une catégorie dans la liste déroulante, puis un sous-argument dans la liste
située en dessous, et cliquez enfin sur le bouton en forme de flèche pointant vers la droite.

L'ordre de la liste de droite est important (vous pouvez réordonner les éléments par
glisser-déposer). Pour choisir un doublon pour la position de référence, le premier critère est
utilisé en premier. En cas d'égalité, le deuxième critère est utilisé, et ainsi de suite. Par
exemple, si vos arguments sont « Taille (Plus grande) » puis « Nom de fichier (Ne se termine pas
par un nombre) », le fichier de référence choisi dans un groupe sera le plus gros fichier ; si
deux fichiers ou plus ont la même taille, celui dont le nom de fichier ne se termine pas par un
nombre sera utilisé. Lorsque tous les critères aboutissent à des égalités, l'ordre dans lequel
les doublons se trouvaient précédemment dans le groupe est utilisé.
