import mysql.connector 
import streamlit as st

# Connection to mysql_server

db= mysql.connector.connect(
    host='localhost',
    port= '3306',
    password = "",
    user= 'root',
    database = "crud"
)

c = db.cursor()
print('Connection Established!')

# Create Streamlit app

def main():
    st.title("CRUD operation with MySQL")
    # Display Options for CRUD operations
    st.sidebar.subheader("Display Options")
    options = st.sidebar.selectbox("Select an option", ("Create", "Read", "Update", "Delete"))

    # Perform Selected CRUD Operations
    if options == "Create":
        st.subheader("Create a record")
        name = st.text_input("Enter Name:")
        email = st.text_input("Enter Email:")
        age = st.text_input("Enter Age:")
        city = st.text_input("Enter City:")
        phone_no = st.text_input("Enter Phone:")
        if st.button("Create"):
            sql = "insert into users(name, email, age, city, phone_no) values(%s,%s,%s,%s,%s)"
            val = (name, email, age, city, phone_no)
            c.execute(sql, val)
            db.commit()
            st.write("Record inserted successfully")

    elif options == "Read":
        st.subheader("Read the record")
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        for row in rows:
            st.write(row)

    elif options == "Update":
        st.subheader("Update the record")
        id = st.number_input('Enter ID')
        name = st.text_input("Enter New Name:")
        email = st.text_input("Enter New Email:")
        age = st.text_input("Enter New Age:")
        city = st.text_input("Enter New City:")
        phone_no = st.text_input("Enter New Phone:")
        if st.button("Update"):
            sql = "update users set name=%s, email=%s, age=%s, city=%s, phone_no=%s where id=%s"
            val = (name, email, age, city, phone_no, id)
            c.execute(sql, val)
            db.commit()
            st.write("Record updated successfully")

    elif options == "Delete":
        st.subheader("Delete the record")
        id = st.number_input('Enter ID')
        if st.button("Delete"):
            sql = "delete from users where id=%s"
            val = (id,)
            c.execute(sql, val)
            db.commit()
            st.write("Record deleted successfully")
if __name__ == "__main__":
    main()