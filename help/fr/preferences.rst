Préférences
===========

**Tags à analyser :**
    Lorsque vous utilisez le type d'analyse **Tags**, vous pouvez sélectionner les tags qui
    seront utilisés pour la comparaison.

**Pondération des mots :**
    Voir :ref:`word-weighting`.

**Rapprocher les mots similaires :**
    Voir :ref:`similarity-matching`.

**Rapprocher les images de dimensions différentes :**
    Si vous cochez cette case, des images de dimensions différentes pourront se trouver dans le
    même groupe de doublons.

**Rapprocher les images d'orientations différentes :**
    Si vous cochez cette case, des images d'orientations différentes pourront se trouver dans le
    même groupe de doublons.

.. _filter-hardness:

**Niveau de filtrage :**
    Le seuil nécessaire pour que deux fichiers soient considérés comme des doublons. Une valeur
    plus basse signifie plus de doublons. La signification du seuil dépend du type d'analyse
    (voir :doc:`scan`). Ne fonctionne que pour les analyses :ref:`par mots <worded-scan>` et
    :ref:`par blocs d'image <picture-blocks-scan>`.

**Peut mélanger les types de fichiers :**
    Si vous cochez cette case, les groupes de doublons peuvent contenir des fichiers ayant des
    extensions différentes. Si vous ne la cochez pas, eh bien, ils ne le peuvent pas !

**Ignorer les doublons liés par lien physique au même fichier :**
    Si cette option est activée, dupeGuru vérifiera les doublons pour voir s'ils renvoient au
    même `inode`_. Si c'est le cas, ils ne seront pas considérés comme des doublons. (Uniquement
    pour OS X et Linux)

**Utiliser des expressions régulières lors du filtrage :**
    Si vous cochez cette case, la fonction de filtrage traitera votre requête de filtre comme une
    **expression régulière**. Les expliquer dépasse le cadre de ce document. Un bon point de
    départ pour les apprendre est `regular-expressions.info`_.

**Supprimer les dossiers vides après suppression ou déplacement :**
    Lorsque cette option est activée, les dossiers sont supprimés après la suppression ou le
    déplacement d'un fichier si le dossier est vide.

**Hachage partiel des fichiers plus gros que :**
    Utilisé uniquement par les types d'analyse **Contenu** et **Dossiers**. Les fichiers plus
    gros que cette taille sont d'abord comparés à partir d'échantillons prélevés à quelques
    endroits, de sorte que les fichiers qui diffèrent à ces endroits ne sont jamais lus en
    entier. Cela fait gagner du temps sur les gros fichiers de même taille. Les fichiers dont les
    échantillons correspondent sont tout de même comparés en entier.

**Copier et déplacer :**
    Détermine le comportement des opérations Copier et Déplacer (dans le menu Actions).

* **Directement dans la destination :** Tous les fichiers seront envoyés directement dans la
  destination choisie, sans essayer de recréer le chemin source.
* **Recréer le chemin relatif :** Le chemin du fichier source sera recréé dans le dossier de
  destination jusqu'à la racine de la sélection dans le panneau des répertoires. Par exemple, si
  vous avez ajouté ``/Users/foobar/SomeFolder`` à votre panneau des répertoires et que vous
  déplacez ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` vers la destination
  ``/Users/foobar/MyDestination``, la destination finale du fichier sera
  ``/Users/foobar/MyDestination/SubFolder`` (``SomeFolder`` a été retiré du chemin source dans la
  destination finale).
* **Recréer le chemin absolu :** Le chemin du fichier source sera recréé en entier dans le
  dossier de destination. Par exemple, si vous déplacez
  ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` vers la destination
  ``/Users/foobar/MyDestination``, la destination finale du fichier sera
  ``/Users/foobar/MyDestination/Users/foobar/SomeFolder/SubFolder``.

Dans tous les cas, dupeGuru gère élégamment les conflits de noms en ajoutant un nombre au début
du nom du fichier de destination si ce nom existe déjà dans la destination.

**Autoriser le marquage des fichiers de référence :**
    Dans l'onglet Avancé. Lorsque cette option est activée, les fichiers de référence ont eux
    aussi une case de marquage, de sorte que chaque fichier d'un groupe peut être supprimé,
    déplacé ou copié. Voir :doc:`results` pour savoir comment se comportent les références
    marquées et comment dupeGuru les protège.

**Commande personnalisée :**
    Cette préférence détermine la commande qui sera lancée par l'action « Lancer la commande
    personnalisée ». Vous pouvez lancer n'importe quelle application externe grâce à cette
    action. Cela peut être utile si, par exemple, vous avez installé une bonne application de
    comparaison (diff).

Le format de la commande est le même que celui que vous écririez en ligne de commande, sauf qu'il
y a 2 marqueurs de substitution : **%d** et **%r**. Ces marqueurs seront remplacés par le chemin
du doublon sélectionné (%d) et le chemin du fichier de référence du doublon sélectionné (%r).

Si le chemin de votre exécutable contient des espaces, vous devez l'entourer de guillemets "". Il
est aussi recommandé d'entourer les marqueurs de guillemets, car les chemins des doublons et des
références contiendront très probablement des espaces. Voici un exemple de commande
personnalisée ::

    "C:\Program Files\SuperDiffProg\SuperDiffProg.exe" "%d" "%r"

.. _inode: http://en.wikipedia.org/wiki/Inode
.. _regular-expressions.info: http://www.regular-expressions.info
