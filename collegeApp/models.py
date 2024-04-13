from django.db import models

# Create your models here.
class Role(models.Model):
    name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Dept(models.Model):
    name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Facilitys(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    salary=models.IntegerField()
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    dept=models.ForeignKey(Dept, on_delete=models.CASCADE)
    phoneno=models.IntegerField()
    def __str__(self) :
        return self.fname