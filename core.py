from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import community_token

vk = vk_api.VkApi(token=community_token)
longpoll = VkLongPoll(vk)

class VKTools:
    def __init__(self, access_token):
        self.vkapi = vk_api.VKApi(token=access_token)

    def _bdate_toyear(self, bdate):
        user_year = bdate.split('.')[2]
        now = datetime.now().year
        return now - int(user_year)
    def get_profile_info(user_id):
         try:
            info, = vkapi.method('users.get',
                                 {'users_id': user_id,
                                  'fields': 'city,sex,bdate,relation,books,interests,music,groups'})
        except ApiError as e:
            info = {}
            print(f'error = {e}')

        result = [{'name': (info['first_name']+' '+info['last_name']) if 'first_name' in info and 'last_name' in info else None,
                  'sex': info.get('sex'),
                  'city': info.get('city')['title'] if info.get('city') is not None else None,
                  'year': self._bdate_toyear(info.get('bdate')),
                  'relation': info.get('relation'),
                  'books': info.get('books'),
                  'interests': info.get('interests') if info.get('interests') is not None else None,
                  'music': info.get('music') if info.get('music') is not None else None,
                  'groups': info.get('groups') if info.get('groups') is not None else None,
                 }]
        return result

    def search_worksheet(self, params):
        try:
            users = self.vkapi.method('users.search',
                                        {'count': 100,
                                         'hometown': params['city'],
                                         'sex': 1 if params['sex'] == 2 else 2,
                                         'has_photo': True,
                                         'age_from': params['year']-3,
                                         'age_to': params['year']+3
                                         })

        except ApiError as e:
            users = []
            print(f'error = {e}')
        return users

    def sort_by_interests(users, named_interests):
        try:
            interesting_users = []
            for interest in named_interests:
                for user in users:
                    common_interests = filter(lambda x: (interest == users[user]['interests'][x]), users[user]['interests'])
                    common_music = filter(lambda x: (interest == users[user]['music'][x]), users[user]['music'])
                    common_book = filter(lambda x: (interest == users[user]['books'][x]), users[user]['books'])
                    common_interests = common_interests + common_music + common_book
                    if len(common_interests)>0:
                        interesting_users.append(users[user]['id'])

        except ApiError as e:
            interesting_users = {}
            print(f'error = {e}')
        interesting_users_result = [{'name': item['first_name']+' '+item['last_name'],
                                     'id': item['id']} for item in users['items'] if item['is_closed'] is false for id in interesting_users if id==item['id'] ]
        return interesting_users_result

    def get_photos(self, id, interesting_users):
        global photos
        try:
            photos = self.vkapi.method('photos.get',
                                      {'owner_id': id,
                                       'album_id': 'profile',
                                       'extended': 1,
                                       })
        except ApiError as e:
            photos = {}
            print(f'error = {e}')

        result = [{'owner_id': item['owner_id'],
        'id': item['id'],
        'likes': item['likes']['count'],
        'comments': item['comments']['count']} for item in photos['item']
        ]
        return photos, result
#id phpto like-dislike  attribute
if __name__=='__main__'
    user_id = 15206350
    tools = VKTools(access_token)
    params = tools.get_profile_info(user_id)
    worksheet = tools.search_worksheet(params)
    worksheets = worksheet.pop()        #показывает последний элемент списка и удаляет его из списка
    interesting_users = worksheet.sort_by_interests(user_id, users, named_interests)
    for
        photos = tools.get_photos(interesting_users['id'])
        photo_like = tools.likes.add(photos)
        photo_dislike = tools.likes.delete(photos)
    pprint(photos)