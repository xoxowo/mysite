from ast import Name
import json

import re
import bcrypt

from django.http    import JsonResponse
from django.views   import View
from django.conf    import settings

from posting.models import *

class Posting(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            title    = data['title']
            text     = data['text']
            name     = data['name']
            password = data['password']   

            if not re.match('^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,16}$', password):
                return JsonResponse({'messasge':'Invalid Password Format'}, status=401)

            hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            Post.objects.create(
                title    = title,
                text     = text,
                name     = name,
                password = hash_password,
            )
            return JsonResponse({'messasge':'SUSSECE'}, status=201)

        except KeyError :
            return JsonResponse({'messasge':'KeyError'}, status=400)

    def get(self, request):
        try:
            data     = json.loads(request.body)
            name     = data['name']
            password = data['password']
            user     = Post.objects.get(name=name)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'messasge':'INVALID_USER'}, status=400)           
            
            return JsonResponse({'messasge':'SUSSECE'}, status=200)
            
        except Post.DoesNotExist:               
            return JsonResponse({"message": "INVALID_USER"}, status = 400)

        except KeyError:
            return JsonResponse({'messasge':'KeyError'}, status=400)           
