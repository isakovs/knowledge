"""Хранение секретных данных"""
import os
from dotenv import load_dotenv
load_dotenv()


def other_function():    
    secret_token = os.getenv('TOKEN')
    # взяли переменную token из загруженного внешнего хранилища
    # шпионы печальны, шпионы ушли с пустыми руками
    response_post = requests.post('https://api.vk.com/method/users.get',
                                   data=secret_token)
# в файле .env в той же директории хранятся секретные ключи и значения.
# ЛИБО они предварительно загружены в глобальное пространство командой: 
# export token=123
# тогда файл создавать не нужно. Посмотреть данные переменных
# можно командой env в терминале


"""Django REST framework - организация АПИ и
встроенная авторизация по токену Authtoken
"""
pip install djangorestframework

# затем добавить приложение rest_framework в INSTALLED_APPS
# 'rest_framework'

# setiings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', 
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
} 

# Затем выполняем миграцию
# Затем заполняем маршрут в любом файле URL
from rest_framework.authtoken import views


urlpatterns = [

    ...

    path('api-token-auth/', views.obtain_auth_token),
] 

"""Способы аутентификации по токену"""
# Authtoken
# Установлен в Django REST framework


"""Пример сериаолизации данных из Питона в JSON"""

from datetime import datetime
from rest_framework import serializers
# Импорт класса, который конвертирует Python-словарь в JSON
from rest_framework.renderers import JSONRenderer


class Post():
    def __init__(self, author, text, pub_date=None):
        self.author = author
        self.text = text
        self.pub_date = pub_date or datetime.now()


# Создаём сериализатор, наследник предустановленного класса Serializer
class PostSerializer(serializers.Serializer):
    # Описываем поля и их типы
    author = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=5000)
    pub_date = serializers.DateTimeField()


# Создаём объект класса Post
post = Post(author='Робинзон Крузо', 
            text='23 ноября. Закончил работу над лопатой и корытом.',
            pub_date ='1659-11-23T18:02:33.123543Z'
            )

# Создаём экземпляр сериализатора PostSerializer
# Передаём в него объект класса Post
serializer = PostSerializer(post)

# serializer.data содержит Python-словарь:
# {'author': 'Робинзон Крузо', 'text': '23 ноября. Закончил работу над лопатой и корытом.', 'pub_date': '1659-11-23T18:02:33.123543Z'}

# Рендерим JSON из Python-словаря:
json_object = JSONRenderer().render(serializer.data)


"""При работе с моделями"""
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField("created", auto_now_add=True)

...

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # Указываем поля модели, с которыми будет работать сериализатор 
        # (поля модели, не указанные в этом списке, сериализатор будет игнорировать).
        # Для перечисления полей можно использовать список или кортеж.
        fields = ('id', 'post', 'author', 'text', 'created') 


"""Получить / отправить несколько объектов в сериализатор (many=True)"""
# Получаем все объекты модели
cats = Cat.objects.all()
# Передаём queryset в конструктор сериализатора
serializer = CatSerializer(cats, many=True)

# А из JSON в объект
serializer = CatSerializer(data=request.data, many=True) 

"""Обновление данных, когда из request получаем не все нужные поля (partial=True)"""
# без partial=True выдаст ошибку 400 Bad Request "This field is required."
serializer = CatSerializer(cat, data=request.data, partial=True)


"""Декаратор для определения типов запросов функции API"""
@api_view(['GET', 'POST'])

# пример функции и декоратора
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['GET', 'POST'])  # Разрешены только POST- и GET-запросы
def cat_list(request):
    # В случае POST-запроса добавим одну запись или список записей в БД
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # В случае GET-запроса возвращаем список всех котиков
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data) 


"""Аругмент partial=True, если в сериализатор переданы не все поля"""
serializer = CatSerializer(cat, data=request.data, partial=True) 