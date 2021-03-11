# Django Blog
Django Blog is a simple yet more than a basic blog website built using FLask.
Follow the Steps to use flask blog

****
## Local installation guide:
**Clone the repository**
```bash
 git clone https://github.com/NayanMogra/Django.git
```

**Install virtual enviornment**
#### For Windows
```bash
python -m pip install --user enviroment
python -m venv env
python -m enviroment --help
```
#### For Linux
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
python -m enviroment --help
```

**Activate the  virtual enviornment**
####For Windows
```bash
cd flaskblog\enviornment
Scripts\activate
```
####For Linux 
```bash
source env/bin/activate
```

****
## Installing dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies in blog directory

### To install all dependencies at once use 
#### For both Windows and Linux
```bash
pip install -r requirement
```

****
## Set Username and password 
**Set Username and password for sending link to change password**
```bash
 1. Go in search and write enviroment varible and click on edit the system envrioment varible
 2. Now got to Enviroment varible option
 3. now set two system varible:-
   a. EMAIL_USER as varible name and <a valid gmail id> as varible value
   b. EMAIL_PASSWORD as varible name and <a valid gmail password> as varible value
 ```
 ****
 
## Run the code at your local envn
**Run it as**
```bash
 python manage.py runserver
 ```
>Open your browser and the site can be found running at http://127.0.0.1:8000/



