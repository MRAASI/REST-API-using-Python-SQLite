# REST-API-using-Python-SQLite 

# What is an API 
Application Programming interface is a part of a computer program to be used by another program 

# API Terminologies 
1.HTTP ('GET','POST') 
2.URL
3.JSON
4.REST

# what is REST 
REST is basically a set of rules followed to make an API


# What is REST API
RESTFul API is an advance concept of web development that implemented at server and used with HTTP method (GET/ POST/ PUT/ DELETE) to handle the data. The HTTP request methods and resources are identified using URIs and handled functionality accordingly. 

# What is Flask 
flask is a microframework in Python. 


# Running the Application
In the command line, navigate to your api folder.Once you’re in your project directory, run the Flask application with the command:
set FLASK_APP= dsetup.py
flask run 

**The below image shows how to run the application
![image](https://user-images.githubusercontent.com/46440771/118770526-136aa880-b89f-11eb-89e3-a6f597f99426.png)



You should see output similar to this:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 

# Create database Connection
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect('project1.db')
        return conn
    except Error as e:
        print(e)
 
    return conn

and created a table called buyer_table 


# A route to return all of the available entries in our catalog.

@app.route('/buyerdetails', methods=['GET'])

for running: http://127.0.0.1:5000/buyerdetails



# To insert new entry into database
@app.route('/addrec',methods=['GET','POST'])

http://127.0.0.1:5000/addrec




