from django.contrib import admin
from .models import Category, Resources, Tag, ResourceSubmission

admin.site.register(Category)

admin.site.register(Resources)

admin.site.register(Tag)

admin.site.register(ResourceSubmission)

# Register your models here.
