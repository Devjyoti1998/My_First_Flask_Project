from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from resources.users import Register
from security import authenticate,identity
from resources.item import *
from resources.store import *
import sqlite3
from db import db

app=Flask(__name__)
api=Api(app)
app.secret_key='Devjyoti'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
@app.before_first_request
def create_tables():
        db.create_all()

jwr=JWT(app,authenticate,identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(Register,'/register')
'''@app.route('/check')
def check():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    select="select * from ITEMS"
    items=[]
    for row in cursor.execute(select):
        items.append(row)
    return jsonify(items)
    connection.commit()
    connection.close()
'''

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5002,debug=True)
