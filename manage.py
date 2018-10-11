from flask import Flask, render_template, request, redirect, url_for
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
def hot_302():
    return redirect(url_for('hot', page=1))
@app.route('/hot/<page>')
def hot(page):
    page = int(page)
    if page == None:
        page = 1
    return render_template('hot.html', result=hot_spier.run(page), before_page = str(page-1) if page >1 else '1', next_page = str(page+1))
    
    
@app.route('/order')
def order_302():
    return redirect(url_for('order', page=1))
@app.route('/order/<page>')
def order(page):
    page = int(page)
    if page == None:
        page = 1
    return render_template('order.html', result=order_spider.run(page), before_page = str(page-1) if page >1 else '1', next_page = str(page+1))
if __name__ == '__main__':
    manager.run()
    #app.run(debug=True)