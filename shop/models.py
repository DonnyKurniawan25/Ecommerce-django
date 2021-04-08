from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','SportWear'),
    ('OW','OutWear')
)

LABEL_CHOICES = (
    ('S', 'secondary'),
    ('P', 'primary'),
    ('D', 'danger')
)

class Items(models.Model):
    title = models.CharField(max_length = 225)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()


    def __str__(self):
        return self.title
    

class Orderitem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
