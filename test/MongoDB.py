import sys
from flask_pymongo import PyMongo
sys.path.append("..")
from manager import app
from Beijixin import SpiderBeijixin
app.config['MONGO_URI']='mongodb://localhost:27017/flask'

mongo = PyMongo(app)
spider = SpiderBeijixin()
result = spider.run()
count = 0 
for key in result:
    title = key
    url = result[key]
    if (mongo.db.news.find_one({'title':key}) is None) and count < 6:
        mongo.db.news.insert({'title':title, 'url':url}, check_keys=False)
    else:
        count += 1
        if count > 5:
            count = 0
            print('出现大量重复，结束入库')
            break

if __name__ == '__main__':
    app.run(debug=True)
    