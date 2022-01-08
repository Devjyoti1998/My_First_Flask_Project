from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store=StoreModel.fetch(name)
        if store:
            return store.json()
        return {'Message':'Store does not exist'},404

    def post(self,name):
        store=StoreModel.fetch(name)
        if store:
            return {'Message':'Store \'{}\' exists'.format(name)},400
        store=StoreModel(name)
        store.save_to_db()

        return store.json()

    def delete(self,name):
        store=StoreModel.fetch(name)
        if store:
            store.delete_from_db()
        return {'Message':'Store Deleted'}

class StoreList(Resource):
    def get(self):
        return {
        'stores':[store.json() for store in StoreModel.query.all()]
        }
