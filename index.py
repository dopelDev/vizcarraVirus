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


def getLastWeek():
    lastAll = data.listDeaths
    lastWeek = []
    for i in range(-7, 0, 1):
        death = int(lastAll[i]) - int(lastAll[i-1])
        lastWeek.append(int(death))
    return lastWeek


def getLastWeekDays():
    listD = data.listHeader
    lastWeekDays = []
    for i in range(-7, 0, 1):
        lastWeekDays.append(str(listD[i]))
    return lastWeekDays


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', head=getHead(),
                           confirmed=getConfirmed(),
                           deaths=getDeaths(), recovered=getRecovered(),
                           lastWeek=getLastWeek(),
                           lastWeekDays=getLastWeekDays())


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
