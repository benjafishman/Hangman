from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from blog.models import GemaraPost, Category

'''
The index view simply lists the categories one could click to look at
FOR NOW
'''
def index(request):

    #posts = Post.objects.filter(published=True)
    categories = Category.objects.all()

    shteig_header = "home"

    # get most recent 5 parsha posts (posts with section == parsha)
    gemara_posts = GemaraPost.objects.all()
    #halacha_posts = Post.objects.filter(section__title__startswith='Halacha')
    return render(request, 'blog/index.html', {'categories': categories, 'gemara_posts': gemara_posts, 'subheader': shteig_header})

def about(request):
    return render(request,'blog/about.html', context)

def post(request, slug):
    print("post view")
    # get the Post object
    post = get_object_or_404(GemaraPost, slug=slug)
    related_posts = GemaraPost.objects.all().exclude(pk=post.pk)

    subheader = post.get_title()
    # now return the rendered template
    return render(request, 'blog/post-gemara.html', {'post': post, 'subheader': subheader, 'related_posts':related_posts})

def category_post_list(request, category):
    print("category post view")
    print(category)
    posts = Post.objects.filter(categories__title__startswith=category)
    return render(request, 'blog/view_category.html', {'posts': posts})