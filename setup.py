from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    it will give list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name='Student-performance-prediction',
    version='0.0.1',
    author='Atharva',
    author_email='anpatil.1223@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)