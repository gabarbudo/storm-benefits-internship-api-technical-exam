# storm-benefits-internship-api-technical-exam
by Gab Barbudo

## Setup Requirements
* Python Flask
* MySQL Database Server
* SQLAlchemy
* Marshmallow
* PyMySQL (to support newer versions of Python)

You can install SQLAlchemy, Marshmallow, and PyMySQL using pip, by running the following commands in the terminal:
```
$ pip install flask_sqlalchemy
$ pip install flask_marshmallow
$ pip install marshmallow-sqlalchemy
$ pip install PyMySQL
```
## Instructions
### 1. Generate MySQL database


* Open terminal in the folder of the Flask application.
* Start up your MySQL server.

  ```
  $ mysql -u root -p
  ```

  Just press `ENTER` on your keyboard when prompted to enter a password.
  
* Create a database and name it `companydb`.

  ```
  > CREATE DATABASE companydb;
  ```
  
  Then import the `company` table to the  newly created database.
  
  ```
  > USE companydb;
  > source company.sql;
  ```

* Exit MySQL server.
  
  ```
  > exit
  ```
  
### 2. Run Flask application
* While still in the Flask application folder, run the following command from your terminal.

  ```
  $ python crud.py
  ```
* The flask application is now ready to use. Access it through your browser by typing in `http://localhost:5000/company/`. 
* You can use [Postman](https://www.getpostman.com/postman) for testing the application's CRUD functions.
