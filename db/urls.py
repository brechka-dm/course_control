from django.urls import path
from . import views


urlpatterns = [
	path('', views.start, name='start'),
	path('students/<int:cid>/', views.showStudents, name='showStudents'),
	path('student_progress/<int:sid>/', views.showStudentProgress, name='showStudentProgress'),
	path('lesson/<int:sid>/', views.addLesson, name='addLesson'),
	path('add_student/<int:sid>/', views.addStudent, name='addStudent'),
	path('bill/<int:sid>/<int:lid>', views.addBill, name='addBill'),
	path('lesson/<int:lid>', views.showLesson, name='showLesson'),
	path('all_students', views.showAllStudents, name='showAllStudents'),
	path('course/<int:cid>', views.addCourse, name = 'addCourse'),
	path('all_plans', views.allPlans, name = 'allPlans'),
	path('course_item/<int:cid>/<int:iid>', views.courseItem, name = 'courseItem'),
	path('student_plan/<int:sid>', views.studentPlan, name = 'studentPlan'),
	path('all_bills', views.allBills, name = 'allBills'),
]