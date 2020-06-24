from django.db import models
from db.dbModels.Human import Human
from db.dbModels.Course import Course
from db.dbModels.Theme import Theme
#from db.dbModels.Bill import Bill
class Lesson(models.Model):
	theme= models.CharField(
		max_length=255,
		blank=True,
		verbose_name = 'Тема'
	)
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
	date=models.DateTimeField(
		verbose_name = 'Дата/Время'
	)
	decription=models.TextField(
		verbose_name = 'Описание',
		blank=True
	)
	number=models.IntegerField(
		verbose_name = 'Номер занятия',
		default=0
	)
	class Meta:
		managed = True
		verbose_name = 'Занятие'
		verbose_name_plural = 'Занятия'
	def __str__(self):
		if self.student:
			st=self.student.first_name+' '+self.student.last_name
		else: st=''
		return st+' '+str(self.date)