import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

token = "vk1.a.k-lsJcjCkdjAieSEE7-MdmOIYVvVAZg12l0MA3L1WsHN75VGa2a5OZNd61DTw81dHsDvWQY-zK3Ksz5LNDzVODsGdGjOq3drfyVtTWEbtJSIIjivygXQboC5W19Xy6WxmpWQk0-7cWtfuzSplRDtGUa6fYpW6JODflzjVcPCm-YBwYanerhwHkCccu7tC99EQV5XAN7BOMl5JHWI6k8Bcw"
vk = vk_api.VkApi(token=token)
longpollus = VkLongPoll(vk)
api = vk.get_api()

admin_list = [610313330, 309970107, 597481421, 7617097]
option = 'False'

def write_msg(id, text, keyboard=None, wall=None):
	vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': get_random_id(), 'keyboard': keyboard, 'attachment':wall})

def admin_keyboard():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("📅Мероприятия", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_button("🏆Достижения", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_line()
	keyboard.add_button("👓Обзор", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_button("👤О нас", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_line()
	keyboard.add_button("Настройки", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
	return keyboard.get_keyboard()

def user_keyboard():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("📅Мероприятия", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_button("🏆Достижения", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_line()
	keyboard.add_button("👓Обзор", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	keyboard.add_button("👤О нас", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	return keyboard.get_keyboard()

def opt():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Добавить мероприятие", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
	keyboard.add_button("Добавить достижение", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
	keyboard.add_line()
	keyboard.add_button("Удалить мероприятие", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
	keyboard.add_button("Удалить достижение", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
	keyboard.add_line()
	keyboard.add_button("Выйти из настроек", color=vk_api.keyboard.VkKeyboardColor.SECONDARY)
	return keyboard.get_keyboard()
def yes():
	keyboard = vk_api.keyboard.VkKeyboard(one_time=True)
	keyboard.add_button("Да", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
	keyboard.add_button("Нет", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
	return keyboard.get_keyboard()

for event in longpollus.listen():    
	if event.type == VkEventType.MESSAGE_NEW:    
		if event.to_me:        
			if event.user_id in admin_list:
				menu_k = admin_keyboard()
			else:
				menu_k = user_keyboard()
			yesorno = yes()
			options= opt()
			request = event.text
			if option == 'True' and event.user_id in admin_list:
				if request == 'Добавить мероприятие':
					upload = vk_api.VkUpload(vk)
					photo = upload.photo_messages('exam.PNG')
					owner_id = photo[0]['owner_id']
					photo_id = photo[0]['id']
					access_key = photo[0]['access_key']
					attachment = f'photo{owner_id}_{photo_id}_{access_key}'
					write_msg(event.user_id, "Напишите сюда id записи сообщества, которое нужно переслать. Для этого нажмите на запись и скопируйте все после слова wall.",  wall=attachment)
					write_msg(event.user_id, "Например, 'wall-193344902_420'")
					option = 'AddE'
				elif request == 'Добавить достижение':
					upload = vk_api.VkUpload(vk)
					photo = upload.photo_messages('exam.PNG')
					owner_id = photo[0]['owner_id']
					photo_id = photo[0]['id']
					access_key = photo[0]['access_key']
					attachment = f'photo{owner_id}_{photo_id}_{access_key}'
					write_msg(event.user_id, "Напишите сюда id записи сообщества, которое нужно переслать. Для этого нажмите на запись и скопируйте все после слова wall.",  wall=attachment)
					write_msg(event.user_id, "Например, 'wall-193344902_420'")
					option = 'AddA'
				elif request == 'Удалить достижение':
					x = open('test.txt','r')
					achivs = x.readlines()
					x.close()
					if len(achivs) == 0:
						write_msg(event.user_id, "Достижения еще не добавлены.", keyboard=options)
					else:
						write_msg(event.user_id, None, wall=achivs[len(achivs)-1])
						write_msg(event.user_id, "Последняя добавленная запись будет удалена?", keyboard=yesorno)
						option = 'RemA'
				elif request == 'Удалить мероприятие':
					f = open('testf.txt','r')
					events = f.readlines()
					f.close()
					if events==[]:
						write_msg(event.user_id, "Мероприятия еще не добавлены.", keyboard=options)	
					else:	
						write_msg(event.user_id, None, wall=str(events[-1]))
						write_msg(event.user_id, "Последняя добавленная запись будет удалена?", keyboard=yesorno)
						option = 'RemE'
				elif request == 'Выйти из настроек':
					write_msg(event.user_id, "Меню настроек закрыто", keyboard=menu_k)
					option = 'False'
				else:
					write_msg(event.user_id, "Пожалуйста, нажмите на одну из кнопок.", keyboard=options)
			elif option == 'AddE' and event.user_id in admin_list:
				#events.append(request)
				f = open('testf.txt','a+')
				f.write(request + '\n')
				f.close()
				f = open('testf.txt','r')
				events = f.readlines()
				try:							
					write_msg(event.user_id, None, wall=events[-1])
					write_msg(event.user_id, "Мероприятие успешно добавлено.", keyboard=options)
					events.clear()
					option = 'True'
					f.close()
				except:
					f.close()
					f = open('testf.txt','w')
					for line in events:
						if line!=events[-1]:
							f.write(line)					
					write_msg(event.user_id, "Id записи написано неверно. Операция отменена.", keyboard=options)
					events.clear()
					option = 'True'
					f.close()
			elif option == 'AddA' and event.user_id in admin_list:	
					#achivs.append(request)
					x = open('test.txt','a+')
					x.write(request + '\n')
					x.close()
					x = open('test.txt','r')
					achivs = x.readlines()
					try:
						write_msg(event.user_id, None, wall=achivs[-1])
						write_msg(event.user_id, "Достижение успешно добавлено.", keyboard=options)
						achivs.clear()
						option = 'True'
						x.close()
					except:
						x.close()
						x = open('test.txt','w')
						for line in achivs:
							if line!=achivs[-1]:
								x.write(line)	
						write_msg(event.user_id, "Id записи написано неверно. Операция отменена.", keyboard=options)
						achivs.clear()
						option = 'True'
						x.close()
			elif option == 'RemA' and event.user_id in admin_list:
				x = open('test.txt','r')
				achivs = x.readlines()
				x.close()
				if request == 'Да':	
					x = open('test.txt','w')
					for line in achivs:
						if line!=achivs[-1]:
							x.write(line)
					write_msg(event.user_id, "Достижение успешно удалено", keyboard=options)
					achivs.clear()
					x.close()
					option = 'True'
				elif request == 'Нет':	
					write_msg(event.user_id, "Операция отменена", keyboard=options)
					achivs.clear()
					option = 'True'
				else:
					write_msg(event.user_id, "Нажмите на одну из кнопок.", keyboard=yesorno)
			elif option == 'RemE' and event.user_id in admin_list:
				f = open('testf.txt','r')
				events = f.readlines()
				f.close()
				if request == 'Да':	
					f = open('testf.txt','w')				
					for line in events:
						if line!=events[-1]:
							f.write(line)
					write_msg(event.user_id, "Мероприятие успешно удалено", keyboard=options)
					events.clear()
					option = 'True'
					f.close()
				elif request == 'Нет':	
					write_msg(event.user_id, "Операция отменена", keyboard=options)
					events.clear()
					option = 'True'
				else:
					write_msg(event.user_id, "Пожалуйста, нажмите на одну из кнопок.", keyboard=yesorno)
			else:	
				if request == 'Начать':
					user_get = api.users.get(user_ids=event.user_id)
					user_get = user_get[0]
					first_name = user_get['first_name']
					write_msg(event.user_id, "Приветствую 🖐🏻, " + first_name + ". Я - чат-бот музея школы №12! Рад знакомству 😉!", keyboard=menu_k)
				elif request == '👓Обзор':
					write_msg(event.user_id, "Вот видео-обзор школьного музея от нашего трудового коллектива. Обязательно посмотрите 😊!")
					write_msg(event.user_id, "https://vk.com/video-193344902_456239023", keyboard=menu_k)
				elif request == '👤О нас':
					write_msg(event.user_id, "Это школьный музей имени маршала Советского Союза К.К. Рокоссовского основан в 1995 году, в канун 50-летия Победы. \n\nПосетите наш сайт: \nhttps://museum.pskovedu.ru/#/view/91c37ddb-f701-42d6-bad1-7b13550621e4/exhibits\n\nКонтактный номер: +78115392780", keyboard=menu_k)
				elif request == '📅Мероприятия':
					f = open('testf.txt','r')
					events = f.readlines()
					f.close()
					if len(events) == 0:	
						write_msg(event.user_id, "У пока нас нет актуальных мероприятий.", keyboard=menu_k)	
					else:
						write_msg(event.user_id, "Это наши мероприятия:", keyboard=menu_k)
						for i in range(0,len(events)):   
							write_msg(event.user_id, None, keyboard=menu_k, wall=events[i])
				elif request == '🏆Достижения':
					x = open('test.txt','r')
					achivs = x.readlines()
					x.close()
					if len(achivs) == 0:	
						write_msg(event.user_id, "Наши достижения пока не добавили сюда.", keyboard=menu_k)
					else:
						write_msg(event.user_id, "Вот наши достижения:", keyboard=menu_k)	
						for i in range(0,len(achivs)):   					
							write_msg(event.user_id, None, keyboard=menu_k, wall=achivs[i])
				elif event.user_id in admin_list and request == 'Настройки':
					write_msg(event.user_id, "Меню отладки бота. Добавтье мероприятия и достижения, либо удалите их. (Доступно только аднимистраторам)", keyboard=options)
					option = 'True'
				else:
					write_msg(event.user_id, "Пожалуйста, нажмите на одну из кнопок.", keyboard=menu_k)