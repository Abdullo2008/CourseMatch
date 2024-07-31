from django.contrib import admin
from .models import CourseModel, BlogModel, ContactModel, Category

admin.site.register(CourseModel)
admin.site.register(BlogModel)
admin.site.register(Category)
admin.site.register(ContactModel)
