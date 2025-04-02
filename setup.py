from setuptools import find_packages, setup
from typing import List


HYPHEN_E = '-e .'

def get_requirements(filepath):

    requirements = []

    with open(filepath) as obj:
        requirements = obj.readlines()
        requirements = [r.replace("\n", '') for r in requirements]

    if HYPHEN_E in requirements:
        requirements.remove(HYPHEN_E)

    return requirements

setup(

name="ml project",
version = "0.0.1",
author = "Yash Milak",
author_email = "yashmilak20@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")

)