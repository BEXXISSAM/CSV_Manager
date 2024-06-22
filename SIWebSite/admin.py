from django.contrib import admin
from .models import ImportFileModel
from .models import RIDModel
admin.site.register(RIDModel)
admin.site.register(ImportFileModel)

# Register your models here.
