from django.db import models

class WxUser(models.Model):
    user_openid = models.CharField(max_length =100,blank = False,default='',unique=True)
    adress = models.CharField(max_length=200,blank=True,default='')
    phonenumber= models.IntegerField(maxlength=20,blank=True,default='')
    user_name = models.CharField(max_length = 40,blank = False, default= '')
    
class Item(models.Model):
    item_num = models.IntegerField()##自动填入
    item_name = models.CharField(max_length = 100,blank=False,default='')
    owner = models.CharField(max_length= 100,blank=False,default='')
    category = models.CharField(max_length= 100,blank=False,default='')
    vedio_adress = models.CharField(max_length=400)##vedio url
    pic_adress = models.CharField(max_length=400)##pic url
    description = models.CharField(max_length=800,blank=True)

class Active_Bill(models.Model):
    bill_num = models.IntegerField()##自动生成填入
    user_openid = models.ForeignKey(related_name=WxUser)
    Item_num = models.ForeignKey(related_name=Item,)##not finished
    date_active = models.DateTimeField(auto_now_add=True)
    adress = models.CharField(max_length=200,blank = False)

class FarmUser(models.Model):
    farm_num = models.IntegerField()#自动填入
    farm_name = models.CharField(max_length=100,blank = False,default='')
    farm_adress = models.CharField(max_length= 100)

class Question(models.Model):
    Question_num=models.IntegerField()#自动填入
    category=models.CharField(max_length= 100,blank=False,default='')
    Question_text = models.CharField(max_length=400)
    option_A=models.CharField(max_length=100)
    option_B=models.CharField(max_length=100)
    option_C=models.CharField(max_length=100)
    option_D=models.CharField(max_length=100)
    correct_answer=models.CharField(max_length=100)
    



    
