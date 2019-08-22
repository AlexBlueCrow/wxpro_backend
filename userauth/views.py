from django.shortcuts import render

import hashlib
import json
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_redis import get_redis_connection
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def code2Session(request):
    appid = ''
    secret = ''
    js_code = request.data['code']
    url = 'https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid + '&secret=' + secret + '&js_code=' + js_code + '&grant_type=authorization_code'
    response = json.loads(requests.get(url).content) # 将json数据包转成字典
    
    if 'errcode' in response:
    # 有错误码
    return Response(data={'code':response['errcode'], 'msg': response['errmsg']})

    # 登录成功
    openid = response['openid']
    session_key = response['session_key']
    # 保存openid, 需要先判断数据库中有没有这个openid
    user, created = User.objects.get_or_create(openid=openid)
    user_str = str(UserSerializer(user).data)
    # 生成自定义登录态，返回给前端
    sha = hashlib.sha1()
    sha.update(openid.encode())
    sha.update(session_key.encode())
    digest = sha.hexdigest()
    # 将自定义登录态保存到缓存中, 两个小时过期
    conn = get_redis_connection('default')
    conn.set(digest, user_str, ex=2*60*60)
    return Response(data={'code': 200, 'msg': 'ok', 'data': {'skey': digest})

    

