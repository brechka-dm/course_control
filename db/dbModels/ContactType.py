from django.db import models
class ContactType(models.Model):
	name=models.CharField(
		max_length=255,
		blank=True,
		verbose_name = 'Тип контакта'
	)
	function=models.CharField(
		max_length=255,
		blank=True,
		verbose_name = 'Функция'
	)
	class Meta:
		managed = True
		verbose_name = 'Тип контакта'
		verbose_name_plural = 'Типы контактов'
	def __str__(self):
		return self.name