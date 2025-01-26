Kaggle Hub Client Library

Installation
Install the kagglehub package with pip:

pip install kagglehub

Usage
Authenticate
Authenticating is only needed to access public resources requiring user consent or private resources.

First, you will need a Kaggle account. You can sign up here.

After login, you can download your Kaggle API credentials at https://www.kaggle.com/settings by clicking on the "Create New Token" button under the "API" section.

You have 3 different options to authenticate.

Option 1: Calling kagglehub.login()
This will prompt you to enter your username and token:

import kagglehub

kagglehub.login()
Option 2: Read credentials from environment variables
You can also choose to export your Kaggle username and token to the environment:

export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
Option 3: Read credentials from kaggle.json
Store your kaggle.json credentials file at ~/.kaggle/kaggle.json.

Alternatively, you can set the KAGGLE_CONFIG_DIR environment variable to change this location to $KAGGLE_CONFIG_DIR/kaggle.json.

Note for Windows users: The default directory is %HOMEPATH%/kaggle.json.


Other dependencies needed

PANDAS
Installing from PyPI
pandas can be installed via pip from PyPI.

pip install pandas

SCIKIT-LEARN
Installing from PyPI

pip install scikit-learn

OPENPYXL
Installing from PyPI

pip install openpyxl
