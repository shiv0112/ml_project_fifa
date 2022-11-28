import logging
import os
from pathlib import Path

package_name = "ml_project_fifa"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

list_of_files = [
    "data/.gitkeep",
    "templates/.gitkeep",
    "static/.gitkeep",
    "screenshots/.gitkeep",
    "research/EDA.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "app.py",
    "Procfile",
    "runtime.txt",
    "setup.sh",
    "template.py",
]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating directory: {filedir}")
    
    else:
        logging.info(f"{filename} already exists")