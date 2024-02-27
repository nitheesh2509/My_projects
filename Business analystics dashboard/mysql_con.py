import mysql.connector 
import streamlit as st

#Connection

conn = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "",
    db = "my_streamlit_app"
)

c = conn.cursor()

# Fetch data

def view_all_data():
    c.execute('select * from customers order by id asc')
    data = c.fetchall()
    return data