from index import app
from flask_frozen import Freezer

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = '/home/dopel/projects/vizcarraVirus/docs'

if __name__ == '__main__':
    freezer.freeze()
