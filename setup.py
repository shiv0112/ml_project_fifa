from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="fifa-rating"
VERSION="0.0.1"
AUTHOR="Shivansh Srivastava"
DESCRIPTION="This is a full FDSD project to predict fifa overall rating"
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return a list which contains name of 
    libraries mentioned in our requirements.txt file.
    """
    with open('requirements.txt') as f:
        packages = []
        for line in f:
            line = line.strip()
            # let's also ignore empty lines and comments and ignore -e .
            if not line or line.startswith('#') or '-e .' in line:
                continue
            packages.append(line)
    return packages

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),#PACKAGES=["fifa_rating"]
    install_requires=get_requirements_list()
)

