from django.db import models
from db.dbModels.Human import Human
from db.dbModels.Theme import Theme
class StudentItem(models.Model):
	student=models.ForeignKey(
		Human, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Ученик'
	)
	item=models.ForeignKey(
		Theme, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Пункт плана'
	)
	status=models.BooleanField(
		verbose_name = 'Статус'
	)
	number=models.IntegerField(
		null=True,
		default=0,
		verbose_name = 'Номер'
	)
	class Meta:
		managed = True
		verbose_name = 'Пункт плана'
		verbose_name_plural = 'Пункты планов'
	def __str__(self):
		st=self.student.first_name+' '+self.student.last_name
		return st+' '+str(self.item.caption)