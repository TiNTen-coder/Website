from requests import get, post, delete

#print(get('http://localhost:5000/api/news').json())

#print(get('http://localhost:5000/api/news/1').json())

#print(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

#print(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())

#print(get('http://localhost:5000/api/news').json())



# newses = get('http://localhost:5000/api/news').json()
# for ns in newses["news"]:
#     print(ns)

#print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

# print(delete('http://localhost:5000/api/news/5').json())
#
# print("============================================================")
#
# newses = get('http://localhost:5000/api/news').json()
# for ns in newses["news"]:
#     print(ns)

newses = get('http://localhost:5000/api/v2/news').json()
for ns in newses["news"]:
    print(ns)

print(post('http://localhost:5000/api/v2/news',
           json={'title': 'Заголовок API V2',
                 'content': 'API V2 Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

newses = get('http://localhost:5000/api/v2/news').json()
for ns in newses["news"]:
    print(ns)