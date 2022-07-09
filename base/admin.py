from pyexpat.errors import messages
from django.contrib import admin
from .models import *


admin.site.register(Room)
admin.site.register(message)
admin.site.register(Topic)

