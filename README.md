# Build-a-team-for-Startup

> Software Project course in Innopolis University Spring semester 2019  
Main goal is to create a web application for searching job and workers for projects

***

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For running our project you need to install Django framework by entering following command in terminal

```
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Firstly, run the server

```
python manage.py runserver
```

Then enter

```
http://127.0.0.1:8000/
```

To recieve letters for reset password you need to run a server on new terminal
```
python -m smtpd -n -c DebuggingServer localhost:1025
```
Then after writing your email to corresponding field letter will come to this server


## Source Code Analyzing

Firstly, run [SonarQube](https://www.sonarqube.org/downloads/) from its bin directory

For Linux/MacOS:
```bash
./sonar.sh start
```

For Windows:
```bash
./StartSonar.bat
```

Then, run [SonarQube Scanner](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner) in the root directory of the project

For Linux/MacOS:
```bash
<path to sonar-scanner bin>/sonar-scanner
```

For Windows:
```bash
<path to sonar-scanner bin>/sonar-scanner.bat
```

After that, open this link in browser:

http://localhost:9000/dashboard?id=Build-a-team-for-Startup

## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [SQLite](https://www.sqlite.org/docs.html) - Database Management System
* [Material Kit](https://github.com/creativetimofficial/material-kit) - Bootstrap UI Kit inspired by material design

## Authors

* **Amir Subaev** - *Front-end* - [Apostrov](https://github.com/Apostrov)
* **Anastasia Minakova** - *Front-end* - [Stalem9](https://github.com/stalem9)
* **Ali Akhmetbek** - *Back-end* - [Akhmetbekali](https://github.com/Akhmetbekali)
* **Kamil Alimov** - *Back-end* - [kamel2700](https://github.com/kamel2700)
* **Ilya Khabirov** - *Back-end* - [Spirys](https://github.com/Spirys)

See also the list of [contributors](https://github.com/stalem9/Build-a-team-for-Startup/graphs/contributors) who participated in this project.


## Acknowledgments

### Our project is not that perfect right now, as a result we have some minor bugs:

#### First sprint

* If you enter the main page after successfull login you need to enter the system again
* For now, you can not edit description, speciality and photo
* Moreover, in edit profile page there is password warning, because we do not have an ability to change password (fixed)
* To see the front-end of catalog page you need to run http://localhost:8000/account/catalog  

#### Second sprint

* For editing profile we need to fill in all the fields
* If a user logs in under a non-existing account, nothing happens
* Bug with catalog card that they are not in the correct order

#### Third sprint

* Only prototypes of comments and work history sections in user profile are ready now
#### All the bugs will be fixed for the next sprint
