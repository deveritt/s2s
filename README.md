# s2s

## Setup

* Clone the repo: `darren@darren-UbuntuMacBook:~/data/projects$ git clone git@github.com:deveritt/s2s.git`
* (not going to create a pyenv).
* Create the Django project:
    * Install/upgrade Django: `pip install django`
    * `darren@darren-UbuntuMacBook:~/data/projects$ cd s2s`
* Get the database going:
```
darren@darren-UbuntuMacBook:~/data/projects$ sudo apt install mysql-server
darren@darren-UbuntuMacBook:~/data/projects/s2s$ sudo apt install python3-dev`
darren@darren-UbuntuMacBook:~/data/projects/s2s$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
darren@darren-UbuntuMacBook:~/data/projects/s2s$ pip install mysqlclient
darren@darren-UbuntuMacBook:~/data/projects/s2s$ sudo mysql -u root

mysql> CREATE DATABASE s2s;
CREATE USER 's2sta'@'%' IDENTIFIED WITH mysql_native_password BY 'ats2s';
mysql> GRANT ALL ON s2s.* TO 's2sta'@'%';
mysql> FLUSH PRIVILEGES;
CTRL+D
```

## API Test Results
```
darren@darren-UbuntuMacBook:~/data/projects/s2s$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.056s

OK
Destroying test database for alias 'default'...
```

## Notes to Assessor

* Creating using Django because it's more familiar to me and quicker, also, I have a Python IDE running and not a php one for review discussion.


Time to open pycham, create the project and edit the settings file, then we'll return to setting up the db.



Back to add the database to settings.py.
darren@darren-UbuntuMacBook:~/data/projects/s2s$ python3 manage.py migrate

=9.30am - 10.30am
Django project runs in browser (Off to another appointment.)

= 10.30am
Create requirements.txt
darren@darren-UbuntuMacBook:~/data/projects/s2s$ pip install -r requirements.txt 
Create model. Add name as required and make attributes a JSON field.
darren@darren-UbuntuMacBook:~/data/projects/s2s$ python3 manage.py startapp products
darren@darren-UbuntuMacBook:~/data/projects/s2s$ python3 manage.py makemigrations
darren@darren-UbuntuMacBook:~/data/projects/s2s$ python3 manage.py migrate

+ Expansion: add mapping from client to local database for fields.

= 11am

Written API interface (Serializer and API, need to test it.

= 11.30 - 12 away

mysql> GRANT ALL PRIVILEGES ON test_s2s.* TO 's2sta'@'%';