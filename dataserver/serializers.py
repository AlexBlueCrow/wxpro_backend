from rest_framework import serializers
from dataserver.models import WxUser,Item,Active_Bill,FarmUser,Question


class WxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WxUser
        fields = ('user_openid', 'address','phonenumber','user_name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_num','item_name','owner','category','vedio_address','pic_address','description')

class Active_BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active_Bill
        fields = ('bill_num','user_openid','item_num','date_active','address')

class FarmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmUser
        fields = ('farm_num','farm_name','farm_address')

class QuestionSerializer(serializers.ModelSerializer):
    model = Question
    fields = ('question_num',
    'category',
    'question_text',
    'option_A',
    'option_B',
    'option_C',
    'option_D',
    'correct_answer')
