from flask import Flask, render_template
from getData import dataObject

data = dataObject()

def getHead():
    head = data.listHeader
    return head
def getConfirmed():
    confirmed = data.listConfirmed
    confirmed = confirmed
    return confirmed
def getDeaths():
    deaths = data.listDeaths
    return deaths
def getRecovered():
    recovered = data.listRecovered
    return recovered


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', head=getHead(), confirmed=getConfirmed(), deaths=getDeaths(), recovered=getRecovered())

@app.route('/about.html')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
