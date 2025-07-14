from django.shortcuts import render
import random
# Create your views here.
jokes=[
    "this is first  joke",
    "this is second joke",
    " this is the third joke"
]

def random_joke(request):
    joke=random.choice(jokes)
    return render(request,"joke.html",{'joke':joke})

