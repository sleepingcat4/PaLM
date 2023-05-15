from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

with open("README.md", "r") as f:
    long_description = f.read()

def load_requirements(path):
    with open(path, "r") as f:
        return [line.strip() for line in f]

setup(
    name="PaLM",
    version="1.0.0",
    author="conceptofmind, sleepingcat4",
    description="PaLM: a tiny implementation of Google's PaLM model based on conceptofmind's implementation & Google",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sleepingcat4/PaLM",
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    distclass=BinaryDistribution
)
