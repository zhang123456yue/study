from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)#注意后面的参数

	def __str__(self):
		return self.text


class Entry(models.Model):
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50] + "...."#我认为切片是用于列表的
# Create your models here.
