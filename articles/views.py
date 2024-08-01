from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    comments = Comment.objects.filter(article_id=id) #
    context = {
        'article': article,
        'form': form,
        'comments': comments, #
    }
    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 방금 사용자가 입력한 데이터로 html
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm() # 빈 html을 만듦
    
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)
    # context는 if문 밖
    # form.html > update랑 같은 페이지 사용

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 임시저장 (article_id가 입력되지 않았으므로)
            
            # 1. 객체를 저장하는 방법
            # article = Article.objects.get(id=article_id)
            # comment.article = article
            # comment.save()

            # 2. integer(숫자)를 저장하는 방법
            comment.article_id = article_id
            comment.save()

            return redirect('articles:detail', id=article_id)
    else:
        return redirect('articles:index')

def comment_delete(request, article_id, id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
    return redirect('articles:detail', id=article_id)