from django.db import models

# Create your models here.
class Projects(models.Model):
    Name=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    Description=models.TextField(max_length=500)
    

    

    def __str__(self):
        return self.Name 
    
        
class Education(models.Model):
     Duration=models.CharField(max_length=50)
     program=models.CharField(max_length=50)
     School=models.CharField(max_length=50)
     Thingslearnt=models.TextField(max_length=200)

     def __str__(self):
         return self.Duration + " / " + self.program + " / " + self.School

class skills(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class programs(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class experience(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    period=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    