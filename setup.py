#!/usr/bin/env python

"""
setup.py file for SWIG
"""

from setuptools import setup, Extension

import importlib
import subprocess
import sys

def get_include_dirs():
    import pkgconfig
    import numpy

    if not pkgconfig.exists('eigen3'):
        raise Exception('Missing `eigen3` library. Please install it using the package manager of your operating system')

    np_include_dir = numpy.get_include()

    # We have to throw away the `-I` part of the `pkgconfig` output
    # because it is not part of the include directory.
    eigen3_include_dir = pkgconfig.cflags('eigen3')[2:]

    return [np_include_dir, eigen3_include_dir]

GKextCPy_module = Extension('_GKextCPy',
    sources = ['GKextCPy_wrap.cxx', 'GKextCPy.cpp'],
    swig_opts = ['-c++'],
    extra_compile_args = ['-std=c++11', '-O3'],
    include_dirs = get_include_dirs()
)

setup(name = 'GKextCPy',
    version = '0.4.1',
    author = 'Elisabetta Ghisu',
    description = """Graph Kernels: building the extension Python module. This is a wrapper package from C++ to Python.""",
    ext_modules = [GKextCPy_module],
    py_modules = ['GKextCPy'],
    setup_requires = ['pkgconfig'],
    install_requires = ['numpy'],
    license = 'ETH Zurich',
)
