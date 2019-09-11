from django.shortcuts import render

import requests

# Create your views here.
def login(request):
    print(request)
    if request.code:
        appid= 'wx48c0b0d820c4563d'
        secret='4acdae8837a2d8e8a6a675193394eed1'
        JSCODE=request.data.code
        wxLoginURL = 'https://api.weixin.qq.com/sns/jscode2session?' +'appid='+appid+'&secret='+secret+'&js_code='+JSCODE+'&grant_type='+authorization_code
        r = requests.get( wxLoginURL ,request.data.code)
        print(r)
    

