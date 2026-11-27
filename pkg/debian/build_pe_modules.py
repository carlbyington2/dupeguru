import sys
import os
import os.path as op
import shutil
import importlib

from setuptools import setup, Extension

sys.path.insert(1, op.abspath("src"))

from dupeguru.hscommon.build import move_all

exts = [
    Extension("_block", [op.join("modules", "block.c"), op.join("modules", "common.c")]),
    Extension("_cache", [op.join("modules", "cache.c"), op.join("modules", "common.c")]),
    Extension("_block_qt", [op.join("modules", "block_qt.c")]),
]
setup(
    script_args=["build_ext", "--inplace"],
    ext_modules=exts,
)
move_all("_block_qt*", op.join("src", "dupeguru", "qt", "pe"))
move_all("_cache*", op.join("src", "dupeguru", "core", "pe"))
move_all("_block*", op.join("src", "dupeguru", "core", "pe"))
