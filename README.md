flask-app-structure
===================

A Flask app template with Login, and Logout, support.

Flask-App-Structure, an upgraded version from: https://github.com/codecool/flask-app-structure

Fixed many bugs, added creation of accounts.

Dependencies of the code:
-------------------------
- MySQL
- Flask-WTF
- Flask-Bcrypt
- Flask-Manager
- Flask-Login
- Flask-openid
- Flask-script
- Flask-assests

To Run:
-------
1:) Edit database.py db_engine to your mysql credentials
```
db_engine = create_engine('mysql://USERNAME:PASSWORD@localhost/DATABASE')
```
2:) Initialize a new database:
```
Python
from databse import init_db
init_db()
```
