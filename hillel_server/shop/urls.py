# Доробити проект, що ми почали робити на уроці:
# Аналогічно таблиці Dog, створити таблицю Cat. ТАкож потрібно зробити endpoint в залежності від методу якого буде
# відбуватися створення, отримання або видалення кота в нашій БД.

from django.urls import path

from shop.views import hello_page, dogs, dog, cats, cat

urlpatterns = [
    path('hello/', hello_page),
    path('dog/', dogs),
    path('dog/<id>', dog),
    path('cat/', cats),
    path('cat/<id>', cat),
]