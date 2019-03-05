from django.contrib import admin
from .models import Blog
from .models import Portfolio

admin.site.register(Blog)
admin.site.register(Portfolio)