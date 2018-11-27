from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime 

posts = [
    {
        'author' : 'Tzao Kai',
        'title' : 'Who am i',
        'content' : 'I am legend',
        'date_posted' : 'August, 2018' #try putting in timezone.now() 
    },
    {
        'author' : 'Belieber',
        'title' : 'What am i',
        'content' : 'an animal',
        'date_posted' : datetime.datetime.now() #try putting in timezone.now() 
    }
]

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'polls/home.html', context)


def picture(request):
    return render(request, 'polls/picture.html', {'title' : 'About'})

def chatting(request):
    return render(request, 'polls/chatting.html', {'title' : 'Chatting'})

def chatting2(request):
    return render(request, 'polls/chatting2.html', {'title' : 'Chatting2'})

def chatting3(request):
    return render(request, 'polls/chatting3.html', {'title' : 'Chatting 3!'})


def script(request):
    return render(request, 'polls/script.php', {'title': 'Script!'})


name = "Echobot 1"
weather = "Cloudy"

import random

responses = {
	"what's your name?" : ["They call me {0}".format(name), "I'm {0}".format(name), "You can call me {0}".format(name),
], 
"what's the weather?" : ["It's {0}".format(weather), "It is {0} today".format(weather)],
"question" : ["I dont know:(", "You tell me"],
"statement" : ["How long have you felt this way?","Oh why?"]
}


def send_message(request):
    print(request.POST)
    message = request.POST['message']
    print('message is ' + message)
    reply =''
    if message.endswith("?") and not (message in responses):
        reply = random.choice(responses["question"])
        print("I'm at checking of ?")
    elif message in responses:
        reply = random.choice(responses[message])
        print("I'm at checking for a random reply")
    else:
        reply = random.choice(responses["statement"])
        print("I'm at checking for a statement")
    return HttpResponse(reply) 


# from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# import os

bot = ChatBot('Test')

# bot.set_trainer(ListTrainer)

# for f in os.listdir('/home/Desktop/GovTech Projects/CHATBOT FOR WEBPAGE/files'):
#     print(f)
#     # toprocess = open('files/' + f).readlines()
#     # bot.train(toprocess)

def send_replyfromChatterbot(request):
    xinxi = request.POST['message']
    reply = bot.get_response(xinxi)
    return HttpResponse(reply)

    


