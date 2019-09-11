from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import requests

# Create your views here.
appid= 'wx48c0b0d820c4563d'
secret='4acdae8837a2d8e8a6a675193394eed1'
def login(request):
    JSCODE = request.GET.get('code')
    if JSCODE:
        wxLoginURL = 'https://api.weixin.qq.com/sns/jscode2session?' +'appid='+appid+'&secret='+secret+'&js_code='+JSCODE+'&grant_type='+authorization_code
        r = requests.get(wxLoginURL)
        print(r)
        return HttpResponse(r)
    else:
        return HttpResponseNotFound
    

