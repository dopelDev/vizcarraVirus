from flask import Flask, render_template
from getData import dataObject

data = dataObject()


def getHead():
    head = data.listHeader
    return head


def getConfirmed():
    confirmed = data.listConfirmed
    return confirmed


def getDeaths():
    deaths = data.listDeaths
    return deaths


def getRecovered():
    recovered = data.listRecovered
    return recovered


def getLastWeek():
    tempList = data.listDeaths
    lastWeek = []
    for i in range(-7, 0, 1):
        death = int(tempList[i]) - int(tempList[i-1])
        lastWeek.append(int(death))
    return lastWeek


def getLastWeekDays():
    tempList = data.listHeader
    lastWeekDays = []
    for i in range(-7, 0, 1):
        lastWeekDays.append(str(tempList[i]))
    return lastWeekDays


def getBeforeLastWeek():
    tempList = data.listDeaths
    beforeLastWeek = []
    for i in range(-14, -7, 1):
        death = int(tempList[i]) - int(tempList[i-1])
        beforeLastWeek.append(death)

    return beforeLastWeek


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', head=getHead(),
                           confirmed=getConfirmed(),
                           deaths=getDeaths(), recovered=getRecovered(),
                           lastWeek=getLastWeek(),
                           lastWeekDays=getLastWeekDays(),
                           beforeLastWeek=getBeforeLastWeek())


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
