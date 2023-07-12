from setuptools import setup, find_packages

setup(
    name='dmi-llm-classifiers',
    version='0.1.0',
    packages=find_packages(include=['dmi-llm-classifiers', 'dmi-llm-classifiers/.*'])
)
