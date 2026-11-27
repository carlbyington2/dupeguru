# Why this fork?

The Fedora package is built from the fedora-build branch of
https://github.com/carlbyington2/dupeguru. The upstream should be
https://github.com/arsenetar/dupeguru but that version is almost
dormant. The last release was four years ago, and there are many
critical outstanding pull requests that have not been merged.

## Merged pull requests

This branch is a fork of https://github.com/arsenetar/dupeguru with
the following pull requests merged:

* PR1395 - core: guard copy_or_move when no location path matches dupe parent
* PR1393 - Set the application DesktopFileName
* PR1392 - Port to PyQt6
* PR1390 - Add StartupWMClass to desktop files to ensure DupeGuru icon is shown in launcher. Background:
* PR1368 - perf: configurable scan speed for picture mode (up to 16x faster)
* PR1365 - Fix SQL injection in cache modules
* PR1364 - Fix XXE vulnerabilities in XML parsing
* PR1363 - Fix command injection in Custom Command
* PR1238 - updated polish translation
* PR1207 - Update french translation
* PR1134 - I18n: Update Russian language
* PR1417 - move code into dupeguru namespace for fedora build
* PR1410 - fix: Don't crash on startup when a saved folder is unreachable
* PR1415 - Only treat files as hardlinks when the device matches too
* PR1416 - fix: Report a problem instead of crashing on relative copy/move
* PR1427 - feat: Add alphabetical and natural filename order criteria
* PR1428 - fix: Fully hash big files whose samples match before matching them
* PR1431 - fix: walk directories iteratively to avoid RecursionError during scans
* PR1432 - Fix picture scans crashing on incompatible cache schemas
* PR1435 - fix: Pick the same reference in every scan when files tie on every rule
* PR1436 - feat: Allow marking reference files, and confirm actions on them
* PR1437 - fix: Select the revealed file even in a folder Explorer has not listed
* git c16d627 - cleanup 2015 license change from BSD to GPLv3
* git 81ecf63 - cleanup packaging requirements, remove references to OSX cocoa
* git 788503e - remove reference to obsolete OSX cocoa version
* git 85c382c - gunnerman1/dupeguru - feat: Apply folder states to selected rows and add Windows release
* git e42dd4e - gunnerman1/dupeguru - build: Enable portable settings
* git 8c10eda - gunnerman1/dupeguru - build: Verify packaged Qt startup without visible window handles

## Other changes

In addition to those changes, this fork has a lot of packaging and
documentation cleanup. There are now github workflows to build
(debian, macos, windows) packages, and also standalone native scripts
to do the same.

The locale translations have been updated by transifex, and the
help files have been translated by Claude Sonnet 5.5.

The Ubuntu/debian changelog, created by
`dupeguru/hscommon/build.py/build_debian_changelog()`, needs an author
field, and that was left as `Virgil Dupras <hsoft@hardcoded.net>` in
honor of the original author, even though that email and domain name
no longer exist. A new maintainer field in `dupeguru/core/__init__.py`
is used to avoid hardcoding that in multiple places.


## Other forks

Other github dupeguru forks with recent activity that we might
think of merging here:

* dajiaohuang/dupeguru - all the changes here have been submitted as PRs to arsenetar.

* greeng3/dupeguru - 43 commits ahead, released as 5.1.1, adds Windows code signing and MacOS signing & notarization.

* haggyroth/dupeguru - 350 commits ahead, a very large update, released as 4.21.0

* Ikkoru/dupeguru - all the changes here have been submitted as PRs to arsenetar.

* kenny-ish/dupeguru - only one fix, seems to be an independent duplicate of PR1432

* manrajidevi91/dupeguru - A web/server based project, not a desktop app.

* marcmy/dupeguru - 56 commits ahead, needs to be considered.

* nedy13/dupeguru - 43 commits ahead, another one that was frustrated with arsenetar. Renamed to dupegurux and released as 4.4.3

* Tzahreddin/dupeguru - only one fix here, submitted as PR1420 to arsenetar. I don't understand the implications of this change well enough to merge it.

* usermo7amed/dupeguru-fedora - building for Fedora 44. We don't need this one, since dupeguru is now in the official Fedora repos.

* yyy-wqy/dupeguru - 2 commits ahead. Adds a language dialog so the language can be set on the first run. Adds .zip internal duplicate scanning.
