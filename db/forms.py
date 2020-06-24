from django import forms
from .models import *

class CurrentLessonForm(forms.ModelForm):
	class Meta:
		model=Lesson
		fields=['course','theme', 'date', 'decription', 'number','student']
		widgets={
			'number':forms.NumberInput(attrs={'class':'lesson-field'}),
			'student':forms.Select(attrs={'class':'lesson-field'}),
			'course':forms.Select(attrs={'class':'lesson-field'}),
			'theme':forms.TextInput(attrs={'class':'lesson-field'}),
			'date':forms.TextInput(attrs={'class':'lesson-field'}),
			'decription':forms.Textarea(attrs={'class':'lesson-discription'})
		}

class AddStudentForm(forms.ModelForm):
	class Meta:
		model=Human
		exclude=['child']
		widgets={
			'last_name':forms.TextInput(attrs={'class':'lesson-field'}),
			'first_name':forms.TextInput(attrs={'class':'lesson-field'}),
			'middle_name':forms.TextInput(attrs={'class':'lesson-field'}),
		}

class AddParentForm(forms.ModelForm):
	class Meta:
		model=Human
		exclude=[]

class BillForm(forms.ModelForm):
	class Meta:
		model=Bill
		exclude=[]
		widgets={
			'agent':forms.Select(attrs={'class':'lesson-field'}),
			'lesson':forms.Select(attrs={'class':'lesson-field'}),
			'ammount':forms.NumberInput(attrs={'class':'lesson-field'}),
			'billingDate':forms.TextInput(attrs={'class':'lesson-field'}),
			'receiptDate':forms.TextInput(attrs={'class':'lesson-field'}),
			'text':forms.Textarea(attrs={'class':'lesson-field'})
		}

class CourseForm(forms.ModelForm):
	class Meta:
		model=Course
		exclude=[]

class ThemeForm(forms.ModelForm):
	class Meta:
		model=Theme
		exclude=[]

class StudentItemForm(forms.ModelForm):
	class Meta:
		model=StudentItem
		exclude=[]