from setuptools import find_packages, setup
from typing import List

E_DOT = "-e ."
def get_requirements(file_path:str):
    """
      This function will return list of requirement packages
    """
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [ req.replace("\n", "") for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# if __name__ == "__main__":
#     get_requirements("requirements.txt")