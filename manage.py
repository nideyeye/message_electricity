from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import logging 
from flask_script import Manager, Server
from spiders.Beijixin import Beijixin
from spiders.StateGrid import StateGrid

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
manager.add_command("runserver", Server(use_debugger=True))

hot_spier = Beijixin()
order_spider = StateGrid()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hot')
def hot():
    return render_template('hot.html', result=hot_spier.run())
    
@app.route('/order')
def order():
    return render_template('order.html', result=order_spider.run())
if __name__ == '__main__':
    manager.run()
    #app.run(debug=True)