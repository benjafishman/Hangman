from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from blog.models import GemaraPost, Category, ParshaPost, Chumash,\
Parsha, ParshaQuestion
from django.http import HttpResponse

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
    print("request: " + str(request))
    print("slug: " + slug)
    # get the Post object
    #post = get_object_or_404(GemaraPost, slug=slug)
    post = get_object_or_404(ParshaPost, slug=slug)
    related_posts = GemaraPost.objects.all().exclude(pk=post.pk)

    template_name = 'post-' + post.get_template_suffix() + '.html'

    subheader = post.get_title()
    # now return the rendered template
    return render(request, 'blog/'+template_name, {'post': post, 'subheader': subheader, 'related_posts':related_posts})

def category_post_list(request, category):
    print("category post view")
    print(category)
    posts = Post.objects.filter(categories__title__startswith=category)
    return render(request, 'blog/view_category.html', {'posts': posts})

def chumash_parsha_listing(request):
    #genesis = Parsha.objects.filter(chumash__title__startswith='Genesis').order_by('order')
    chumash = {'Genesis':
                   ['Bereishis','Noach','Lech Lecha', 'Vayeira','Chayei Sara', 'Toldos', 'Vayeitzei',\
                    'Vayishlach','Vayeishev','Mikeitz','Vayigash','Vayechi'],
               'Exodus':[],
               'Leviticus':[],
               'Numbers':[],
               'Deuteronomy':[]
    }
    return render(request, 'blog/chumash-parsha-list.html', {'books':chumash})

def sefer_parsha_listing(request, sefer):

    chumash = {'Genesis':
                   ['Bereishis','Noach','Lech Lecha', 'Vayeira','Chayei Sara', 'Toldos', 'Vayeitzei',\
                    'Vayishlach','Vayeishev','Mikeitz','Vayigash','Vayechi'],
               'Exodus':[],
               'Leviticus':[],
               'Numbers':[],
               'Deuteronomy':[]
    }
    parshas = []
    if sefer in chumash:
        parshas = chumash[sefer]
    print(parshas)
    return render(request, 'blog/sefer_parsha_listing.html', {'parshas':parshas, 'sefer':sefer})

def parsha_questions_list(request, parsha_name):
    # get all questions related to parsha id returned in descending order by date creaed

    # convert query string to lower case
    parsha_name = parsha_name.lower()
    questions = ParshaQuestion.objects.filter(parsha__eng_name=parsha_name).order_by('created')
    return render(request, 'blog/parsha_questions_list.html', {'questions':questions})

def parsha_question_detail(request, question_id):
    question = get_object_or_404(ParshaQuestion, pk=question_id)

    # query for other question in selected parsha but exclud current question
    related_question = ParshaQuestion.objects.filter(parsha__eng_name=question.parsha.eng_name).exclude(pk=question.pk)
    return render(request, 'blog/parsha_question_detail.html',{'question':question,'related_questions': related_question})