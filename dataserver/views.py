from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from dataserver.models import WxUser,Item,Active_Bill,FarmUser,Question
from dataserver.serializers import WxUserSerializer,ItemSerializer,Active_BillSerializer,FarmUserSerializer,QuestionSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs) 


def login(request):
    appid= 'wx48c0b0d820c4563d'
    appid= 'wxb3c126a3f39ffb03'
    secret='4acdae8837a2d8e8a6a675193394eed1'
    JSCODE = request.GET.get('code')
    if JSCODE:
        wxLoginURL = 'https://api.weixin.qq.com/sns/jscode2session?' +'appid='+appid+'&secret='+secret+'&js_code='+JSCODE+'&grant_type='+'authorization_code'
        r = requests.get(wxLoginURL)
        print('response:',r.content)
        data = requests.get
        return HttpResponse(r)
    else:
        return HttpResponseNotFound

def get_active_bill(request):
    active_bill= Active_Bill.objects.get(openid = openid)
    active_bill_serializer = Active_BillSerializer(active_bill, many=True)
    return JSONResponse(active_bill_serializer.data)





def get_item(request):
    item = Item.objects.all()
    item_serializer = ItemSerializer(item,mant=True)
    return JSONResponse(item_serializer.data)


#def get_questions():

#def get_farmuser():

#def data_response():

#def get_wxuser(request):
    

    

    









