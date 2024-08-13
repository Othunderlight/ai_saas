 
from django.db import models
from django.contrib.auth.models import User
import shortuuid
 



class AiModel(models.Model):
    name= models.CharField(max_length=255, blank=True, default='') 
    discription= models.CharField(max_length=255, blank=True, default='')
    short_discription= models.CharField(max_length=255, blank=True, default='') 
    main_tag= models.CharField(max_length=255, blank=True, default='')  
    tags= models.CharField(max_length=255, blank=True, default='') 
    senario_1= models.CharField(max_length=255, blank=True, default='')
    senario_2= models.CharField(max_length=255, blank=True, default='')
    senario_3= models.CharField(max_length=255, blank=True, default='') 
    best_use_case= models.CharField(max_length=255, blank=True, default='')
    skills= models.CharField(max_length=255, blank=True, default='')
    languages= models.CharField(max_length=255, blank=True, default='')
    tokens= models.CharField(max_length=255, blank=True, default='')  
    api= models.CharField(max_length=255, blank=True, default='')   
    img_icon= models.ImageField(upload_to='/', default='')
    img_hero= models.ImageField(upload_to='/', default='')

    def __str__(self):
        return f'{self.name}'



class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True, blank=True)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)
    ai_model= models.ForeignKey(AiModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        if not self.group_name:
            self.group_name = shortuuid.uuid()
        super().save(*args, **kwargs)    
        

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.body or "File Message"}'

