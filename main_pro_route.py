# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
import json
import datetime
app = Flask(__name__)
#实例化Flask
Bootstrap(app)
#启用bootstrap装饰模板
nav = Nav()
# 定义导航栏
nav.register_element('top',Navbar(u'设备管理信息系统',
View(u'主页','home'),
View(u'关于','about'),
View(u'设备信息','device')
))
# 注册到app上
nav.init_app(app)

@app.route('/')
def home():
    return render_template('mybase.html')
@app.route('/device')
def device():
    return render_template("device-asset-table.html"),
@app.route('/about')
def about():
    return 'about'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

if __name__ == '__main__':
    app.run(debug=True)