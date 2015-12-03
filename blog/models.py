from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title


class Section(models.Model):
    title = models.CharField(max_length=255)

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
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        print("in here")
        print([self.slug])
        return reverse('blog:blog_detail', args=[self.slug])

    def get_categories(self):
        return ", ".join([c.title for c in self.categories.all()])


class GemaraPost(Post):
    AMUDS = (
        ('0','A'),
        ('1','B')
    )
    gemara = models.ForeignKey('Gemara', null=True)
    daf = models.IntegerField(default=0, blank=True, null=True)
    amud = models.CharField(max_length=2, choices=AMUDS)


class Mesechta(models.Model):
    SEDERS = (
        ('Zr', 'Zraim'),
        ('Mo', 'Moed'),
        ('Na', 'Nashim'),
        ('Ne', 'Nesikim'),
        ('Ko', 'Kodashim'),
        ('To', 'Toharoth'),
    )
    seder = models.CharField(max_length=2, choices=SEDERS)

    def __str__(self):
        seder_dict = {'Zr': 'Zraim', 'Mo': 'Moed' ,'Na':'Nashim', 'Ne':'Nesikim', 'Ko':'Kodashim','To':'Toharoth'}
        return u'%s' % seder_dict[self.seder]

class Gemara(models.Model):
    title = models.CharField(max_length=100, unique=True)
    seder = models.CharField(max_length=100, unique=True)
    number_of_daf = models.IntegerField(default=0, blank=True, null=True)
    number_of_perakim = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return u'%s' % self.title

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return u'%s' % self.name

class Statement(models.Model):
    person = models.ForeignKey(Person, null=True)
    statement = models.TextField()
    gemara_post = models.ForeignKey(GemaraPost, null=True)


    def __str__(self):
        return u'%s' % self.id

class Challenge(models.Model):
    title = models.CharField(max_length=100, unique=True)
    challenger = models.ForeignKey(Person, null=True)
    challenged_statement = models.ForeignKey(Statement)
    content = models.TextField()
    gemara_post = models.ForeignKey(GemaraPost)


    def __str__(self):
        return u'%s' % self.title

class Challenge_Resolution(models.Model):
    challenge = models.ForeignKey(Challenge)
    resolver = models.ForeignKey(Person)
    resolution_text = models.TextField()

    def __str__(self):
        return u'%s' % self.id









