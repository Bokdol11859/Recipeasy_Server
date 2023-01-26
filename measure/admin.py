from django.contrib import admin

# Register your models here.
from measure.models import Measurement

admin.site.register(Measurement)