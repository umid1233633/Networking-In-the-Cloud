from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('superuser', 'Superuser'),
        ('simpleuser', 'Simple User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='simpleuser')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    hub = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.sku}"


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Order(models.Model):
    ORDER_STATUS = [
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    customer_name = models.CharField(max_length=10)
    products = models.ManyToManyField(Product,blank=True,null=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='new')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"



class Collaboration(models.Model):
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    partnership_type = models.CharField(max_length=100, help_text="e.g. Supplier, Distributor")
    agreement_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} ({self.partnership_type})"




class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} for Order #{self.order.id}"



class Info(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
