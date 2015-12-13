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

    def get_title(self):
        return self.title

class ParshaPost(Post):
    CHUMASH = ((1,'Genesis'),(2,'Exodus'),(3,'Leviticus'),(4,'Deutoronomy'),(5,'Bamidbar'))
    sefer = models.IntegerField(choices=CHUMASH)

    def get_template_suffix(self):
        return 'parsha'

class GemaraPost(Post):
    AMUDS = (
        ('0','A'),
        ('1','B')
    )
    gemara = models.ForeignKey('Gemara', null=True)
    daf = models.IntegerField(default=0, blank=True, null=True)
    amud = models.CharField(max_length=2, choices=AMUDS)

    def get_title(self):
        return self.gemara.title


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
    is_challenge = models.BooleanField(default=False)
    is_resolution = models.BooleanField(default=False)
    is_mishnah = models.BooleanField(default=False)
    is_gemara = models.BooleanField(default=False)

    def __str__(self):
        return u'%s' % self.id

class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return u'%s' % self.title

class ParshaQuestion(Question):
     parsha = models.ForeignKey('Parsha', null=True)


class Chumash(models.Model):
    title = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return u'%s' % self.title

class Parsha(models.Model):
    eng_name = models.CharField(max_length=100, unique=True)
    chumash = models.ForeignKey(Chumash, null=True)
    order = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return u'%s' % self.eng_name

    def sefer(self):
        return self.chumash.title

    class Meta:
        ordering = ['order']







