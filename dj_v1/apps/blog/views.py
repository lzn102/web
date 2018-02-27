from django.shortcuts import render
from .models import Article
from .forms import WriteForm
from datetime import datetime, date
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    titles = Article.objects.order_by("-add_time")
    context = {"titles": titles}
    return render(request, "blog/index.html", context)


def detail(request, title_id):
    article = Article.objects.get(pk=title_id)
    context = {"article": article}
    return render(request, "blog/detail.html", context)


def write(request):
    if request.method == "GET":
        return render(request, "blog/write.html")
    elif request.method == "POST":
        form = WriteForm(request.POST)
        if form.is_valid():
            new_article = Article.objects.create(
                title=request.POST["title"],
                author=request.POST["author"],
                content=request.POST["content"],
                add_time=datetime.now()
            )
            title_id = new_article.id
            return HttpResponseRedirect(reverse("blog:detail", args=[title_id]))
        else:
            return render(request, "blog/write.html")
