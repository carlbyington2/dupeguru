Résultats
=========

.. contents::

Lorsque dupeGuru a terminé de rechercher les doublons, il affiche ses résultats sous la forme d'une liste de groupes de doublons.

À propos des groupes de doublons
--------------------------------

Un groupe de doublons est un groupe de fichiers qui correspondent tous entre eux. Chaque groupe possède un **fichier de référence** et un ou plusieurs **fichiers en double**. Le fichier de référence est le premier fichier du groupe. Sa case de marquage est désactivée. En dessous, et indentés, se trouvent les fichiers en double.

Vous pouvez marquer les fichiers en double, mais par défaut vous ne pouvez pas marquer le fichier de référence d'un groupe. C'est une mesure de sécurité pour éviter que dupeGuru ne supprime pas seulement les fichiers en double, mais aussi leur référence. Vous ne voulez sûrement pas cela, n'est-ce pas ?

Lorsque chaque fichier d'un groupe doit disparaître, activez **Autoriser le marquage des fichiers de référence** dans les préférences avancées. Les fichiers de référence ont alors eux aussi une case de marquage, et une référence marquée est affichée barrée. Vous marquez une référence en cliquant sur sa case de marquage, ou en la sélectionnant et en appuyant sur **Espace**. **Tout marquer** et **Inverser le marquage** laissent toujours les références de côté, et **Ne rien marquer** les démarque. Un fichier provenant d'un dossier de référence ne peut jamais être marqué. Avant de supprimer, déplacer ou copier des fichiers marqués incluant des références, dupeGuru demande une confirmation, et les fichiers supprimés ne peuvent pas être remplacés par des liens tant que des références sont marquées. Lorsqu'une référence est supprimée ou déplacée, le fichier suivant de son groupe prend la position de référence, non marqué.

Ce qui détermine quels fichiers sont des références et quels fichiers sont des doublons, c'est d'abord l'état de leur dossier. Un fichier provenant d'un dossier de référence sera toujours la référence dans un groupe de doublons. Si tous les fichiers proviennent d'un dossier normal, la taille détermine quel fichier sera la référence d'un groupe de doublons. dupeGuru part du principe que vous voulez toujours conserver le plus gros fichier, les plus gros fichiers prennent donc la position de référence.

Vous pouvez changer manuellement le fichier de référence d'un groupe. Pour ce faire, sélectionnez le fichier en double que vous voulez promouvoir en référence et cliquez sur **Actions-->Faire de la sélection la référence**.

Examen des résultats
--------------------

Bien que vous puissiez simplement cliquer sur **Édition-->Tout marquer** puis sur **Actions-->Envoyer les éléments marqués à la corbeille** pour supprimer rapidement tous les fichiers en double de vos résultats, il est toujours recommandé d'examiner tous les doublons avant de les supprimer.

Pour vous aider à examiner les résultats, vous pouvez afficher le **panneau de détails**. Ce panneau montre tous les détails du fichier actuellement sélectionné ainsi que ceux de sa référence. C'est très pratique pour déterminer rapidement si un doublon est réellement un doublon. Vous pouvez aussi double-cliquer sur un fichier pour l'ouvrir avec son application associée.

Si vous avez plus de faux doublons que de vrais doublons (si votre niveau de filtrage est très bas), la meilleure façon de procéder est d'examiner les doublons, de marquer les vrais doublons, puis de cliquer sur **Actions-->Envoyer les éléments marqués à la corbeille**. Si vous avez plus de vrais doublons que de faux doublons, vous pouvez à la place marquer tous les fichiers qui sont de faux doublons et utiliser **Actions-->Retirer les éléments marqués des résultats**.

Marquage et sélection
---------------------

Un doublon **marqué** est un doublon dont la petite case à côté est cochée. Un doublon **sélectionné** est un doublon mis en surbrillance. Les actions de sélection multiple peuvent s'effectuer dans dupeGuru de la manière standard (clic avec Maj/Commande/Ctrl). Vous pouvez inverser l'état de marquage de tous les doublons sélectionnés en appuyant sur **Espace**.

Afficher uniquement les doublons
--------------------------------

Lorsque ce mode est activé, les doublons sont affichés sans leur fichier de référence respectif. Vous pouvez sélectionner, marquer et trier cette liste, exactement comme en mode normal.

Les résultats de dupeGuru, en mode normal, sont triés selon le **fichier de référence** des groupes de doublons. Cela signifie que si vous voulez, par exemple, marquer tous les doublons portant l'extension « exe », vous ne pouvez pas simplement trier les résultats par « Type » pour regrouper tous les doublons exe, car un groupe peut être composé de plusieurs types de fichiers. C'est là que le mode Doublons uniquement entre en jeu. Pour marquer tous vos doublons « exe », il vous suffit de :

* Activer le mode Doublons uniquement.
* Ajouter la colonne « Type » avec le menu « Colonnes ».
* Cliquer sur cette colonne « Type » pour trier la liste par type.
* Repérer le premier doublon de type « exe ».
* Le sélectionner.
* Faire défiler la liste vers le bas pour repérer le dernier doublon de type « exe ».
* Maintenir Maj enfoncé et cliquer dessus.
* Appuyer sur Espace pour marquer tous les doublons sélectionnés.

.. _deltavalues:

Valeurs delta
-------------

Si vous activez cet interrupteur, les colonnes numériques afficheront la valeur relative à la référence du doublon au lieu des valeurs absolues. Ces valeurs delta seront aussi affichées dans une couleur différente, l'orange, afin que vous puissiez les repérer facilement. Par exemple, si un doublon fait 1,2 Mo et que sa référence fait 1,4 Mo, la colonne Taille affichera -0,2 Mo.

De plus, les valeurs non numériques seront aussi en orange si leur valeur est différente de celle de leur référence, et resteront en noir si leur valeur est la même. Combiné au tri des colonnes en mode Doublons uniquement, cela permet un filtrage post-analyse très puissant.

Doublons uniquement et valeurs delta
------------------------------------

Le mode Doublons uniquement révèle toute sa puissance lorsque vous l'utilisez avec l'interrupteur Valeurs delta activé. Lorsque vous l'activez, des valeurs relatives sont affichées à la place des valeurs absolues. Ainsi, si par exemple vous voulez retirer de vos résultats tous les doublons dont la taille diffère de plus de 300 Ko de celle de leur référence, vous pouvez trier les résultats en mode Doublons uniquement par taille, sélectionner tous les doublons inférieurs à -300 dans la colonne Taille, les supprimer, puis faire de même pour les doublons supérieurs à 300 en bas de la liste.

Il en va de même pour les valeurs non numériques : lorsque Doublons uniquement et Valeurs delta sont activés en même temps, le tri des colonnes regroupe les lignes selon qu'elles sont orange ou non. Exemple : vous avez effectué une analyse par contenu, mais vous ne voulez supprimer que les doublons qui ont le même nom de fichier ? Triez par nom de fichier et tous les doublons dont l'attribut nom de fichier est identique à celui de la référence seront regroupés, leur valeur étant en noir.

Vous pouvez aussi l'utiliser pour changer la priorité de référence de votre liste de doublons. Lorsque vous effectuez une nouvelle analyse, s'il n'y a pas de dossiers de référence, le fichier de référence de chaque groupe est le plus gros fichier. Si vous voulez changer cela, par exemple pour la date de modification la plus récente, vous pouvez trier les résultats en mode Doublons uniquement par date de modification en ordre **décroissant**, sélectionner tous les doublons dont la valeur delta de date de modification est supérieure à 0 et cliquer sur **Faire de la sélection la référence**. La raison pour laquelle l'ordre de tri doit être décroissant est que si 2 fichiers d'un même groupe de doublons sont sélectionnés lorsque vous cliquez sur **Faire de la sélection la référence**, seul le premier de la liste deviendra la référence, l'autre sera ignoré. Et comme vous voulez que le fichier modifié en dernier soit la référence, un ordre de tri décroissant vous assure que le premier élément de la liste sera le dernier modifié.

Filtrage
--------

dupeGuru prend en charge le filtrage post-analyse. Il vous permet de restreindre vos résultats afin d'effectuer des actions sur un sous-ensemble. Par exemple, vous pourriez facilement marquer tous les doublons dont le nom de fichier contient « copy » en utilisant le filtre.

Pour utiliser la fonction de filtrage, saisissez votre filtre dans le champ de recherche « Filtre » situé en haut à droite de la fenêtre de résultats. Ce que vous saisissez dans ce champ sera appliqué au *chemin complet* de chaque doublon des résultats. Seuls les *groupes* de doublons comportant au moins un doublon correspondant au filtre seront affichés.

Lorsque certains groupes contiennent des doublons qui ne correspondent pas tous au filtre, nous affichons tout de même tous les doublons du groupe. Toutefois, les doublons non correspondants sont en « mode référence ». Vous pouvez donc effectuer des actions comme « Tout marquer » en étant sûr de ne marquer que les doublons filtrés.

Pour revenir aux résultats non filtrés, videz le champ ou cliquez sur le « X ».

En mode simple (le mode par défaut), ce que vous saisissez comme filtre est la chaîne utilisée pour effectuer le filtrage proprement dit, à l'exception d'un caractère générique : **\***. Ainsi, si vous saisissez « [*] » comme filtre, il correspondra à tout ce qui contient des crochets [], quel que soit leur contenu.

Pour un filtrage plus avancé, vous pouvez activer « Utiliser des expressions régulières lors du filtrage ». La fonction de filtrage utilisera alors des **expressions régulières**. Une expression régulière est un langage de recherche de motifs dans du texte. Les expliquer dépasse le cadre de ce document. Un bon point de départ pour les apprendre est `regular-expressions.info`_.

Les correspondances ne sont pas sensibles à la casse, aussi bien en mode simple qu'en mode regexp.

Pour que le filtre corresponde, votre expression régulière n'a pas à correspondre à l'ensemble du nom de fichier, il suffit que celui-ci contienne une chaîne correspondant à l'expression.

Menu Actions
------------

**Vider la liste d'exclusion :**
    Retire toutes les correspondances ignorées que vous avez ajoutées. Vous devez lancer une
    nouvelle analyse pour que la liste d'exclusion fraîchement vidée soit effective.
**Exporter les résultats en XHTML :**
    Prend les résultats actuels et en crée un fichier XHTML. Les colonnes visibles au moment du
    clic sur ce bouton seront les colonnes présentes dans le fichier XHTML. Le fichier sera
    automatiquement ouvert dans votre navigateur par défaut.
**Envoyer les éléments marqués à la corbeille :**
    Envoie tous les doublons marqués à la corbeille, évidemment. Avant de poursuivre, des options
    de suppression vous seront présentées (voir ci-dessous).
**Déplacer les éléments marqués vers... :**
    Vous demande une destination, puis déplace tous les fichiers marqués vers cette destination.
    Le chemin du fichier source peut être recréé dans la destination, selon la préférence
    « Copier et déplacer ».
**Copier les éléments marqués vers... :**
    Vous demande une destination, puis copie tous les fichiers marqués vers cette destination.
    Le chemin du fichier source peut être recréé dans la destination, selon la préférence
    « Copier et déplacer ».
**Retirer les éléments marqués des résultats :**
    Retire tous les doublons marqués des résultats. Les fichiers eux-mêmes ne seront pas touchés
    et resteront où ils sont.
**Retirer la sélection des résultats :**
    Retire tous les doublons sélectionnés des résultats. Notez que tous les fichiers de référence
    sélectionnés seront ignorés, seuls les doublons peuvent être retirés avec cette action.
**Faire de la sélection la référence :**
    Promeut tous les doublons sélectionnés en référence. Si un doublon fait partie d'un groupe
    dont le fichier de référence provient d'un dossier de référence (en bleu), aucune action ne
    sera effectuée pour ce doublon. Si plus d'un doublon d'un même groupe est sélectionné, seul
    le premier de chaque groupe sera promu.
**Ajouter la sélection à la liste d'exclusion :**
    Retire d'abord tous les doublons sélectionnés des résultats, puis ajoute la correspondance de
    ce doublon avec la référence actuelle à la liste d'exclusion. Cette correspondance ne
    réapparaîtra plus dans les analyses suivantes. Le doublon lui-même peut revenir, mais il sera
    rapproché d'un autre fichier de référence. Vous pouvez vider la liste d'exclusion avec la
    commande Vider la liste d'exclusion.
**Ouvrir la sélection avec l'application par défaut :**
    Ouvre le fichier avec l'application associée au type du fichier sélectionné.
**Afficher la sélection dans le Finder :**
    Ouvre le dossier contenant le fichier sélectionné.
**Lancer la commande personnalisée :**
    Lance l'application externe que vous avez configurée dans vos préférences en utilisant la
    sélection actuelle comme arguments de l'appel. Si la sélection comprend des fichiers de
    référence, pour lesquels **%d** et **%r** sont le même fichier, dupeGuru demande d'abord une
    confirmation.
**Renommer la sélection :**
    Vous demande un nouveau nom, puis renomme le fichier sélectionné.

Options de suppression
----------------------

Ces options affectent le déroulement de la suppression des doublons. La plupart du temps, vous
n'avez besoin d'en activer aucune.

**Remplacer les fichiers supprimés par des liens :**
    Les fichiers supprimés sont remplacés par un lien vers le fichier de référence. Vous pouvez
    choisir de le remplacer soit par un `lien symbolique`_, soit par un `lien physique`_. Il vaut
    mieux lire les pages complètes de Wikipédia à leur sujet pour faire un choix éclairé, mais en
    bref, un lien symbolique est un raccourci vers le chemin du fichier. Si le fichier original
    est supprimé ou déplacé, le lien est rompu. Un lien physique est un lien vers le fichier
    *lui-même*. Ce lien vaut un « vrai » fichier. Ce n'est que lorsque *tous* les liens
    physiques vers un fichier sont supprimés que le fichier lui-même est supprimé.

    Sous OSX et Linux, cette fonctionnalité est entièrement prise en charge, mais sous Windows,
    c'est un peu compliqué. Windows XP ne la prend pas en charge, mais Vista et les versions
    ultérieures oui. Cependant, pour que la fonctionnalité marche, dupeGuru doit s'exécuter avec
    des privilèges administrateur.

**Supprimer directement les fichiers :**
    Au lieu d'envoyer les fichiers à la corbeille, les supprime directement. Cette option sert au
    dépannage et vous n'avez normalement pas besoin de l'activer, sauf si dupeGuru a du mal à
    supprimer normalement les fichiers, ce qui peut arriver lorsque vous essayez de supprimer des
    fichiers sur un stockage réseau (NAS).

.. _regular-expressions.info: http://www.regular-expressions.info
.. _lien physique: http://fr.wikipedia.org/wiki/Lien_physique
.. _lien symbolique: http://fr.wikipedia.org/wiki/Lien_symbolique
