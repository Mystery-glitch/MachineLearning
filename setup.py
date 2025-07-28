# setup.py is responsible for creating the machine learning application as a package. It is special Python file that tells Python how to package your project, so others can install and use it easily.

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'MachineLearning',
    version='0.0.1',
    author='KC',
    author_email='kchansda27@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)