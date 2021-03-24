from setuptools import setup, find_packages
from os import path

setup(
        name             = "RepeatMaskPipeline",
        version          = "0.18",
        author           = "Joris van Steenbrugge",
        author_email     = "joris.vansteenbrugge@wur.nl",
        packages         = find_packages(),
        description      = 'WUR nematology Repeatmask Pipeline',
        scripts          = ['scripts/Repeatmask_pipeline', 'scripts/fastaSplitter'],
        install_requires = ['joblib', 'biopython'],
        )
