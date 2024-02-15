#Quade Witt
#Python Anywhere DB Part 1 Func Test (A isolated enviornment for making sure my functions work for assignments)
#CMPS 415-Enterprise Systems
#02.12.2024

import copy
DBuser="Qwitt" ## This must be your own user ID
DBpass="NoSaltNoPepper" ## DB pass
DB="Qwitt$Bookstore"  ## This is the database
DBtable="Books"  ## This is the table that we created in the database
DBhost ="Qwitt.mysql.pythonanywhere-services.com" 
def search_query_makerinator():
    db_columns = {"Title": "","Author": "John","ISBN": "12345678","Publisher": "","Year": "1988"}
    db_columns_copy = copy.copy(db_columns)
    for i in db_columns:
        if(db_columns_copy[i] == ""):
            del db_columns_copy[i]
    db_columns = db_columns_copy
    db_columns_copy = None
    print(db_columns_copy)
    print(db_columns)

    element_string = "" 
    query = f"SELECT * FROM {DBtable} WHERE {element_string}"
    for k in db_columns:
        frag_string = f"({k} = '{db_columns[k]}') AND "
        query += frag_string
    query =  query[:-5]
    query = f"{query};"
    print(query)

def insert_query_maker():
    db_columns = {"Title": "Hello","Author": "John","ISBN": "12345678","Publisher": "Penguin Books","Year": "1988"}

    element_string = "" 
    query = f"INSERT INTO {DBtable} VALUES ({(element_string)}"
    for k in db_columns:
        frag_string = f"'{db_columns[k]}', "
        query += frag_string
    query =  query[:-2]
    query = f"{query});"
    print(query)

insert_query_maker()