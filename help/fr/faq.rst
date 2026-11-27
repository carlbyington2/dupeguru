Foire aux questions
===================

.. contents::

Qu'est-ce que dupeGuru ?
------------------------

dupeGuru est un outil permettant de trouver les fichiers en double sur votre ordinateur. Il
possède trois modes de fonctionnement : Standard, Musique et Image. Chaque mode a ses propres
préférences spécialisées.

Chaque mode propose plusieurs types d'analyse, comme le nom de fichier, le contenu ou les tags.
Certains types d'analyse disposent d'un algorithme de rapprochement flou avancé, qui vous permet
de trouver des doublons que d'autres outils de recherche de doublons, plus rigides, ne peuvent
pas trouver.

Qu'est-ce qui le rend spécial ?
-------------------------------

C'est surtout une question de personnalisation. Il existe de nombreuses options d'analyse qui
vous permettent d'obtenir le type de résultats que vous cherchez vraiment.

L'utilisation de dupeGuru est-elle sûre ?
-----------------------------------------

Très sûre. dupeGuru a été conçu pour vous éviter de supprimer des fichiers que vous ne vouliez
pas supprimer. D'abord, il y a le système de dossiers de référence qui vous permet de définir des
dossiers dans lesquels vous ne voulez absolument **pas** que dupeGuru vous laisse supprimer des
fichiers, ensuite il y a le système de référence de groupe qui garantit que vous conserverez
**toujours** au moins un membre du groupe de doublons.

Comment signaler un bogue ou suggérer une fonctionnalité ?
----------------------------------------------------------

dupeGuru est hébergé sur `GitHub`_, qui sert aussi au suivi des tickets. Le meilleur moyen de
signaler un bogue ou de suggérer une fonctionnalité est de vous inscrire sur GitHub et
d'`ouvrir un ticket`_.

La case de marquage d'un fichier que je veux supprimer est désactivée. Que dois-je faire ?
------------------------------------------------------------------------------------------

Vous ne pouvez pas marquer la référence (le premier fichier) d'un groupe de doublons. En
revanche, vous pouvez promouvoir un fichier en double au rang de référence. Ainsi, si un fichier
que vous voulez marquer est la référence, sélectionnez dans le groupe un doublon que vous voulez
promouvoir en référence et cliquez sur **Actions-->Faire de la sélection la référence**. Si le
fichier de référence provient d'un dossier de référence (nom de fichier écrit en bleu), vous ne
pouvez pas le retirer de la position de référence.

J'ai un dossier dans lequel je ne veux vraiment pas supprimer de fichiers.
--------------------------------------------------------------------------

Si vous voulez être certain que dupeGuru ne supprimera jamais de fichier d'un dossier donné,
veillez à définir son état sur **Référence** dans :doc:`folders`.

Que signifie cet avis « (X écartés) » dans la barre d'état ?
------------------------------------------------------------

Dans certains cas, certaines correspondances ne sont pas incluses dans les résultats finaux pour
des raisons de sécurité. Prenons un exemple. Nous avons 3 fichiers : A, B et C. Nous les
analysons avec un niveau de filtrage bas. L'analyseur détermine que A correspond à B, A
correspond à C, mais que B ne correspond **pas** à C. Ici, dupeGuru a un petit problème. Il ne
peut pas créer un groupe de doublons contenant A, B et C car tous les fichiers du groupe ne
correspondraient pas entre eux. Il pourrait créer 2 groupes : un groupe A-B et un groupe A-C,
mais il ne le fait pas, pour des raisons de sécurité. Réfléchissons : si B ne correspond pas à C,
cela signifie probablement que B, C, ou les deux, ne sont pas réellement des doublons. S'il y
avait 2 groupes (A-B et A-C), vous finiriez par supprimer à la fois B et C. Et si l'un d'eux
n'est pas un doublon, ce n'est vraiment pas ce que vous voulez faire, n'est-ce pas ? Dans un cas
comme celui-ci, dupeGuru écarte donc la correspondance A-C (et ajoute un avis dans la barre
d'état). Ainsi, si vous supprimez B et relancez une analyse, vous obtiendrez une correspondance
A-C dans vos prochains résultats.

Je veux marquer tous les fichiers d'un dossier donné. Que puis-je faire ?
-------------------------------------------------------------------------

Activez le mode :doc:`Doublons uniquement <results>` et cliquez sur la colonne Dossier pour
trier vos doublons par dossier. Il vous sera alors facile de sélectionner tous les doublons d'un
même dossier, puis d'appuyer sur Espace pour marquer tous les doublons sélectionnés.

Je veux retirer tous les fichiers dont la taille diffère de plus de 300 Ko de celle de leur fichier de référence. Que puis-je faire ?
-------------------------------------------------------------------------------------------------------------------------------------

* Activez le mode :doc:`Doublons uniquement <results>`.
* Activez le mode **Valeurs delta**.
* Cliquez sur la colonne « Taille » pour trier les résultats par taille.
* Sélectionnez tous les doublons inférieurs à -300.
* Cliquez sur **Retirer la sélection des résultats**.
* Sélectionnez tous les doublons supérieurs à 300.
* Cliquez sur **Retirer la sélection des résultats**.

Je veux que mes fichiers modifiés le plus récemment deviennent des fichiers de référence. Que puis-je faire ?
-------------------------------------------------------------------------------------------------------------

* Activez le mode :doc:`Doublons uniquement <results>`.
* Activez le mode **Valeurs delta**.
* Cliquez sur la colonne « Modification » pour trier les résultats par date de modification.
* Cliquez à nouveau sur la colonne « Modification » pour inverser l'ordre de tri.
* Sélectionnez tous les doublons supérieurs à 0.
* Cliquez sur **Faire de la sélection la référence**.

Je veux marquer tous les doublons contenant le mot « copy ». Comment faire ?
----------------------------------------------------------------------------

* Saisissez « copy » dans le champ « Filtre » en haut à droite de la fenêtre de résultats.
* Cliquez sur **Marquer --> Tout marquer**.

Je veux retirer toutes les chansons dont la durée diffère de plus de 3 secondes de celle de leur fichier de référence. Que puis-je faire ?
------------------------------------------------------------------------------------------------------------------------------------------

* Activez le mode :doc:`Doublons uniquement <results>`.
* Activez le mode **Valeurs delta**.
* Cliquez sur la colonne « Durée » pour trier les résultats par durée.
* Sélectionnez tous les doublons inférieurs à -00:03.
* Cliquez sur **Retirer la sélection des résultats**.
* Sélectionnez tous les doublons supérieurs à 00:03.
* Cliquez sur **Retirer la sélection des résultats**.

Je veux que mes chansons au débit le plus élevé deviennent des fichiers de référence. Que puis-je faire ?
---------------------------------------------------------------------------------------------------------

* Activez le mode :doc:`Doublons uniquement <results>`.
* Activez le mode **Valeurs delta**.
* Cliquez sur la colonne « Débit » pour trier les résultats par débit.
* Cliquez à nouveau sur la colonne « Débit » pour inverser l'ordre de tri.
* Sélectionnez tous les doublons supérieurs à 0.
* Cliquez sur **Faire de la sélection la référence**.

Je ne veux pas que les versions [live] et [remix] de mes chansons soient comptées comme des doublons. Comment faire ?
---------------------------------------------------------------------------------------------------------------------

Si votre seuil de comparaison est suffisamment bas, vous vous retrouverez probablement avec des
versions live et remix de vos chansons dans vos résultats. Il n'y a rien que vous puissiez faire
pour l'empêcher, mais vous pouvez facilement les retirer de vos résultats après l'analyse : le
filtrage post-analyse. Si, par exemple, vous voulez retirer toutes les chansons comportant
quelque chose entre crochets [] :

* Saisissez « [*] » dans le champ « Filtre » en haut à droite de la fenêtre de résultats.
* Cliquez sur **Marquer --> Tout marquer**.
* Cliquez sur **Actions --> Retirer la sélection des résultats**.

Le curseur « Niveau de filtrage » des préférences ne bouge pas !
----------------------------------------------------------------

Ce curseur n'est pertinent que pour les types d'analyse qui prennent en charge le « flou ». De
nombreux types d'analyse, comme le type « Contenu », ne prennent en charge que les correspondances
exactes. Lorsque ces types sont sélectionnés, le curseur est désactivé.

Sur certains systèmes, le fait qu'il soit désactivé est plus difficile à voir que sur d'autres,
mais si vous ne pouvez pas déplacer le curseur, cela signifie que cette préférence n'est pas
pertinente pour votre type d'analyse actuel.

J'ai essayé d'envoyer mes doublons à la corbeille, mais dupeGuru m'indique qu'il ne peut pas le faire. Pourquoi ? Que puis-je faire ?
-------------------------------------------------------------------------------------------------------------------------------------

La plupart du temps, la raison pour laquelle dupeGuru ne peut pas envoyer des fichiers à la
corbeille tient aux permissions des fichiers. Vous avez besoin des permissions d'*écriture* sur
les fichiers que vous voulez envoyer à la corbeille.

Si dupeGuru vous pose encore des problèmes après la correction de vos permissions, essayez
d'activer l'option « Supprimer directement les fichiers » qui vous est proposée lorsque vous
activez « Envoyer à la corbeille ». Cela n'enverra pas les fichiers à la corbeille, mais les
supprimera immédiatement. Dans certains cas, par exemple sur un stockage réseau (NAS), il est
arrivé que cela fonctionne alors que la suppression normale échouait.

Pourquoi l'analyse par contenu du mode Image est-elle si lente ?
----------------------------------------------------------------

Cette méthode d'analyse est très différente des autres méthodes. Elle peut détecter des photos en
double même si elles ne sont pas exactement identiques. Cette fonctionnalité très sympathique a
un coût : le temps. Chaque image doit être comparée individuellement et de façon floue à toutes
les autres, ce qui demande beaucoup de puissance de calcul.

Si vous avez seulement besoin de trouver des doublons exacts, utilisez simplement le mode
Standard de dupeGuru avec la méthode d'analyse par contenu. Si vos photos ont des tags EXIF, vous
pouvez aussi essayer la méthode d'analyse « EXIF », bien plus rapide.

Où se trouvent les fichiers utilisateur ?
-----------------------------------------

Pour une raison ou une autre, vous voudrez peut-être supprimer ou modifier les fichiers
utilisateur de dupeGuru (journaux de débogage, caches, etc.). Leur emplacement dépend de votre
plateforme :

* Linux : ``~/.local/share/data/Hardcoded Software/dupeGuru``
* Mac OS X : ``~/Library/Application Support/dupeGuru``

Les préférences sont stockées ailleurs :

* Linux : ``~/.config/Hardcoded Software/dupeGuru.conf``
* Mac OS X : dans le système intégré ``defaults``, sous le nom ``com.hardcoded-software.dupeguru``

.. _GitHub: https://github.com/carlbyington2/dupeguru
.. _ouvrir un ticket: https://github.com/carlbyington2/dupeguru/issues
