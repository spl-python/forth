from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(decimal_places=2,max_digits=8)
    pic = models.ImageField(upload_to='pic',null=True)

    class Meta:
        db_table = 'stu'


