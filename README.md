# User-management-in-Flask
# Project Information
This is a basic authentication system with Flask.\
Backend - Python Flask\
Frontend - Bootstrap, HTML

# SETUP
* In your working directory clone the repository:
```
git clone https://github.com/raykipkorir/User-management-in-Flask.git
```
* Navigate into the repository 
```
cd User-management-in-Flask
```
* Create a virtual environment then activate to install all dependencies\
  For windows
```
python -m venv <envname>
.\<envname>\Scripts\activate
```
 For Unix based system
```
python -m venv <envname>
source <envname>/bin/activate
```
* Lets install the dependencies
```
pip install -r requirements.txt
```
* Create database tables inside the python interactive shell
```
from authentication import db
db.create_all()
```
* Run the server
```
python run.py
```
