from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return self.name


class CourseModel(models.Model):
    course = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, default=True)
    date_added = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.course

    class Meta:
        ordering = ["-id"]


class BlogModel(models.Model):
    course = models.ForeignKey(CourseModel,
                               on_delete=models.CASCADE)
    blog = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blog

    class Meta:
        ordering = ["id"]


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
