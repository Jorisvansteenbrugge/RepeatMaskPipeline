from setuptools import setup, find_packages
from os import path

setup(
        name = "rnaseqpipeline",
        version = "0.1",
        description = 'WUR nematology rnaseq pipeline',
        packages = ['rnaseqpipeline'],
        scripts = ['scripts/rnaseqpipeline']
        )
