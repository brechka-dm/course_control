from django.db import models
from db.dbModels.Course import Course
from db.dbModels.Human import Human
class Distribution (models.Model):
	student= models.ForeignKey(
		Human, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Ученик'
	)
	course= models.ForeignKey(
		Course, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Курс'
	)
	class Meta:
		managed = True
		verbose_name = 'Распределение'
		verbose_name_plural = 'Распределения'
	def __str__(self):
		st=self.student.first_name+' '+self.student.last_name
		return st+' '+self.course.name