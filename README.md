# Django Authentication
this project uses a django framework in python where i created a rest api in the test for login, register and token verification functions using the simple jwt package


# First Preparations

For initial preparation to run this project applications. You need Python version 3, PostgresSQL, operating system Linux/Windows, (or using another OS).

## Basic Settings

Requirements to start the project must use **python version 3**,

you can download and install [here](https://www.python.org/download/releases/3.0/),

This project also uses the **Postgre database**, the settings can be found in the **SIM_PKL** folder then the **setting.py** 

you can install and configuration in this link [here](https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django)

It is recommended to **use env**, which can be found [here](https://www.petanikode.com/python-virtualenv/)

## Installing Pip
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or venv. Just make sure to upgrade pip.

# Windows
The Python installers for Windows include pip. You should be able to access pip using:
Open your CMD/Terminal
``bash
git clone https://github.com/mohamad1213/Django-auth-jwt.git
``
``bash
cd Django-auth-jwt
``
## Install Packages

To install all the required packages, run the command

```bash
pip3 install -p requirements.txt / pip3 install -r requirements.txt
```

## Migrate the Project

before you run this project you must to be migrate this data 

```bash
python3 manage.py migrate
```

## Run the Project

to run the project, you can use python / python3 

```bash
python3 manage.py runserver

```
## Deploy
this project has been deployed in Heroku (Cloud Application Platform) in this link [here](https://labsosv2.herokuapp.com/)

This project has 3 roles, namely college student, lecturers and staff, 
You can sign in with the account below :
