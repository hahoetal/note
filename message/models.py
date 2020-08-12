from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    sender = models.ForeignKey(User, default="알 수 없음", on_delete=models.SET_DEFAULT)
    # 유저 정보가 삭제되더라도 해당 유저가 보낸 쪽지가 삭제되지 않도록 on_delete에 models.SET_DEFAULT를 줌.
    receiver = models.CharField(max_length=100)
    send_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    content = models.TextField()
    scount = models.IntegerField(default=0)
    rcount = models.IntegerField(default=0)
    renotes_s = models.IntegerField(default=0)
    renotes_r = models.IntegerField(default=0)
    
    def summary(self):
        return self.content[:30]

class ReNote(models.Model):
    author = models.ForeignKey(User, default="알 수 없음", on_delete=models.SET_DEFAULT)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    # is_read = models.BooleanField(default=False)