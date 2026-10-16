Preferences
===========

**Tags to scan:**
    When using the **Tags** scan type, you can select the tags that will be used for comparison.

**Word weighting:**
    See :ref:`word-weighting`.

**Match similar words:**
    See :ref:`similarity-matching`.

**Match pictures of different dimensions:**
    If you check this box, pictures of different dimensions will be allowed in the same
    duplicate group.

**Match pictures of different rotations:**
    If you check this box, pictures of different rotations will be allowed in the same
    duplicate group.

.. _filter-hardness:

**Filter Hardness:**
    The threshold needed for two files to be considered duplicates. A lower value means more
    duplicates. The meaning of the threshold depends on the scanning type (see :doc:`scan`).
    Only works for :ref:`worded <worded-scan>` and :ref:`picture blocks <picture-blocks-scan>`
    scans.

**Can mix file kind:**
    If you check this box, duplicate groups are allowed to have files with different extensions. If
    you don't check it, well, they aren't!

**Ignore duplicates hardlinking to the same file:**
    If this option is enabled, dupeGuru will verify duplicates to see if they refer to the same
    `inode`_. If they do, they will not be considered duplicates. (Only for OS X and Linux)

**Use regular expressions when filtering:**
    If you check this box, the filtering feature will treat your filter query as a
    **regular expression**. Explaining them is beyond the scope of this document. A good place to
    start learning it is `regular-expressions.info`_.

**Remove empty folders after delete or move:**
    When this option is enabled, folders are deleted after a file is deleted or moved and the folder
    is empty.

**Partially hash files bigger than:**
    Only used by the **Contents** and **Folders** scan types. Files bigger than this size are first
    compared by hashing samples taken at a few places in them. Files whose samples differ can't be
    duplicates and are never read in full, which saves time on big files that have the same size but
    different contents. Files whose samples match are then hashed in full, so only identical files
    are reported as duplicates.

.. _trust-samples:

**Don't hash them in full: trust matching samples (UNSAFE):**
    Reports files bigger than the size above as duplicates as soon as their samples match, without
    hashing them in full. This is faster, but files that differ anywhere outside the sampled parts
    are then reported as identical: for example files whose tags or other metadata were edited in
    place, downloads that are still incomplete, or damaged copies.

    .. warning::

        Deleting a file that was only matched by its samples can lose data. Only use this option if
        you know that the files you scan are either exact copies of each other or entirely
        different. After a scan, dupeGuru says how many duplicates were only matched by their
        samples, and the results' status line keeps showing it.

**Copy and Move:**
    Determines how the Copy and Move operations (in the Action menu) will behave.

* **Right in destination:** All files will be sent directly in the selected destination, without
  trying to recreate the source path at all.
* **Recreate relative path:** The source file's path will be re-created in the destination folder up
  to the root selection in the Directories panel. For example, if you added
  ``/Users/foobar/SomeFolder`` to your Directories panel and you move
  ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` to the destination
  ``/Users/foobar/MyDestination``, the final destination for the file will be
  ``/Users/foobar/MyDestination/SubFolder`` (``SomeFolder`` has been trimmed from source's path in
  the final destination.).
* **Recreate absolute path:** The source file's path will be re-created in the destination folder in
  its entirety. For example, if you move ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` to the
  destination ``/Users/foobar/MyDestination``, the final destination for the file will be
  ``/Users/foobar/MyDestination/Users/foobar/SomeFolder/SubFolder``.

In all cases, dupeGuru nicely handles naming conflicts by prepending a number to the destination
filename if the filename already exists in the destination.

**Custom Command:**
    This preference determines the command that will be invoked by the "Invoke Custom Command"
    action. You can invoke any external application through this action. This can be useful if,
    for example, you have a nice diffing application installed.

The format of the command is the same as what you would write in the command line, except that there
are 2 placeholders: **%d** and **%r**. These placeholders will be replaced by the path of the
selected dupe (%d) and the path of the selected dupe's reference file (%r).

If the path to your executable contains space characters, you should enclose it in "" quotes. You
should also enclose placeholders in quotes because it's very possible that paths to dupes and refs
will contain spaces. Here's an example custom command::

    "C:\Program Files\SuperDiffProg\SuperDiffProg.exe" "%d" "%r"

.. _inode: http://en.wikipedia.org/wiki/Inode
.. _regular-expressions.info: http://www.regular-expressions.info
