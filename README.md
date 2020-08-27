# s2s

## Setup

In the intended app user directory on Ubuntu 20 LTS (with default python 3.8).
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
mysql> GRANT ALL PRIVILEGES ON test_s2s.* TO 's2sta'@'%';
```
* `pip install -r requirements.txt`
* `python3 manage.py migrate`
* `python3 runserver [ip:port]`

## (API) Test Results
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
* I expect to need be detailing the mechanics of how Django API works (serialiation and such)
* I suggest that this system, although not used in your (php) core, could be used for the client interfaces that you intend setting up.

### Time spent:

* Setup (including db): half hour.
* Model and API interface with testing: 2 hours.
* UI (Indjango because vue.js would play nicely): 45 minutes.

