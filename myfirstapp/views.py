from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['Interviews_record']
collection=db['Record']

def add_data(request):
    collection.insert_many([{'name':'jayendra'},{'age':4},{'address':'kota'}])
    return HttpResponse("data inserted successfully")

def update_data(request):
    prev={"name":"jayendra"}
    nextt={'$set':{"name":"rahul",'id':89}}
    collection.update_many(prev,nextt)
    return HttpResponse("data updated successfully")


def delete_data(request):
   
    rec={"name":"rahul"}
    collection.delete_one(rec)
    return HttpResponse("data deleted successfully")


def find_data(request):
    one=collection.find()
    print(one)
    return render(request,"index.html",context={"data_is":one})
