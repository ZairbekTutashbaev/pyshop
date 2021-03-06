from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title



class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'In Stock'),
        ('out of stock', 'Out of Stock'),
        ('await', 'Awaiting')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)

    def __str__(self):
        return self.title

