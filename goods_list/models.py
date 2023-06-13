from django.db import models


class Goods(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "db_goods: " + str(self.id)

    class Meta:
        managed = True
        db_table = 'goods'


class CategoryGoods(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = True
        db_table = 'category_goods'


class Promotions(models.Model):
    id = models.BigAutoField(primary_key=True)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'promotions'
