from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    sender = models.ForeignKey(User, default="알 수 없음", on_delete=models.SET_DEFAULT)
    # 유저 정보가 삭제되더라도 해당 유저가 보낸 쪽지가 삭제되지 않도록 on_delete에 models.SET_DEFAULT를 줌.
    receiver = models.CharField(max_length=100)
    send_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField()
    content = models.TextField()
    scount = models.IntegerField(default=0)
    rcount = models.IntegerField(default=0)
    
    def summary(self):
        return self.content[:30]