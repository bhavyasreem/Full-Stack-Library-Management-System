import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .db import books


@csrf_exempt
def add_book(request):

    if request.method == "POST":

        data = json.loads(request.body)

        books.insert_one(data)

        return JsonResponse({"message":"Book Added"})


@csrf_exempt
def get_books(request):

    if request.method == "GET":

        data=[]

        for book in books.find({},{"_id":0}):

            data.append(book)

        return JsonResponse(data,safe=False)


@csrf_exempt
def update_book(request,book_id):

    if request.method=="PUT":

        data=json.loads(request.body)

        books.update_one(

            {"book_id":book_id},

            {"$set":data}

        )

        return JsonResponse({"message":"Book Updated"})


@csrf_exempt
def delete_book(request,book_id):

    if request.method=="DELETE":

        books.delete_one({"book_id":book_id})

        return JsonResponse({"message":"Book Deleted"})