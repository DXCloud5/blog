from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles=Article.objects.all()
    return render(request,"index.html",{'articles':articles})

def  article_content(request,art_id):
    article=Article.objects.get(pk=art_id)
    return render(request,"content.html",{'art':article})

def mydelete(request,art_id):
    article=Article.objects.get(pk=art_id)
    article.delete()
    return render(request,"delete.html")



def article_edit(request,art_id):
    if str(art_id)=='0':
        return render(request,"edit.html")
    else:
        art=Article.objects.get(pk=art_id)
        return render(request, "edit.html",{'art':art})

def edit_action(request):
    title=request.POST.get("title","DEFAULT")
    content = request.POST.get("content","DEFAULT")
    pub_time = request.POST.get("pub_time","DEFAULT")
    author = request.POST.get("author","DEFAULT")
    art_class = request.POST.get("art_class", "DEFAULT")
    art_id=request.POST.get("art_id","0")
    if art_id=='0':
        Article.objects.create(title=title,content=content,pub_time=pub_time,author=author,art_class=art_class)
        arts=Article.objects.all()
        return render(request,"index.html",{'articles':arts})
    else:
        article=Article.objects.get(pk=art_id)
        article.title=title
        article.content=content
        article.pub_time=pub_time
        article.author=author
        article.art_class=art_class
        article.save()
        article=Article.objects.get(pk=art_id)
        return render(request,"content.html",{"art":article})


# Create your views here.
