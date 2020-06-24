from django.db import models
from db.dbModels.ContactType import ContactType
from db.dbModels.Human import Human
class Contact(models.Model):
	human=models.ForeignKey(
		Human, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Человек'
	)
	type=models.ForeignKey(
		ContactType, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Тип контакта'
	)
	contact=models.TextField(
		verbose_name = 'Контакт',
		blank=True
	)
	class Meta:
		managed = True
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакты'
	def __str__(self):
		hm=''
		tp=''
		if self.human:
			hm=str(self.human)
		if self.type:
			tp=str(self.type)
		return hm+' '+tp+' '+str(self.contact)