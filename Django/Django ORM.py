"""Типы полей в БД"""
TextField # поле для хранения произвольного текста;
DateTimeField 
# поле для хранения даты и времени. Существуют похожие типы: для хранения даты
# DateField, промежутка времени DurationField, и просто времени TimeField;
ForeignKey # поле, в котором указывается ссылка на другую модель
BooleanField # поле для хранения данных типа bool;
EmailField
# поле для хранения строки, но с обязательной проверкой синтаксиса email;
FileField 
# поле для хранения файлов. Есть сходный, но более специализированный
# тип ImageField, предназначенный для хранения файлов картинок.


"""Вараинты on_delete в поле foreign_key в полях моделей"""
CASCADE: 
# при удалении объекта, на который есть ссылка, также удалите объекты, 
# на которые есть ссылки (например, при удалении сообщения в блоге вы также 
# можете удалить комментарии). Эквивалент SQL: CASCADE.
PROTECT:
#запретить удаление объекта. Чтобы удалить его, вам придется удалить все 
# объекты, которые ссылаются на него вручную. Эквивалентом SQL: RESTRICT.
SET_NULL: 
# установите ссылку на NULL (требуется, чтобы поле было nullable). Например, 
# когда вы удаляете пользователя, вы можете сохранить комментарии, которые 
# он опубликовал в блогах, но сказать, что он был опубликован анонимным 
# (или удаленным) пользователем. Эквивалентом SQL: SET NULL.
SET_DEFAULT: 
# установить значение по умолчанию. Эквивалентом SQL: SET DEFAULT.
SET(...): 
# установить заданное значение. Это не является частью стандарта SQL и 
# полностью обрабатывается Django.
DO_NOTHING: 
# вероятно, очень плохая идея, так как это создаст проблемы с целостностью 
# в вашей базе данных (ссылаясь на объект, который на самом деле не существует). 
# Эквивалентом SQL: NO ACTION.


"""
Рассказать Джанго о новых приложениях, чтобы он создал скрипты миграции. 
Потом можно сделать миграции
"""
(venv) $ python3 manage.py makemigrations 
# >>> Migrations for 'posts': posts/migrations/0001_initial.py 
# >>> - Create model Post


"""Запустить миграции"""
(venv) $ python3 manage.py migrate


"""Запрос к базе на вывод последних новостей."""
def index(request):
    # одна строка вместо тысячи слов на SQL
    latest = Post.objects.order_by('-pub_date')[:10]
    # если к модели привязаны другие модели через related_name
    # то можно <имя модели>.<имя related name>.objects.all()
    # собираем тексты постов в один, разделяя новой строкой
    # минус перед -pub_date указывает на обратную сортировку
    output = []
    for item in latest:
        output.append(item.text)
    return HttpResponse('\n'.join(output))
# Вот ещё несколько примеров, как можно получить данные из базы:
Post.objects.all() # получить все записи модели Post
Post.objects.get(id=1) 
# получить запись модели Post, у которой значение поля id
# равно 1. Поскольку поле id — это первичный ключ, а Django автоматически
# создаёт у модели свойство pk, то альтернативная запись этого же запроса
# будет такой: Post.objects.get(pk=1).
.count()
# метод считает количество строк


"""Фильтры"""
# Это шаблон, где text - это название поля, а __contains фильтр
Post.objects.filter(text__contains='again')
##############################################################
Post.objects.filter(pub_date__year=1854)
# запрос вернёт объекты, у которых значение года в поле pub_date равно 1854.
# Обратите внимание на синтаксис фильтрации: двойное нижнее подчёркивание
# между названиями поля и фильтра. Подробнее о функции filter()
#  — в документации.
Post.objects.filter(text__startswith="Писать не хочется")
# пример фильтра по текстовому полю, он вернёт записи, начинающиеся
# с указанной в фильтре строки.
__contains
# содрежит в значении
__exact
# точное совпадение. «Найти пост, где поле id точно равно 1»
__in
Post.objects.filter(id__in=[1, 3, 4])
# вхождение в множество. «Найти пост, где значение поля id точно равно 
# одному из значений: 1, 3 или 4»
__gt # > (больше),
__gte # => (больше или равно),
__lt # < (меньше),
__lte # <= (меньше или равно).
__range # в диапазоне
Post.objects.filter(pub_date__date=datetime.date(1890, 1, 1))
# дата равна
Post.objects.filter(pub_date__date__lt=datetime.date(1895, 1, 1))
# дата меньше (less than). lte <=, gte >=, gt >


"""Метод aggregate()"""
from django.db.models import Avg, Count, Max, Min, Sum
Post.objects.aggregate(Max("id"))
# Метод aggregate() применяет агрегирующие функции к определённой 
# выборке или ко всей таблице.
# В Django есть несколько агрегирующих функций, вот самые 
# популярные из них:
Avg:  # вернёт среднее значение по указанной колонке в выборке
Count:
# вернёт количество записей в выборке, как и метод count(), описанный выше
Max:  # вернёт максимальное значение по указанной колонке в выборке
Min:  # вернёт минимальное значение по указанной колонке в выборке
Sum:  # вернёт сумму значений по указанной колонке в выборке


"""Метод annotate()"""
# Достать из модели User все объекты,
# создать свойство posts_count и записать в него число постов, связанных с автором.
# posts — это свойство модели User, менеджер объектов
annotated_results = User.objects.annotate(posts_count = Count('posts'))
#  перебрать в цикле список пользователей annotated_results 
#  и для каждого объекта вывести свойство name
#  и новое свойство posts_count, которое хранит число постов пользователя
for item in annotated_results:
    print(f'Постов у пользователя {item.username}: {item.posts_count}')


"""Регистрация модели в админке в файле admin.py"""
from django.contrib import admin

from .models import Post   
# импортируем нашу модель, которую поставим
# в админку


class PostAdmin(admin.ModelAdmin):
   # перечисляем поля, которые должны отображаться в админке
   list_display = ("text", "pub_date", "author")
   # добавляем интерфейс для поиска по тексту постов
   search_fields = ("text",)
   # добавляем возможность фильтрации по дате
   list_filter = ("pub_date",)
   empty_value_display = "-пусто-" # это свойство сработает для всех колонок:
   где пусто - там будет эта строка
# при регистрации модели Post источником конфигурации для неё назначаем класс
# PostAdmin
admin.site.register(Post, PostAdmin)  


"""Два способа загрузки связанных записей."""
select_related(relation)
# загрузка связанных данных с помощью JOIN. В результате обработки получается
# один запрос, который, помимо основной модели, загружает и связанные данные
# из дополнительных таблиц.
prefetch_related(relation)
# «ленивая» подгрузка связанных данных с помощью дополнительных запросов.
# В этом случае Django ORM сперва запрашивает данные из основной таблицы,
# запоминает первичные ключи связанных записей, а затем делает ещё один
# запрос для загрузки связанных данных, ключи которых есть в первой выборке.


"""Создания формы через ModelForm"""
from django.db import models
from django.forms import ModelForm
    
    
# создадим модель, в которой будем хранить данные формы
class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField(min_value=1)
    
    
class BookForm(ModelForm):
    class Meta:
        # эта форма будет работать с моделью Book
        model = Book
        # на странице формы будут отображаться поля 'name', 'isbn' и `pages`
        fields = ['name', 'isbn', 'pages'] 


"""Импорт модель User"""
from django.contrib.auth import get_user_model
User = get_user_model()


"""Преобразовать название в URL. slugify"""
# pip3 install pytils не забыть установить!
# без этого не будет работать с кириллицей
from pytils.translit import slugify

class Task(models.Model):
    # какте-то модели
    
    def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)[:100]
    super().save(*args, **kwargs)

"""Обновление объектов из базы данных"""
Model.refresh_from_db(using=None, fields=None, **kwargs)¶