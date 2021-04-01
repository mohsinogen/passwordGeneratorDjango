from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
        return render(request, 'generator/home.html')

def password(request):
        length = int(request.GET.get('length'))
        characters = list('abcdefghijklmnopqrstuvwxyz')
        thePassword = ''
        if length in range(6,16):
                if request.GET.get('uppercase'):
                        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

                if request.GET.get('numbers'):
                        characters.extend('1234567890')
                
                if request.GET.get('specialChar'):
                        characters.extend("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

                for x in range(length):
                        thePassword += random.choice(characters)
                return render(request, 'generator/password.html', {'password': thePassword})
        else:
                return HttpResponse("Not a Valid Request")
