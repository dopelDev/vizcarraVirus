from csv import reader


class dataObject():

    def __init__(self):
        self.listHeader = []
        self.listConfirmed = []
        self.listDeaths = []
        self.listRecovered = []
        self.country = 'Peru'
        self.path = '/home/dopel/projects/vizcarraVirus/static/data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

        self.getHead('time_series_covid19_confirmed_global.csv')
        self.listConfirmed = self.getData(
            'time_series_covid19_confirmed_global.csv')
        self.listDeaths = self.getData('time_series_covid19_deaths_global.csv')
        self.listRecovered = self.getData(
            'time_series_covid19_recovered_global.csv')

    def getHead(self, fileName):
        dataFile = open(self.path + fileName)
        dataReader = reader(dataFile)
        dataList = list(dataReader)
        dataFile.close()
        header = list(dataList[0])
        listHeader = []
        for item in range(46, len(header)):
            self.listHeader.append(header[item])
        return listHeader

    def getData(self, fileName):
        dataFile = open(self.path + fileName)
        dataReader = reader(dataFile)
        dataList = list(dataReader)
        dataFile.close()

        for row in dataList:
            rowList = list(row)
            for Country in row:
                if row[1] == self.country:
                    rowCountry = list(row)
                    break

        countryData = []

        for item in range(46, len(rowCountry)):
            countryData.append(rowCountry[item])

        return countryData
