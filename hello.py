from flask import Flask, render_template, request, redirect, send_from_directory
from twitter_search import produce_map
app = Flask(__name__,static_url_path="",static_folder="tmp")

#@ is a decorator; the next part is executed --> app.route('/' hello_world)

#render index page
@app.route('/') #'/' is the index of a page; tells Flask to run this function
def hello(): #for an incoming requests (GET)
    return render_template('index.html')

#Render search query page unless user inputted invalid query
@app.route('/login',methods=['POST','GET'])
def login(): #handles the login
    if request.method == 'POST':
        term = request.form['Search term']
        #If user inputted empty search term, render error page
        if term == '':
            return render_template('error.html')
        produce_map(term)
        return render_template('login.html',term=term)
    else:
        return render_template('error.html')

#Render index page when 'back' button from search-query page is pressed
@app.route('/index',methods=['POST','GET'])
def index(): #once you leave the first page, this is the only way to get back
    if request.method == 'POST':
        return render_template('index.html')

#Send file to search-query (login.html) to be displayed
@app.route('/<filename>')
def send_pic(filename):
    return send_from_directory('',filename=filename)

if __name__ == '__main__':
    #app.debug = True
    app.run(
        host = "127.0.0.1",
        port = int("8000")
        )
