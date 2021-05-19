import sqlite3
from sqlite3 import Error
import flask
from flask import request, jsonify
from flask import Flask,request
app = flask.Flask(__name__)
app.config["DEBUG"] = True


#con=sqlite3.connect('project.db')
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
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def main():
    database = r"D:\restapi\project1.db"
 
    
    #buyer_deatils
    tblbuyer= """CREATE TABLE IF NOT EXISTS buyer_table (
                                    id integer PRIMARY KEY,
                                   
                                    fname text NOT NULL,
                                    mname text NOT NULL,
                                    lname text NOT NULL,
                                    email text NOT NULL,
                                    phno text NOT NULL
                                    
                                    
                                );"""
     
    
   
    

 
    # create a database connection
    conn = create_connection('project.db')
 
    # create tables
    if conn is not None:
       
 
        # create buyer table
        create_table(conn, tblbuyer)
        print("SUCCESSFULL")
    else:
        print("Error! cannot create the database connection.")




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sample work of REST API with local database</h1>
<p>A prototype API for distant user details.</p>'''


@app.route('/buyerdetails', methods=['GET'])
def api_all():
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM buyer_table;').fetchall()

    return jsonify(all_books)







@app.route('/addrec',methods=['GET','POST'])
def addrec():
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("INSERT INTO buyer_table(fname,mname,lname,email,phno)VALUES ('kavya','sri','kk','saikp@gmail.com','9870345617')")
    conn.commit()
    all_books = cur.execute('SELECT * FROM buyer_table;').fetchall()
    return jsonify(all_books)














