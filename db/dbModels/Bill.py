from django.db import models
from db.dbModels.Human import Human
from db.dbModels.Lesson import Lesson
class Bill(models.Model):
	status=models.BooleanField(
		verbose_name = 'Оплата'
	)
	agent= models.ForeignKey(
		Human, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Кому'
	)
	lesson= models.OneToOneField(
		Lesson, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Занятие'
	)
	billingDate=models.DateTimeField(
		verbose_name = 'Дата выставления',
		null=True, 
		blank=True
	)
	receiptDate=models.DateTimeField(
		verbose_name = 'Дата получения',
		null=True, 
		blank=True
	)
	ammount=models.FloatField(
		verbose_name = 'Сумма',
		default=0
	)
	text=models.TextField(
		verbose_name = 'Сообщение',
		blank=True
	)
	class Meta:
		managed = True
		verbose_name = 'Счет'
		verbose_name_plural = 'Счета'
	def __str__(self):
		ag=''
		if self.agent:
			ag=self.agent.first_name+' '+self.agent.last_name
		return ag+' '+str(self.lesson.date)+str(self.status)