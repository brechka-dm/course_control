from django.shortcuts import render
from .models import *
from .forms import *
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .billing import *
def lessonsort(lesson):
	return int(lesson.number)
def billsort(bill):
	return int(bill.lesson.number)
def studentitemsort(studentitem):
	return int(studentitem.number)
def humanindexsort(human):
	return human.id
# Create your views here.
def start(request):
	courses=Course.objects.all()
	if (request.method=='POST'):
		r=str(request.POST)
		if r.find('editCourse+')>=0:
			cid=int(r[r.find('editCourse+')+11:r.find('^')])
			return HttpResponseRedirect(reverse('addCourse',args=(cid,)))
	return render(
        request,
        'start.html',
        context={'courses':courses},
    )
def showStudents(request,cid):
	cr=Course.objects.get(id=cid)
	dest=Distribution.objects.filter(course=cr)
	students=[]
	for d in dest: 
		students.append(d.student)
	return render(
		request,
		'show_students.html',
		context={'students':students, 'course':cr}
	)
def showStudentProgress(request, sid):
	std=Human.objects.get(id=sid)
	dest=Distribution.objects.filter(student=std)
	courses=[]
	for d in dest: 
		courses.append(d.course)
	lessons=Lesson.objects.filter(student=std)
	bills=Bill.objects.filter(agent=std)
	bl=[]
	for b in bills: 
		if b.lesson in lessons:
			bl.append(b.lesson)
	nbl=list(set(lessons).difference(set(bl)))
	nbl.sort(reverse=True, key=lessonsort)
	bills=list(bills)
	bills.sort(reverse=True, key=billsort)
	if (request.method== 'POST'):
		ps=str(request.POST)
		if ps.find('bill+')>0:
			fb=(ps.find('bill+'))
			lid=ps[ps.find('+')+1:]
			lid=int(lid[:lid.find('\'')])
			return HttpResponseRedirect(reverse('addBill',args=(sid,lid)))
		if ps.find('lessonDetail+')>0:
			l=(ps.find('lessonDetail+'))
			lid=ps[l+13:]
			lid=int(lid[:lid.find('^')])
			return HttpResponseRedirect(reverse('showLesson',args=(lid,)))
		if ps.find('pay+')>0:
			b=(ps.find('pay+'))
			bid=ps[b+4:]
			bid=int(bid[:bid.find('^')])
			bill=Bill.objects.get(id=bid)
			bill.status=True
			bill.save()
			return HttpResponseRedirect(reverse('showStudentProgress',args=(sid,)))
	return render(
		request,
		'show_student_progress.html',
		context={'student':std, 'courses':courses, 'bills':bills, 'nbl':nbl}
	)

'''def currentLesson(request, sid):
	std=Human.objects.get(id=sid)
	dest=Distribution.objects.filter(student=std)
	crs=dest[0].course
	now=datetime.datetime.now()
	plan=StudentItem.objects.filter(student=std)
	futureplan=[]
	for p in plan: 
		if not p.status: futureplan.append(p)
	inittheme=''
	initdescr=''
	if futureplan:
		inittheme=futureplan[0].item.caption
		initdescr=futureplan[0].item.description
	num=len(Lesson.objects.filter(student=std))+1
	if request.method== 'POST':
		if 'additem' in request.POST:
			itemid=request.POST['selected_theme']
			itemid=int(itemid[itemid.find('|')+2:])
			tm=Theme.objects.get(id=itemid)
			form=CurrentLessonForm(initial={
				'course':request.POST['course'],
				'date':request.POST['date'],
				'theme':tm.caption,
				'description':tm.description
		})
		if 'addlesson' in request.POST:
			form=CurrentLessonForm(request.POST)
			print(form)
			if form.is_valid():
				print(request.POST)
				ls=form.save(commit=False)
				ls.student=std
				ls.number=num
				ls.save()
				return HttpResponseRedirect(reverse('showStudentProgress', args=(sid,)))
	else:
		form=CurrentLessonForm(initial={
			'course':crs,
			'date':now,
			'theme':inittheme,
			'description':initdescr,
		})
	return render(
		request,
		'current_lesson.html',
		context={'student':std, 'form':form, 'plan':futureplan}
	)
	'''
def addStudent(request, sid):
	conts=''
	courses=''
	allcrs=''
	conttps=''
	if sid !=0:
		std=Human.objects.get(id=sid)
		conts=Contact.objects.filter(human=std)
		courses=Distribution.objects.filter(student=std)
		allcrs=Course.objects.all()
		conttps=ContactType.objects.all()
	if request.method== 'GET':
		if sid==0:
			form=AddStudentForm()
		else:
			form=AddStudentForm(instance=std)
	else:
		form=AddStudentForm(request.POST)
		if 'save' in request.POST:
			if form.is_valid(): 
				s=form.save()
				return HttpResponseRedirect(reverse('addStudent', args=(s.id,)))
		if 'selected_course' in request.POST:
			enroll=request.POST.getlist('selected_course')
			for e in enroll:
				cr=Course.objects.get(id=e)
				d=Distribution(student=std, course=cr)
				d.save()
		if 'addContact' in request.POST and request.POST['new_contact']:
			ct=int(request.POST['new_contact_type'])
			ct=ContactType.objects.get(id=ct)
			cn=request.POST['new_contact']
			nc=Contact(human=std,type=ct,contact=cn)
			nc.save()
		if 'delContact' in request.POST:
			cn=int(request.POST['delContact'])
			cn=Contact.objects.get(id=cn)
			cn.delete()
		return HttpResponseRedirect(reverse('addStudent', args=(sid,)))
#		print(form.errors)
#		print(form.non_field_errors)
	return render(request,'add_student.html',
		context={'form':form, 'courses':courses, 'contacts':conts, 'all_courses':allcrs, 'contact_types':conttps}
	)

def addBill(request,sid,lid):
	std=Human.objects.get(id=sid)
	conts=Contact.objects.filter(human=std)
	ls=Lesson.objects.get(id=lid)
	if request.method=='GET':
		sms=std.first_name+' '+std.last_name+'\n'
		sms+=str(ls.date.ctime())
		sms+='\nПожалуйста, добавьте эту строку в поле \"Сообщение для получателя\":\n'
		sms+=get_sms(std.id,ls.id)
		form=BillForm(initial={
			'agent':std, 
			'lesson':ls,
			'billingDate':datetime.datetime.now(),
		})
	else:
		form=BillForm(request.POST)
		r=str(request.POST)
		if r.find('send+')>=0:
			cid=int(r[r.find('send+')+5:r.find('^')])
			cont=Contact.objects.get(id=cid)
			cfunc=cont.type.id
			cont=cont.contact
		if r.find('make')>=0:
			sms=std.first_name+' '+std.last_name+'\n'
			sms+=str(ls.date.ctime())
			sms+='\nСумма:'+str(request.POST['ammount'])
			sms+='\nПожалуйста, добавьте эту строку в поле \"Сообщение для получателя\":\n'
			sms+=get_sms(std.id,ls.id)
			rd=''
			if 'status' in request.POST:
				rd=request.POST['billingDate']
			form=BillForm(initial={
				'agent':request.POST['agent'],
				'lesson':request.POST['lesson'],
				'billingDate':request.POST['billingDate'],
				'ammount':request.POST['ammount'],
				'receiptDate':rd,
				'text':sms
			})
		if r.find('close')>=0:
			form=BillForm(request.POST)
			if form.is_valid(): form.save();
			return HttpResponseRedirect(reverse('showStudentProgress', args=(sid,)))
	return render(request, 'bill.html', {'f': form,'contacts':conts})

def showLesson(request,lid):
	ls=Lesson.objects.get(id=lid)
	plan=StudentItem.objects.filter(student=ls.student.id)
	futureplan=[]
	for p in plan: 
		if not p.status: futureplan.append(p)
	inittheme=''
	initdescr=''
	if futureplan:
		inittheme=futureplan[0].item.caption
		initdescr=futureplan[0].item.description
	if request.method=='POST':
		form=CurrentLessonForm(request.POST,instance=ls)
		if 'additem' in request.POST:
			itemid=request.POST['selected_theme']
			itemid=int(itemid[itemid.find('|')+2:])
			tm=Theme.objects.get(id=itemid)
			form=CurrentLessonForm(initial={
				'course':request.POST['course'],
				'date':request.POST['date'],
				'theme':tm.caption,
				'description':tm.description,
				'student':ls.student,
				'number':ls.number
			})
			return render(request, 'lesson.html', {'f': form,'plan':futureplan})
		if form.is_valid(): 
			form.save()
			return HttpResponseRedirect(reverse('showStudentProgress',args=(ls.student.id,)))
	else:
		form=CurrentLessonForm(initial={
			'number':ls.number,
			'course':ls.course,
			'date':ls.date,
			'decription':ls.decription,
			'theme':ls.theme,
			'student':ls.student
		})
		return render(request, 'lesson.html', {'f': form,'plan':futureplan})

def showAllStudents(request):
	students=list(Human.objects.filter(status='STUDENT'))
	dst=Distribution.objects.all()
	stdl=[]
	for d in dst:
		if d.student not in stdl:
			stdl.append(d.student)
	if request.method=='POST':
		r=str(request.POST)
		if r.find('student+')>=0:
			sid=int(r[r.find('student+')+8:r.find('^')])
			return HttpResponseRedirect(reverse('addStudent',args=(sid,)))
		if 'plan' in request.POST:
			return HttpResponseRedirect(reverse('studentPlan',args=(request.POST['plan'],)))
	else:
		stdl.sort(key=humanindexsort,reverse=True)
	return render(
        request,
        'all_students.html',
        {'students':stdl}
    )
	
def addLesson(request,sid):
	std=Human.objects.get(id=sid)
	dest=Distribution.objects.filter(student=std)
	crs=dest[0].course
	now=datetime.datetime.now()
	num=len(Lesson.objects.filter(student=std))+1
	form=CurrentLessonForm()
	l=form.save(commit=False)
	l.course=crs
	l.date=now
	l.theme=''
	l.description=''
	l.student=std
	l.number=num
	l.save()
	return HttpResponseRedirect(reverse('showLesson',args=(l.id,)))

def addCourse(request, cid):
	if request.method=='GET':
		if cid==0:
			f=CourseForm()
		else:
			cr=Course.objects.get(id=cid)
			f=CourseForm(instance=cr)
	else:
		if cid!=0:
			cr=Course.objects.get(id=cid)
			f=CourseForm(request.POST,instance=cr)
		else: 
			f=CourseForm(request.POST)
		if f.is_valid:
			f.save()
			return HttpResponseRedirect(reverse('start'))
	return render(request, 'course.html',{'form':f})
	
def allPlans(request):
	crs=Course.objects.all()
	crs_plns=[]
	for c in crs:
		itms=Theme.objects.filter(course=c)
		#for i in itms:
		crs_plns.append([c,itms])
	if request.method=='POST':
		return HttpResponseRedirect(reverse('courseItem',args=(request.POST['addItem'],0)))
	return render(request, 'all_plans.html',{'course_plans':crs_plns})

def courseItem(request, cid,iid):
	if request.method=='GET':
		if cid!=0:
			c=Course.objects.get(id=cid)
			if iid!=0:
				t=Theme.objects.get(id=iid)
				f=ThemeForm(instance=t)
			else:
				f=ThemeForm(initial={'course':c})
	else:
		if 'addItem' in request.POST:
			if iid!=0:
				t=Theme.objects.get(id=iid)
				f=ThemeForm(request.POST,instance=t)
			else:
				f=ThemeForm(request.POST)
			if f.is_valid():
				f.save()
		if 'delItem' in request.POST:
			t=Theme.objects.get(id=iid)
			t.delete()
		return HttpResponseRedirect(reverse('allPlans'))
	return render(request, 'course_item.html',{'form':f})

def studentPlan(request, sid):
	s=Human.objects.get(id=sid)
	sp=list(StudentItem.objects.filter(student=s))
	sp.sort(key=studentitemsort)
	allp=Theme.objects.all()
	if request.method=='POST':
		if 'addItem' in request.POST and 'items_to_add' in request.POST:
			items=request.POST.getlist('items_to_add')
			for i in items:
				theme=Theme.objects.get(id=i)
				sitem=StudentItem(student=s,item=theme, status=False, number=0)
				sitem.save()
		if 'delItem' in request.POST:
			i=StudentItem.objects.get(id=request.POST['delItem'])
			i.delete()
		if 'save' in request.POST:
			return HttpResponseRedirect(reverse('showAllStudents'))
		return HttpResponseRedirect(reverse('studentPlan', args=(sid,)))
	return render(request, 'student_plan.html',{'student':s, 'plan':sp, 'all_items':allp})
	
def allBills(request):
	bills=Bill.objects.all().order_by('-id')
	#bills=[]
	#bills.append(Bill.objects.all())#.order_by('id'))
	if (request.method== 'POST'):
		if 'pay' in request.POST:
			bill=Bill.objects.get(id=request.POST['pay'])
			bill=Bill.objects.get(id=request.POST['pay'])
			bill.status=True
			bill.save()
			return HttpResponseRedirect(reverse('allBills'))
	#else:
	#	list(bills)
	#	bills.sort(key=billsort,reverse=True)
	
	return render(request, 'all_bills.html',{'bills':bills})