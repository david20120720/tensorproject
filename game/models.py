from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# Create your models here.
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')    
    def __str__(self):  # __unicode__ on Python 2
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    
    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text
    
        
class Game(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    #http:\\ 는 에러발생함 , //로 해야 정상작동함
    url=models.URLField()
    email=models.EmailField()
    cdate=models.DateTimeField(auto_now_add=True)    
    def __str__(self):  # __unicode__ on Python 2
        return self.name