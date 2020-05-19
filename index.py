from flask import Flask, render_template
from getData import dataObject

data = dataObject()


def getHead():
    head = data.listHeader
    return head


def getConfirmed():
    confirmed = []
    for i in range(1, len(data.listConfirmed)):
        tmp = int(data.listConfirmed[i]) - int(data.listConfirmed[i-1])
        confirmed.append(tmp)
    return confirmed


def getDeaths():
    deaths = []
    for i in range(1, len(data.listDeaths)):
        tmp = int(data.listDeaths[i]) - int(data.listDeaths[i-1])
        deaths.append(tmp)
    return deaths


def getRecovered():
    recovered = []
    for i in range(1, len(data.listRecovered)):
        tmp = int(data.listRecovered[i]) - int(data.listRecovered[i-1])
        recovered.append(tmp)
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


def getDoughnut():
    doughnut = []
    doughnut.append(data.listConfirmed[-1])
    doughnut.append(data.listRecovered[-1])
    doughnut.append(data.listDeaths[-1])

    return doughnut


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', head=getHead(),
                           confirmed=getConfirmed(),
                           deaths=getDeaths(), recovered=getRecovered(),
                           lastWeek=getLastWeek(),
                           lastWeekDays=getLastWeekDays(),
                           beforeLastWeek=getBeforeLastWeek(),
                           doughnut=getDoughnut())


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
