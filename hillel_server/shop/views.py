# Доробити проект, що ми почали робити на уроці:
# Аналогічно таблиці Dog, створити таблицю Cat. ТАкож потрібно зробити endpoint в залежності від методу якого буде
# відбуватися створення, отримання або видалення кота в нашій БД.

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from shop.models import Dog, Cat


def hello_page(request):

    return HttpResponse("Hello world")


def dogs(request):

    if request.method == "POST":  # add a new dog

        data = json.loads(request.body)

        our_dog = Dog(
            name=data["name"],
            breed=data["breed"],
            weight=data["weight"]
        )
        our_dog.save()

    elif request.method == "GET":  # get all dogs
        dogs_json = []
        dogs = Dog.objects.all()

        for d in dogs:
            dogs_json.append(
                {
                    'id': d.id,
                    "name": d.name,
                    "breed": d.breed,
                    "weight": d.weight
                }
            )

        return JsonResponse(
            dogs_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete all dogs
        dogs = Dog.objects.all()
        dogs.delete()

    return HttpResponse("DOG")


def dog(request, id):

    if request.method == "GET":  # get a single dog by its id
        dog_json = []
        dog = Dog.objects.get(id=id)

        dog_json.append(
            {
                'id': dog.id,
                "name": dog.name,
                "breed": dog.breed,
                "weight": dog.weight
            }
        )

        return JsonResponse(
            dog_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete a single dog by its id
        dog = Dog.objects.get(id=id)
        dog.delete()

    return HttpResponse("DOG")


def cats(request):

    if request.method == "POST":  # add a new cat

        data = json.loads(request.body)

        my_cat = Cat(
            name=data["name"],
            breed=data["breed"],
            weight=data["weight"]
        )
        my_cat.save()

    elif request.method == "GET":  # get all cats
        cats_json = []
        cats = Cat.objects.all()

        for cat in cats:
            cats_json.append(
                {
                    'id': cat.id,
                    "name": cat.name,
                    "breed": cat.breed,
                    "weight": cat.weight
                }
            )

        return JsonResponse(
            cats_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete all cats
        cats = Cat.objects.all()
        cats.delete()

    return HttpResponse("CAT")


def cat(request, id):

    if request.method == "GET":  # get a single cat by its id
        cat_json = []
        cat = Cat.objects.get(id=id)

        cat_json.append(
            {
                'id': cat.id,
                "name": cat.name,
                "breed": cat.breed,
                "weight": cat.weight
            }
        )

        return JsonResponse(
            cat_json,
            safe=False
        )

    elif request.method == 'DELETE':  # delete a single cat by its id
        cat = Cat.objects.get(id=id)
        cat.delete()

    return HttpResponse("CAT")
