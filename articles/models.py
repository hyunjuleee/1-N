from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

# models.ForeignKey는
# Comment 모델에는 article_id
# Article 모델에는 comment_set을 자동으로 생성