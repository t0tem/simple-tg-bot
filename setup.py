import os

from setuptools import find_packages, setup

NAME = "simple_tg_bot"
DESCRIPTION = ""
REQUIRES_PYTHON = ">=3.7.0"
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements(filename):
    with open(os.path.join(PROJECT_ROOT, filename), "r") as f:
        return f.read().splitlines()


setup(
    name=NAME,
    version='0.1.0',
    packages=find_packages(),
    python_requires=REQUIRES_PYTHON,
    url="https://github.com/t0tem/simple-tg-bot",
    description=DESCRIPTION,
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
)
