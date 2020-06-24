from django.db import models
class Human(models.Model):
	STAT=[
		('STUDENT','Ученик'),
		('PARENT','Родитель'),
		('OTHER','Другое')
	]
	first_name = models.CharField(
		max_length=20, 
		verbose_name = 'Имя'
	)
	last_name = models.CharField(
		max_length=20, 
		verbose_name = 'Фамилия',
		blank=True
	)
	middle_name = models.CharField(
		max_length=20, 
		verbose_name = 'Отчество',
		blank=True
	)
	child= models.ForeignKey(
		"self", 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True,
		verbose_name = 'Ребенок'
	)
	status=models.CharField(
        max_length=10,
		choices=STAT,
		verbose_name = 'Тип',
        default='STUDENT',
		blank=True
    )
	description=models.TextField(
		verbose_name = 'Описание',
		blank=True
	)
	class Meta:
		managed = True
		verbose_name = 'Человек'
		verbose_name_plural = 'Люди'
	def __str__(self):
		fio=self.first_name+' '
		if (self.middle_name): fio+=self.middle_name+' '
		fio+=self.last_name
		return fio