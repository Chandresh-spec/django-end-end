from django.shortcuts import render
import random
from .models import Book
# Create your views here.
jokes=[
    "this is first  joke",
    "this is second joke",
    " this is the third joke"
]

def random_joke(request):
    joke=random.choice(jokes)
    return render(request,"joke.html",{'joke':joke})

def random_joke2(request):
    joke=random.choice(jokes)

    return render(request,'joke2.html',{'joke':joke})

quotes=[
    "Be yourself; everyone else is already taken",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "In the middle of every difficulty lies opportunity.",
    "Do something today that your future self will thank you for.",
    "The best way to predict the future is to create it.",


]
def quote_OfThe_Day(request):
    quote=random.choice(quotes)
    return render(request,'app/layout.html',{'quote':quote})

def display(request):
    return render(request,'app1/index.html')

def quotes_the(request,id):
    quote=quotes[id]
    return render(request,'app1/display.html',{'quote':quote})



def Boks(request):
    books=Book.objects.all()
    return render(request,'app2/book.html',{'books':books})


def Home(request):
    books=Book.objects.all()
    return render(request,'app2/book.html',{'books':books})