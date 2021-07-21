from liter import __version__
from setuptools import find_packages, setup

# load readme
with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="torchliter",
    version=__version__,
    author="Chenchao Zhao",
    author_email="chenchao.zhao@gmail.com",
    description="A lightweight training tool for pytorch projects.",
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["torch", "numpy", "dataclasses"],
    license="MIT",
)
