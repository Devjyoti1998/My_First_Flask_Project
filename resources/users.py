import sqlite3
from models.users import User
from flask import Flask,request
from flask_restful import Resource


class Register(Resource):
    def post(self):
        '''
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        data=request.get_json()
        x=cursor.execute("Select * from users")
        for row in x:
            if row[1]==data['username']:
                return {"Message":"Username already Exists!"},404

        query="INSERT INTO USERS VALUES(NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))
        '''

        data=request.get_json()
        user=User.get_by_username(data['username'])
        if user:
            return {"Message":"Username already Exists!"},404
        user=User(data['username'],data['password'])
        user.insert_to_db()

        return {"Message":"User Created Successfully"},200
