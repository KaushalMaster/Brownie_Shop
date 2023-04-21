from django.db import models

# Create your models here.


class Products(models.Model):
    Product_id = models.IntegerField(unique=True)
    Product_Name = models.CharField(max_length=100)
    Product_image = models.ImageField(upload_to='media', default='')
    Product_Price = models.FloatField()

    def __str__(self):
        return self.Product_Name

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.Product_image.url
    #     except:
    #         url = ''
    #     return url


class Product_details(models.Model):
    P_id = models.AutoField
    Product_img_one = models.ImageField()
    Product_img_two = models.ImageField()
    Product_img_three = models.ImageField()
    Product_img_four = models.ImageField()
    Product_name = models.TextField()
    Product_price = models.FloatField()
    Product_description = models.TextField()
    Product_Quantity = models.IntegerField()
    Product_category = models.CharField(max_length=100)
    Product_tags = models.CharField(max_length=50)

    def __str__(self):
        return self.Product_name


class registerOrders(models.Model):
    o_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    brownie = models.CharField(max_length=50)
    quantity = models.IntegerField()
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name
