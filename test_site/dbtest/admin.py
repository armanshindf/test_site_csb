from django.contrib import admin

# Register your models here.

from .models import Categories
from .models import Stuff



admin.site.register(Categories)

admin.site.register(Stuff)