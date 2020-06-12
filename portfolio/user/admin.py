from django.contrib import admin
from .models import user, Category, Contents

# Register your models here.

admin.site.register(user)
admin.site.register(Category)
admin.site.register(Contents)
