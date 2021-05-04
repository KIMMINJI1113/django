from django.db import models

# Create your models here.
class Questions(models.Model):   #관계형 db생성을 하려면 쭉쭉쭉 밑으로 이어 붙이면 된다.
    subject = models.CharField(max_length=200) #제목
    content = models.TextField() # 제목밑에 글들
    create_date= models.DateTimeField()  #생성했던 날짜

