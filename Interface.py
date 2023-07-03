from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import community_token

vk = vk_api.VkApi(token=community_token)
longpoll = VkLongPoll(vk)

class BotInterface():
    def __init__(self, community_token):
        self.vk = vk_api.VkApi(token=community_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_tools = VKTools(access_token)
        self.params = {}
        self.worksheets = []
        self.offset = 0
    def message_send(user_id, message, attachment=None):
        self.vk.method('messages.send',
                  {'user_id': user_id,
                   'message': message,
                   'attachment': attachment,
                   'random_id': get_random_id()})

    def write_msg(user_id, message):
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })

    def event_handler(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                if event.text.lower() == 'привет':
                    self.params = self.vk_tools.get_profile_info(event.user_id)
                    self.message_send(event.user_id, f'Привет, {self.params["name"]}')

                    if self.params['dbate']==None:
                        self.message_send(event.user_id, 'Назовите свой возраст')
                        if event.text.isdigit():
                            info['id']['year'].get(event.text())
                        else:
                            self.message_send(event.user_id, 'Поиск без учета возраста')

                    self.message_send(event.user_id, 'Назовите ваши интересы')
                    a = event.text.lower()
                    interests_list = a.split(", ")
                    named_interests = []
                    named_interests.append(interests_list)

                    self.message_send(event.user_id, 'Выберете, что важнее: книги, музыка или интерес')
                    if event.text.lower() == 'книги':
                        if self.params['books'] == None:
                            self.message_send(event.user_id, 'Назовите любимую книгу')
                            event.text.lower()
                            info['id']['books'].get(event.text())
                    if event.text.lower() == 'музыка':
                        if self.params['music'] == None:
                            self.message_send(event.user_id, 'Назовите любимую песню')
                            event.text.lower()
                            info['id']['music'].get(event.text())
                    if event.text.lower() == 'музыка':
                        if self.params['interests'] == None:
                            self.message_send(event.user_id, 'Назовите любимую песню')
                            event.text.lower()
                            info['id']['music'].get(event.text())

                    mutual_interests_users


                   if self.params['interests'] == None:

                    # massiv sorted(key, функция, котора будет вызываться, чтобы оценить порядок эжлеентов, мы передаем свою функцию:
                    # цикл сравнения пользователя  list comprehensions: cycle for
                    #

                    if self.params['interest']==None:
                        self.message_send(event.user_id, 'Назовите свой главный интерес')
                            if event.text.lower():
                                info['id']['year'].get(event.text())
                            else:
                                self.message_send(event.user_id, 'Ошибка')
                elif event.text.lower() == 'поиск':
                    self.message_send(event.user_id, 'Начинаем поиск')

                    if self.worksheets:
                        worksheet = self.worksheets.pop()
                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}_photo['id'],'
                    else:
                        self.worksheets = self.vk_tools.search_worksheet(self.params, self.offset)
                        worksheet = self.worksheets.pop()
                        photos = self.vk_tools.get_photos(worksheet['id'])
                        photo_string= ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}_photo['id'],'
                        self.offset += 10

                    self.message_send(event.user_id, f'имя: {worksheet["name"]} ссылка: vk.com/{worksheet["id"]}', attachment=photo_string)

                elif event.text.lower() == "пока":
                    self.message_send(event.user_id, "До новых встреч!")
                else:
                    self.message_send(event.user_id, "Неизвестная команда")

if __name__=='__main__':
    bot_interface = BotInterface(community_token, access_token)
    bot_interface.event_handler()