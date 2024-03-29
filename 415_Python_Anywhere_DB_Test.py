####some code taken from the code made by my teacher Dr.Cris Koutsougeras####
####i.e not my work####
####Code to access MYSQL database from a browser####
####This Returns everything in a SQL Database to a web page####

import mysql.connector
outp=""


def dbDemo():
    global outp
    outp=""
    ## Define variables needed throughout the script
    DBuser="ckselu"
    DBpass="cksclass"
    DB="ckselu$Bookstore"
    DBtable="Books"
    DBhost ="ckselu.mysql.pythonanywhere-services.com"


    ## Now open the DB
    mydb = mysql.connector.connect(host=DBhost, user=DBuser, passwd=DBpass, database=DB)
    outp += "<p>DB Connected...<br>"


    ##-- and create database object
    mycursor = mydb.cursor()


    ## Database is now ready for use


    ## Define a query for the DB, possibly using form inputs from a user
    query = "SELECT * FROM " + "  " + DBtable


    outp += "<p>Query is " + query + "<p>\n"


    ## Execute the query
    mycursor.execute(query)


    ####### Handle Results:
    results = mycursor.fetchall()      ## Now all items retrieved from DB are in "results" 
    ## Print all the results
    for row in results:
        outp += ', '.join(map(str,row))  ## join all elements of "row" mapped as strings separated by ", "
        outp += "<br>\n" ## Insert an HTML line break after each element


    mydb.close()     ## Finished; Close the DB
    outp += "<p>I am done<p>"




### The following is the router ###


def application(environ, start_response):
    global outp
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = "HELLO_WORLD"
    elif environ.get('PATH_INFO') == '/runDB' :
        dbDemo()
        status = '200 OK'
        content = outp
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'


    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')
