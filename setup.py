from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Arunav',
    author_email='prakasharunav12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
