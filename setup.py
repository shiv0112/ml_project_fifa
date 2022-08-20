from setuptools import setup  
from typing import List

PROJECT_NAME="fifa-rating"
VERSION="1.0.0"
AUTHOR="Shivansh Srivastava"
DESCRIPTION="THis is a full FDSD project to predict fifa overall rating"
PACKAGES=["fifa-rating"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return a list which contains name of 
    libraries mentioned in our requirements.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())