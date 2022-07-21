from django.db import models
from user.models import User


class Post(models.Model):
    writer = models.ForeignKey(to=User, verbose_name='작성자', on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=50)
    content = models.CharField('내용', max_length=255)
    hashtag = models.CharField('해시태그', max_length=255)
    hits = models.PositiveIntegerField('조회수', default=0)
    likes = models.PositiveBigIntegerField('좋아요', default=0)
    delete_flag = models.BooleanField('삭제 상태', default=False)  # True: 삭제
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return f'{self.title} / {self.writer}'

    def toggle_active(self):
        self.delete_flag = not self.delete_flag
        self.save()
        message = '삭제' if self.delete_flag else '복구'
        self.delete_message = {'success': f'{message}되었습니다.'}
