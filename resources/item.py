
import json
from models.item import ItemModel
from flask import Flask,request,jsonify
from flask_restful import Resource
from flask_jwt import jwt_required


class Item(Resource):

    @jwt_required()
    def get(self,name):
        '''for item in items:
            if item['item']==name:
                return item,200
        return {'item':None},404'''

        item=ItemModel.fetch(name)
        if item:
            #return json.loads(json.dumps(item.__dict__))
            return  item.json()#######
        return {"Message":"Item dont exist!"},404


    def post(self,name):
        item=ItemModel.fetch(name)
        if item:
            return {'Message':"'{}' already exists".format(name)},400

        data=request.get_json()
        '''items.append(
            {
                'item':name,
                'price':data['price']
            }
        )
        return items,201'''
        ItemModel(name,data['price'],data['store_id']).save_to_db()
        return {'item': "'{}' inserted".format(name)},200

    def delete(self,name):
        '''global items
        items=list(filter(lambda x: x['item']!=name,items))
        return {'item': "'{}' deleted".format(name)}'''
        item=ItemModel.fetch(name)
        if item is None:
            return {'Message':"'{}' Dosen't exists".format(name)},400
        item.delete_from_db()
        return {'item': "'{}' deleted".format(name)},200

    def put(self,name):
        '''global items
        item=next(filter(lambda x:x['item']==name,items),None)
        data=request.get_json()
        if item is None:

            item={
                'item':name,
                'price':data['price']
            }
            items.append(item)
        else:
            item['price']=data['price']
        return item'''

        item=ItemModel.fetch(name)
        data=request.get_json()

        if item:
            #ItemModel(name,data['price']).update_db()
            item.price=data['price']
        else:
            item=ItemModel(name,**data)
        item.save_to_db()
        #return json.loads(json.dumps(item.__dict__)),200
        return item.json()



class Items(Resource):
    def get(self):
        '''
        itemlist=[]
        item=ItemModel.fetch_all()
        for items in item:
            itemlist.append(items.json())

        return jsonify(itemlist)
        '''
        return {
        'items':
            list(map(lambda x: x.json(), ItemModel.query.all()))
        }


        '''
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
