from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        print("in here")
        print([self.slug])
        return reverse('blog:blog_detail', args=[self.slug])

    def get_categories(self):
        return ", ".join([c.title for c in self.categories.all()])


