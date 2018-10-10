from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import logging 
from flask_script import Manager
from spiders import Beijixin, StateGrid

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hot')
def hot():
    result_list = spider.run()
    return render_template('hot.html', result_list=result_list)
    

if __name__ == '__main__':
    manager.run()
    #app.run(debug=True)