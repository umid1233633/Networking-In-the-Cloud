from django.contrib import admin
from .models import Product, Task, Order, Collaboration, Invoice, Info

admin.site.register(Product)
admin.site.register(Task)
admin.site.register(Order)
admin.site.register(Collaboration)
admin.site.register(Invoice)
admin.site.register(Info)
