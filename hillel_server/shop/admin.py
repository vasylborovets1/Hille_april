# Доробити проект, що ми почали робити на уроці:
# Аналогічно таблиці Dog, створити таблицю Cat. ТАкож потрібно зробити endpoint в залежності від методу якого буде
# відбуватися створення, отримання або видалення кота в нашій БД.

from django.contrib import admin

# Register your models here.
from shop.models import Dog
from shop.models import Cat

admin.site.register(Dog)
admin.site.register(Cat)
