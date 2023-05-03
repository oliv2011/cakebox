from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Cakes(models.Model):
    name=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    shape_options=(
        ("round","round"),
        ("rectangle","rectangle"),
        ("square","square"),
        ("oval","oval")
    )
    shape=models.CharField(max_length=100,choices=shape_options,default="round")
    layers_options=(
        ("one","one"),
        ("two","two"),
        ("three","three")
    )
    layers=models.CharField(max_length=100,choices=layers_options,default="one")
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images",default=True)
    price=models.PositiveIntegerField()

    def _str_(self):
        return self.name
    
class Orders(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=100,choices=options,default="order-placed")
    curDate=datetime.date.today()
    expdate=curDate+datetime.timedelta(days=1)
    expected_deliverydate=models.DateTimeField(default=expdate)
    address=models.CharField(max_length=100,null=True)

class Carts(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=order,default="in-cart")
    quantity=models.PositiveIntegerField(default=1)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def _str_(self):
        return self.comment