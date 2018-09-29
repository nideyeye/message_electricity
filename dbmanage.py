from manage import app
from flask_pymongo import PyMongo
from spiders import Beijixin

app.config['MONGO_URI']='mongodb://localhost:27017/news'
mongo = PyMongo(app)

def save_to_db(dict):
    count = 0 
    for key in dict:
        title = key
        url = dict[key]
        if (mongo.db.news.find_one({'title':key}) is None) and count < 6:
            mongo.db.news.insert({'title':title, 'url':url}, check_keys=False)
        else:
            count += 1
            if count > 5:
                count = 0
                print('出现大量重复，结束入库')
                break
               
def read_from_db():
    