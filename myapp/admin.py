from django.contrib import admin
from .models import BookCarModel, DisplayCarsModel

# Register your models here.

admin.site.register(BookCarModel)
admin.site.register(DisplayCarsModel)