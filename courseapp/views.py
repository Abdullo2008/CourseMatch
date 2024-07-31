from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CourseEditForm, BlogEditForm
from .models import CourseModel, BlogModel, ContactModel, Category


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def Contacts(request):
    model = ContactModel.objects.all()
    context = {
        'contacts': model
    }
    return render(request, 'contacts.html', context)


class Contact(CreateView):
    model = ContactModel
    template_name = 'contact.html'
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('index')


def course(request, id):
    categorys = BlogModel.objects.all().filter(course_id=id)
    if list(categorys) == []:
        new_blog = categorys
    else:
        new_blog = zip(list(range(1, len(categorys) + 1)), categorys)
    context = {
        'blogs': new_blog
    }
    return render(request, 'blogs/course.html', context)


def courses(request):
    curses = CourseModel.objects.all()
    categories = Category.objects.all()
    context = {
        'curses': curses,
        'categories': categories
    }
    return render(request, 'courses/courses.html', context)


class AddBlog(CreateView):
    model = BlogModel
    template_name = 'blogs/addblog.html'
    fields = ['course', 'blog']
    success_url = reverse_lazy('courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CourseModel.objects.all()
        return context


class AddCourse(CreateView):
    model = CourseModel
    template_name = 'courses/add.html'
    fields = ('course', 'image', 'title', 'body', 'category')
    success_url = reverse_lazy('courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ['name']
    success_url = reverse_lazy('courses')


class CourseDeleteView(DeleteView):
    model = CourseModel
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses')


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = 'blogs/deleteblog.html'
    success_url = reverse_lazy('courses')


class CourseUpdateView(UpdateView):
    model = CourseModel
    template_name = 'courses/update.html'
    form_class = CourseEditForm
    success_url = reverse_lazy('courses')


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = 'blogs/update_blog.html'
    form_class = BlogEditForm
    success_url = reverse_lazy('courses')


def SearchView(request):
    search = ''
    courses_search = CourseModel.objects.none()  # Default to an empty queryset
    courses_all = CourseModel.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', '')
        if search:
            courses_search = CourseModel.objects.filter(course__contains=search)

    return render(request, 'search.html', {
        'search': search,
        'courses_search': courses_search,
        'courses_all': courses_all
    })


def single_category(request, id):
    curses = CourseModel.objects.all().filter(category_id=id).order_by('-id')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'curses': curses
    }
    return render(request, 'single_category.html', context)
