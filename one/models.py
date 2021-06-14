from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.CharField(max_length=200 ,null=False)
    def __str__(self):
        return self.Category
class product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Mahsulot Turi')
    name = models.CharField(max_length=100, null=False,verbose_name="Mahsulot Nomi")
    photo = models.CharField(max_length=200)
    price = models.FloatField(default=0, verbose_name='Narxi')
    description = models.TextField(verbose_name='Mahzulot haqida izoh')
    quantity = models.IntegerField(default=0, verbose_name='Soni')
    def __str__(self):
        return str(self.name) +' $'+str(self.price)





class incart(models.Model):
    username = models.CharField(max_length=200, null=False)
    choise = models.ForeignKey(product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name='Soni')
    def __str__(self):
        return str(self.username)+ ' '+ str(self.choise.name)