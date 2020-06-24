from django.db import models
from db.dbModels.Course import Course
class Theme(models.Model):
	caption=models.CharField(
		max_length=100, 
		verbose_name = 'Тема'
	)
	description=models.TextField(
		verbose_name = 'Описание',
		blank=True
	)
	course= models.ForeignKey(
		Course, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Курс'
	)
	number=models.IntegerField(
		null=True,
		default=0,
		verbose_name = 'Номер'
	)
	class Meta:
		managed = True
		verbose_name = 'Тема'
		verbose_name_plural = 'Темы'
	def __str__(self):
		return self.caption