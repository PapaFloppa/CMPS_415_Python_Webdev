#Quade Witt
#Python Anywhere DB Part 1
#CMPS 415-Enterprise Systems
#02.12.2024

import mysql.connector
import cgi
import copy
from urllib.parse import parse_qs
global outp
outp=""
# Create instance of FieldStorage
form = cgi.FieldStorage()

## Define variables needed throughout the script
DBuser="Qwitt" ## DB username
DBpass="NoSaltNoPepper" ## DB password
DB="Qwitt$Bookstore"  ## DB database name
DBtable="Books"  ##DB Table
DBhost ="Qwitt.mysql.pythonanywhere-services.com"
select_all = "SELECT * FROM Books"

###########Functions###########


def search_query_maker(db_columns): #takes all null values out of the disctionary of search values
    ###Making the dictionary of user input easier to process###
    db_columns_copy = copy.copy(db_columns) #because a dictionary will not let you delete from it while iterating
    for i in db_columns:
        if(db_columns_copy[i] == ""): #iterate through the original and edit the copy
            del db_columns_copy[i]
    db_columns = db_columns_copy
    db_columns_copy = None #make the copy not exist anymore and update the original
    print(db_columns_copy)
    print(db_columns)

###Make the query string for searching###
    query = f"SELECT * FROM {DBtable} WHERE "
    for k in db_columns:
        frag_string = f"{k} LIKE '{db_columns[k]}%' AND "
        query += frag_string
    query =  query[:-5]
    query = f"{query};"
    return query

def insert_query_maker(db_columns):
###Make the query string for insertion###
    element_string = ""
    query = f"INSERT INTO {DBtable} VALUES ({(element_string)}"
    for k in db_columns:
        frag_string = f"'{db_columns[k]}', "
        query += frag_string
    query =  query[:-2]
    query = f"{query});"
    return query

####Checks the connection and fixes it if anything is wrong, I was having issues with it though####
"""def MySQL_Check(self):
    if (self.mysql.connector.MySQLConnection.is_connected() == 0): #check if a connection already exists
        outp += "<p>DB Connected...<br>"
        return mysql.connector.connect(host=DBhost, user=DBuser, passwd=DBpass, database=DB) #if no connection exists make one

    else: #if one does exist
        Current_Database = mysql.connector.MySQLConnection.database #check if the current DB is the one you want

        if (Current_Database != DB): #if it is not the one you want then connect to the one you want
            outp += "<p>DB Connected...<br>"
            return mysql.connector.MySQLConnection.cmd_change_user(host=DBhost, user=DBuser, passwd=DBpass, database=DB)
####################################
"""


#####Insert/Search selection HTML#####
Start ="""
    <style>
    #buttons{
    display: flex;
    justify-content: space-evenly;
    flex-direction: row;
}
h1 {
    display: flex;
    justify-content: center;
    flex-direction: row;
}
</style>
    <body>
        <h1>Would you like to search or insert?</h1>
        <div id="buttons">
            <form action="./search" method="GET">
            <button>search</button>
            </form>
            <form action="./insert" method="GET">
            <button>insert</button>
            </form>
        </div>
    </body>
</html>
"""

#####insert form HTML#####
insert = """
<html>
    <style>
#textboxes {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
    flex-direction: column;
    align-items: flex-end;
    align-content: center;
    flex-wrap: wrap;
}
#submitbutton{
    width: 103%;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}
#submitbutton:hover {
  color: darkgray;
}
h1{
    text-align:center;
    font-size: 3rem;
}

    </style>

    <body><h1>Input into the Bookstore Database!</h1>

        <form action="./inserted" method="GET">

            <div id= "textboxes">

                <p>Title: <input type="text" name="book_title" requied>

                <p>Author: <input type="text" name="book_author" required>

                <p>ISBN: <input type="text" name="book_isbn" required>

                <p>Publisher: <input type="text" name="book_publisher" required>

                <p>Year: <input type="text" name="book_year" required>
            </div>
            <div id = "submitbutton">
            <p ><input style="cursor: pointer;" type="submit" name="Submit">
            </div>
        </form>
    </body>
</html>"""


#####search form HTML#####
search = """
<html>
    <style>
#textboxes {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
    flex-direction: column;
    align-items: flex-end;
    align-content: center;
    flex-wrap: wrap;
}
#submitbutton{
    width: 103%;
    display: flex;
    flex-direction: row;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}
#submitbutton:hover {
  color: darkgray;
}
h1{
    text-align:center;
    font-size: 3rem;
}

    </style>

    <body><h1>Search the Bookstore Database!</h1>

        <form action="./searched" method="GET">

            <div id= "textboxes">

                <p>Title: <input type="text" name="book_title">

                <p>Author: <input type="text" name="book_author">

                <p>ISBN: <input type="text" name="book_isbn">

                <p>Publisher: <input type="text" name="book_publisher">

                <p>Year: <input type="text" name="book_year">
            </div>
            <div id = "submitbutton">
            <p ><input type="submit" name="Submit">
            </div>
        </form>
    </body>
</html>
"""

####The user does not want to do anything else####
done = """
<html>
<Style>
#text{
  position: absolute;
  left: 50%;
  top: 7%;
  transform: translate(-50%, -50%);
  animation: color-change 60s infinite;
    font-size: 4rem;


}
.video-container{
  width: 100vw;
  height: 100vh;
}

iframe {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100vw;
  height: 100vh;
  transform: translate(-50%, -50%);
}
@media (min-aspect-ratio: 16/9) {
  .video-container iframe {
    /* height = 100 * (9 / 16) = 56.25 */
    height: 56.25vw;
  }
}

@media (max-aspect-ratio: 16/9) {
  .video-container iframe {
    /* width = 100 / (9 / 16) = 177.777777 */
    width: 177.78vh;
  }
}
@keyframes color-change {
  0% { color: red;}
  5% { color: forestgreen; }
  10% { color: aqua; }
  15% { color: hotpink; }
  20% { color: darkorange; }
  25% { color: red; }
  30% { color: mediumblue; }
  35% { color: darkorchid; }
  40% { color: red; }
  45% { color: forestgreen; }
  50% { color: aqua; }
  55% { color: hotpink; }
  60% { color: darkorange; }
  65% { color: red; }
  70% { color: mediumblue; }
  75% { color: darkorchid; }
  80% { color: red;}
  85% { color: forestgreen; }
  90% { color: aqua; }
  95% { color: hotpink; }
  100% { color: darkorange; }
}

button{
  animation: color-change 60s infinite;
   position: absolute;
  left: 50%;
  top: 90%;
  transform: translate(-50%, -50%);
  animation: color-change 60s infinite;
      background: #4b5863;
     width: 20rem;
    height: 5rem;
    font-size: 2.5rem;
    cursor: pointer;
}
button:hover {
  background-color: darkgray;
}
</Style>
    <body>
        <div class= "video-container">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/OJrX3aNPsHM?si=c9yDjJFC9fVlKq3m?&autoplay=1&mute=1&playsinline=1" name="video" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>

        <div id="text">
            <h1>All Done!</h1>
        </div>

        <form action="./" id = "button" method="GET">
            <button>Back To Start</button>
        </form>
    </body>
</html>"""

### Router ###
def application(environ, start_response):
    global outp
    if environ.get('PATH_INFO') == '/': ##The 'search or insert?' page
        status = '200 OK'
        content = Start
    elif environ.get('PATH_INFO') == '/insert' : ##Hosts the insert form
        status = '200 OK'
        content = insert
    elif environ.get('PATH_INFO') == '/search' : ##Hosts the search form
        status = '200 OK'
        content = search

##########Search Data Handling###########
    elif environ.get('PATH_INFO') == '/searched' : #Handles the user data from search form
        myQueryString = parse_qs(environ.get('QUERY_STRING'))
        mydb = mysql.connector.connect(host=DBhost, user=DBuser, passwd=DBpass, database=DB)
        mycursor = mydb.cursor()
        db_columns = {"Title":  myQueryString.get('book_title', [''])[0], "Author": myQueryString.get('book_author', [''])[0], "ISBN": myQueryString.get('book_isbn', [''])[0], "Publisher": myQueryString.get('book_publisher', [''])[0], "Year": myQueryString.get('book_year', [''])[0]}

        query = search_query_maker(db_columns)
        outp = ""
        try:
            mycursor.execute(query) #Execute the query

            results = mycursor.fetchall() #Get the results in an array

            separator=', ' ## define how to separate printed items (see below)
            if not results:
                outp += "<div id= 'result'> Nothing Found </div>"

            else:
                for row in results: #Prints the results
                    outp += f"<div id= 'result'> {separator.join(map(str,row))} </div>" ## join all elements of "row" mapped as strings using "separator"
                    outp += "<br>\n"
        except mysql.connector.Error as err:
            outp = "<div id= 'result'>" + "Something went wrong: {}".format(err) + "</div>" #print the error if there is any
        else:
            outp += """
            <style>
            #buttons{
            display: flex;
            justify-content: space-evenly;
            flex-direction: row;
        }
        #results{
    display: flex;
    align-content: space-around;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-evenly;
    align-items: center;
}
        h1 {
            display: flex;
            justify-content: center;
            flex-direction: row;
        }
        </style>
            <body>
                <h1>Would you like to go again?</h1>
                <div id="buttons">
                    <form action="./" method="GET">
                    <button>Yes</button>
                    </form>
                    <form action="./done" method="GET">
                    <button>No</button>
                    </form>
                </div>
            </body>
        </html>
        """


        ## Finished; Close the DB
        mydb.close()
        status = '200 OK'
        content = outp
#########################################


##########Insert Data Handling###########
    elif environ.get('PATH_INFO') == '/inserted' :
        mydb = mysql.connector.connect(host=DBhost, user=DBuser, passwd=DBpass, database=DB)
        myQueryString = parse_qs(environ.get('QUERY_STRING'))
        mycursor = mydb.cursor()
        db_columns = {"Title":  myQueryString.get('book_title')[0], "Author": myQueryString.get('book_author')[0], "ISBN": myQueryString.get('book_isbn')[0], "Publisher": myQueryString.get('book_publisher')[0], "Year": myQueryString.get('book_year')[0]}
        query = insert_query_maker(db_columns)

        try: #try to execute and print the query
            mycursor.execute(query)
            mycursor.execute(select_all)
            results = mycursor.fetchall()

            ## Print all the results
            outp = "<div id= 'results'> Your new table is:" + "<br>\n </div>"
            separator=', '
            for row in results:
                outp += f"<div id= 'results'> {separator.join(map(str,row))} </div>"
                outp += "<br>\n"
        except mysql.connector.Error as err: #if there are any SQL errors print them
            outp += "<div id= 'result'>" + "Something went wrong: {}".format(err) + "</div>" #print the error if there is any
        else:
            ## Finished; Close the DB
            mydb.close()

            outp += """
            <style>
                #results{
    display: flex;
    align-content: space-around;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-evenly;
    align-items: center;
}
                #buttons{
                    display: flex;
                    justify-content: space-evenly;
                    flex-direction: row;
                }
                h1 {
                    display: flex;
                    justify-content: center;
                    flex-direction: row;
                }
            </style>
                <body>
                    <h1>Would you like to go again?</h1>
                    <div id="buttons">
                        <form action="./" method="GET">
                        <button>Yes</button>
                        </form>
                        <form action="./done" method="GET">
                        <button>No</button>
                        </form>
                    </div>
                </body>
            </html>
            """
        status = '200 OK'
        content = outp
################################################################
    elif environ.get('PATH_INFO') == '/done' : #If the user is done sends to a fun page
        status = '200 OK'
        content = done
    else: #if the page does not exist go here
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')