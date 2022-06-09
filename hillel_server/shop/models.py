# Доробити проект, що ми почали робити на уроці:
# Аналогічно таблиці Dog, створити таблицю Cat. ТАкож потрібно зробити endpoint в залежності від методу якого буде
# відбуватися створення, отримання або видалення кота в нашій БД.


from django.db import models

# Create your models here.


class Dog(models.Model):

    name = models.CharField(unique=True, max_length=100)  # dogs must have unique names
    breed = models.CharField(max_length=100)
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Cat(models.Model):

    name = models.CharField(max_length=50)  # but it's not necessary for cats to have unique names
    breed = models.CharField(max_length=50)
    weight = models.FloatField()

    def __str__(self):
        return self.name

