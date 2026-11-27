# dupeGuru

dupeGuru is a cross-platform (Linux, OS X, Windows) GUI tool to find duplicate files in
a system. It is written mostly in Python 3 and uses [Qt6](https://www.qt.io/) for the UI.

## Why this fork?

See the [notes.md](notes.md) file for an explanation of the reasons for the
existance of this fork.

## Current status

Still looking for additional help especially with regards to:

* OSX maintenance: reproducing bugs
* Linux maintenance: reproducing bugs, maintaining PPA repository, Debian package.
* Documentation: keeping it up-to-date.

## Contents of this folder

This folder contains the source for dupeGuru. Its documentation is in `help`
Here's how this source tree is organized:

* dupeguru/core: the core Python logic code for dupeGuru
* dupeguru/qt: Python UI code for the Qt toolkit using PyQt
* dupeguru/hscommon: a collection of helpers
* help: Help document, written for Sphinx.
* help/translate: a script to generate Claude prompts and files for translation
* images: Images used by the different UI codebases.
* locale: .po files for localization.
* pkg/{debian,macos,windows}: Skeleton files and templates required to create packages
* pkg/build-scripts: manual setup and build scripts to create packages
* .github/workflows/{ubuntu,macos,windows}-release.yml - github workflows to create packages

## How to build dupeGuru from source

### Fedora

dupeguru is in the Fedora repositories, so a simple

> sudo dnf install dupeguru

will install the package. You can rebuild that package from source
by running:

> dnf download --source dupeguru<br>
> rpmbuild --rebuild dupeguru*.src.rpm

### Ubuntu, macOS, Windows

If you have forked the project on GitHub, then manually run the
appropriate release workflow and download the build artifacts when it
finishes.

If you have cloned the project to a local working directory, then run
the appropriate script in pkg/build-scripts. These scripts were generated
by Google Gemini from the corresponding GitHub workflows, and have
not been tested.
