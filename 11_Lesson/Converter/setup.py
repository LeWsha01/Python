from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Converter',
    version='0.5',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)