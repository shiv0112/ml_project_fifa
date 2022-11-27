echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ./env
echo [$(date)]: "Installing the dev env"
pip install -r requirements.txt
echo [$(date)]: "Installing predictions"
source activate ./env
echo [$(date)]: "END"