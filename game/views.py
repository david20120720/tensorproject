import tensorflow as tf
from django.http import HttpResponse
import pygame
#from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.template import loader
# Create your views here.
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('game/index.html')
    context = { 'latest_question_list': latest_question_list, }
    return render(request,'game/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'game/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def gamesp(request):
#    import spider_v1
#    if game_id==3 :
#       from game import spider_v1
    #    print('Hello, world. You are at the game spider %s')
#       spider_v1.spider()
#    elif game_id==6 :
#        from game import jinja
    #    print('Hello, world. You are at the game spider %s')
#        jinja.py.jinja()

#    from tensorproject import spider_v1
#    if(__name__ == "__main__"):
#      print("main 으로 실행됨")
 #   else: print("import 됨")
#    return HttpResponse("Thank you . End of the game spider %s." % game_id)
#    pigame_id=game_id
       return render(request,'game/car.html')

def gamejin(request):
#    import spider_v1
#    if game_id==3 :
       from game import jinja
    #    print('Hello, world. You are at the game spider %s')
       jinja.jin()
#    elif game_id==6 :
#        from game import jinja
    #    print('Hello, world. You are at the game spider %s')
#        jinja.py.jinja()

#    from tensorproject import spider_v1
#    if(__name__ == "__main__"):
#      print("main 으로 실행됨")
 #   else: print("import 됨")
#    return HttpResponse("Thank you . End of the game spider %s." % game_id)
#    pigame_id=game_id
       return render(request,'game/gameexe.html')



def gametensor(request,num1,num2):
    from game import gametensor
    gametensor.gameten(request,num1,num2)
#    return render(request,'game/gameexe.html')
    return render(request,'game/gametensor.html')
