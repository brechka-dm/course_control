from collections import defaultdict
from .models import ContactType
def whatsapp_f(contact,sms):
	print (sms)
selector = defaultdict(lambda: 'неизвестно',
                       {'1': 'ВКонтакте',
                        '2': 'Телефон',
                        '3': 'Discord',
                        '4': 'Skype',
						'5': 'E-mail',
						'6': whatsapp_f,
						'7': 'Одноклассники',
						'8': 'Viber'
						})

def get_selector():
	ct=ContactType.obgects.all()
	selector={}
	for t in ct:
		selector.append(ct.id,ct,function)
	print (selector)
	return 1
def get_sms(sid,lid):
	return '#'+str(sid)+'.'+str(lid)+'#'
def send_sms(func,contact,sms):
	try:
		selector[str(func)](contact,sms)
	except KeyError as e:
		print(e)
	return