#!/usr/bin/env python
"""Setup file and install script SciLife python scripts.
"""
from setuptools import setup, find_packages
import sys
import os
import glob
import subprocess

# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    version_git = subprocess.check_output(["git", "describe"]).rstrip()
except:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

version_msg = "# Do not edit this file, versioning is governed by git tags"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__=" + version_git)

setup(name = "scilifelab",
    version = "{ver}".format(ver=version_git),
    author = "Science for Life Laboratory",
    author_email = "genomics_support@scilifelab.se",
    description = "Useful scripts for use at SciLifeLab",
    license = "MIT",
    scripts = glob.glob('scripts/*.py') +
                glob.glob('scripts/analysisDB/*.py') +
                glob.glob('scripts/RNA_analysis/*.py') +
                glob.glob('scripts/bcbb_helpers/*.py') +
                glob.glob('scilifelab/lims_utils/*.py') +
                ['scripts/pm', 'scripts/stdin_to_redis'],
    install_requires = [
        "bcbio-nextgen >= 0.2",
        "drmaa >= 0.5",
        "sphinx >= 1.1.3",
        "couchdb >= 0.8",
        "reportlab >= 2.5",
        "cement >= 2.0.2",
        "mock",
        "PIL",
        "pyPdf",
        "logbook >= 0.4",
        "biopython",
        "rst2pdf",
        "fabric",
        "beautifulsoup4",
        "texttable",
        ],
      test_suite = 'nose.collector',
      packages=find_packages(exclude=['tests']),
      package_data = {'scilifelab':[
          'data/grf/*',
          'data/templates/*.mako',
          'data/templates/halo/*.mako',
          'data/templates/rst/*',
          ]}
      )
