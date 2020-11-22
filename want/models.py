from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_owner')
    group = models.ForeignKey('Group',on_delete=models.CASCADE,)
    content = models.TextField(max_length=1000)
    shared_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    shared_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + '(' + str(self.owner) + ')'

    def get_share(self):
        return Message.objects.get(id=self.shared_id)
    
    class Meta:
        ordering = ('-pub_date',)

class Group(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_name')
    title = models.CharField(max_length=30)



    
    
    




