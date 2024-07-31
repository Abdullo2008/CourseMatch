from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('course/<int:id>/', course, name='course'),
    path('courses', courses, name='courses'),
    path('category/<int:id>/', single_category, name="single_category"),
    path('contact', Contact.as_view(), name='contact'),
    path('ghost11/', Contacts, name='contacts'),
    path('addcourse', AddCourse.as_view(), name='addcourse'),
    path('addblog', AddBlog.as_view(), name='addblog'),
    path('addcategory', AddCategory.as_view(), name='addcategory'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update'),
    path('updateblog/<int:pk>/', BlogUpdateView.as_view(), name='updateblog'),
    path('deleteblog/<int:pk>/', BlogDeleteView.as_view(), name='deleteblog'),
    path('search/', SearchView, name='search'),
]
