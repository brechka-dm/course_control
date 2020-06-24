from django.db import models
class Course(models.Model):
	name = models.CharField(
		max_length=100, 
		verbose_name = 'Название'
	)
	class Meta:
		managed = True
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
	def __str__(self):
		return self.name