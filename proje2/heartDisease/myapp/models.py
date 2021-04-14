from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    id_number = models.CharField(max_length=11)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


class Values(models.Model):
    age = models.IntegerField(default=0, null=False)
    sex = models.BooleanField(default=False, null=False)
    cp = models.IntegerField(default=0, null=False)
    trestbps = models.IntegerField(default=0, null=False)
    chol = models.IntegerField(default=0, null=False)
    fbs = models.BooleanField(default=False, null=False)
    restecg = models.BooleanField(default=False, null=False)
    thalach = models.IntegerField(default=0, null=False)
    exang = models.BooleanField(default=False, null=False)
    oldpeak = models.FloatField(default=0.0, null=False)
    slope = models.IntegerField(default=0, null=False)
    ca = models.BooleanField(default=False, null=False)
    thal = models.IntegerField(default=0, null=False)
    target = models.BooleanField()
    percent_of_disease = models.CharField(max_length=11, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
