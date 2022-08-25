import yaml
from fifa_rating.exception import FifaException
import sys

def read_yaml_file(file_path:str)->dict:
    """
    Reads a yaml file content when path of the file is given in string and return content as a dictionary value
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise FifaException(e,sys) from e