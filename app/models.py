from django.db import models

# Create your models here.
class Employ(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    eage=models.IntegerField()
    def __str__(self) -> str:
        return self.ename
