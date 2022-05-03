"""
Как работает Джанго

Данные проекта хранятся в БД.
Для взаимодействия с БД в коде создаются модели.
Пользователь обращается к какой-то странице сайта, Django сверяет запрошенный адрес с шаблонами адресов в файле urls.py.
Каждый шаблон адреса в urls.py связан с определённой функцией или классом, которые обрабатывают входящие данные. Такие функции (или классы) называются View.
View обращается к моделям и через них получает необходимые данные из БД. Эти данные View передает в шаблоны (Template).
Данные выводятся в шаблон и генерируется HTML-документ, который возвращается пользователю.
"""

"""Начало проекта

1. Создаем репозиторий на Гитхаб
2. Клонируем в папку
3. Устанавливаем виртуальное окружение
4. Устанавливаем Django
"""
# python3, обнови, пожалуйста, менеджер пакетов pip 
(venv)...$ python3 -m pip install --upgrade pip 
# Менеджер пакетов pip, поставь мне, пожалуйста, Django версии 2.2.19 
(venv)...$ pip install Django==2.2.19 # Нажимаем <enter>
"""
5. Настройка редактора VSC
Зайдите в настройки VSC: File (или Code на macOS) > Preferences > Settings. 
Переключитесь в режим настроек текущего проекта, на закладку Workspace. 
В строке поиска введите имя ключа конфигурации python.pythonPath и укажите значение:
Для Windows ./venv/Scripts/python.exe
Для macOS ./venv/bin/python или полный путь к python.exe
"""
# 6. Создаем проект
(venv)... $ django-admin startproject имя_проекта


"""Создание приложения"""
# Использовать в директории с manage.py. команду:
(venv)...$ python3 manage.py startapp ice_cream 
# startapp -- команда создания шаблона приложения 
# ice_cream -- название приложения
# или
django-admin startapp ice_cream
python3 -m django startapp ice_cream


"""Как задавать URL"""
urlpatterns = [
    path('/detail/<int:pk>/', views.details, name='detail'),
    path('/<str:username>/<int:id>/', views.article, name='article'),
]


"""Сделать VIEW функцию и подключить шаблон"""
# испортируем вот это
from django.shortcuts import render
# в конце функции конструкция такая
..return render(request, 'messages.html', context) 


"""Импорт простого ответа в браузер и view функции."""
from django.http import HttpResponse


"""Статика."""
# Команда для сбора статики проекта в одну директорию
collectstatic
# По этой команде Django проверит все директории проекта и скопирует в общую
# директорию содержимое всех папок с названием static, какие найдёт в проекте. 
# Если по каким-то причинам необходимо назвать папку со статикой иным именем — 
# адрес такой папки нужно зарегистрировать в переменной STATICFILES_DIRS в 
# yatube/settings.py

# Чтобы добавить ссылку на подгрузку файла в шаблон, необходимо загрузить 
# модуль для работы со статикой командой {% load static %}, а в адресах 
# подключаемых файлов применять тег 
# {% static "адрес_файла_относительно_директории_статики" %}:
{% load static %}
<script src="{% static "bootstrap/dist/js/bootstrap.js" %}"></script> 


"""Создать суперпользователя"""
(venv) $ python manage.py createsuperuser


"""Выполнение кода для Django через консоль"""
$ python manage.py shell


"""Модуль django.contrib.auth"""
from django.contrib.auth import views


"""Generic Views"""
Generic Views
# это встроенные в Django view-классы, созданные для решения стандартных
# задач. В переводе Generic Views — это «общий вид» или «базовое
# представление». Популярные Generic Views:
FormView
# обрабатывает формы на основе моделей.
TemplateView
# упрощает вывод данных в шаблон.
CreateView
# связывает модель и пользовательскую веб-форму, предназначенную
# для создания новой записи в базе.


"""Создание форм на основе моделей"""
# 1. Создаётся (или выбирается существующая) модель.
# 2. На основе модели создаётся класс формы.
# 3. Объект формы (экземпляр, созданный на основе класса формы)
# передаётся в специальный view-класс.
# 4. View-класс передаёт объект формы в шаблон, создаёт и возвращает
# пользователю страницу с веб-формой.
# 5. Для создания форм на основе моделей есть предустановленный
# класс ModelForm: от него можно наследовать классы для генерации форм.
# 6. Вот пример создания формы через ModelForm:
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


"""Создание формы обратной связи на отдельной странице"""
# 1. Создаем обычную модель с полями в файле с моделями
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField(min_value=1)

# ------ ИЛИ ------

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Введите имя')
    sender = forms.EmailField(label='Email для ответа')
    subject = forms.CharField(
        label='Тема сообщения', initial='Письмо администратору', max_length=100
    )
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(
        label='Отправить себе копию', required=False
    ) 

BooleanField
# соответствует типу bool. Виджет по умолчанию отрисовывает
# чекбокс <input type="checkbox">
CharField
# поле для ввода текста, по умолчанию используется виджет однострочного
# поля ввода <input type="text">. Виджет можно заменить: если указать в параметрах
# widget=forms.Textarea, будет отрисовано поле многострочного ввода, <textarea>
ChoiceField
# поле выбора из выпадающего списка, <select>
EmailField
# однострочное поле ввода текста, но с обязательной проверкой
# введённой строки на соответствие формату email
FileField
# поле для отправки файла, в шаблоне отрисует тег <input type="file">.
# Есть аналогичное поле для отправки только файлов изображений: ImageField
IntegerField
# поле для ввода чисел: <input type="number">


# 2. Создаем в файле forms содаем класс формы
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        # эта форма будет работать с моделью Book
        model = Book
        # на странице формы будут отображаться поля 'name', 'isbn' и `pages`
        fields = ['name', 'isbn', 'pages'] 

# 3. В файле views создаем класс для связи с формой и страницей
from django.views.generic import CreateView
from .forms import BookForm

class BookView(CreateView):
    form_class = BookForm
    success_url = "/thankyou"
    # куда переадресовать пользователя после успешной отправки формы
    template_name = 'new_book.html'

# 4. В HTML-шаблон передаётся переменная form:
# new_book.html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Отправить">
</form>
# as_p здесь означает обрамление в тег p
# можно использовать as_table или as_ul

# 5. Внести ссылку в урлы
urlpatterns = [
    # ...
    path('new_book/', views.BookView.as_view(), name='new_book')
]

"""Сделать подписи, поясняющий текст к полям формы"""
from django.utils.translation import ugettext_lazy as _

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

"""Декоратор @login_required импортируется из django.contrib.auth.decorators"""


"""Простое добавление формы в шаблон"""
  <form method="post" action="{% url 'signup' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Зарегистрироваться">
  </form>


"""Поджинатор: постраничный вывод элементов"""
from django.core.paginator import Paginator
# Создаём тестовый список объектов
items = ['Антон Чехов', 'Владимир Набоков', 'Лев Толстой', 'Марина Цветаева']

# Cоздаём объект Paginator(object_list, per_page),
# он принимает на вход список объектов 
# и число объектов, которое должно отображаться на одной странице.
# Передаём список items и задаём постраничное деление: по два объекта на страницу
p = Paginator(items, 2)

# Свойство count показывает, сколько объектов в последовательности
p.count
4

# Свойство num_pages показывает сколько страниц получится из списка
# num_pages рассчитывается как len(items)/per_page
p.num_pages
2

# Получаем объект с элементами для первой страницы
page1 = p.get_page(1)
page1
<Page 1 of 2>

# Получаем элементы для отображения на первой странице
page1.object_list
['Антон Чехов', 'Владимир Набоков']

# Проверяем, есть ли страницы после текущей
# и надо ли отображать кнопку "Следующая страница"
page1.has_next()
True
# Проверяем, есть ли страницы перед текущей
# и надо ли отображать кнопку "Предыдущая страница"
page1.has_previous()
False

page2 = p.get_page(2)
page2.object_list
['Лев Толстой', 'Марина Цветаева']

page2.has_next()
False
page2.has_previous()
True

# Чтобы отобразить список с номерами доступных страниц,
# получим значение свойства page_range:
# в нём хранятся данные типа range
type(p.page_range)
<class 'range'>
# выведем в консоль линейку с перечнем страниц
for n in p.page_range:
    print(f"<{n}> ", end="")
... 
<1> <2>

######################################################
# При запросе данных из базы тоже возвращается список 
# объектов, и работать с ним можно точно так же, как 
# со списком писателей из приведённого примера.

from posts.models import Post
posts = Paginator(Post.objects.order_by('-pub_date'), 2)
# В переменную post_page передадим объект второй страницы паджинатора
post_page = posts.get_page(2)
post_page.object_list
<QuerySet [<Post: 36>, <Post: 35>]>

post_page
# значение <Page 2 of 19>, тип django.core.paginator.Page
post_page.has_next()
# значение True, тип bool
post_page.has_previous()
# значение True, тип bool
post_page.has_other_pages()
# значение True, тип bool
post_page.next_page_number()
# значение 3, тип int
post_page.previous_page_number()
# значение 1, тип int
post_page.start_index()
# номер первого элемента на текущей странице. Отсчёт идёт
# от начала списка, начиная с 1. Значение: 3, тип: int
post_page.end_index()
# номер последнего элемента на текущей странице. Отсчёт 
# идёт от начала списка, начиная с 1. Значение: 4, тип: int


"""Статичные страницы через TemplateView"""
# views.py
from django.views.generic.base import TemplateView


class JustStaticPage(TemplateView):
    template_name = 'app_name/just_page.html'

    def get_context_data(self, **kwargs):
        """Функция для создание контекста. Она необязательна"""
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['just_title'] = 'Очень простая страница'
        context['just_text'] = 'На создание этой страницы у меня ушло пять минут! Ай да я.'
        return context


"""Проверка авторизации пользователей @login_required"""
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):

# Если незалогиненный пользователь обратится к странице, доступной только для авторизованных
# пользователей, то декоратор @login_required перенаправит его на страницу авторизации.
# Если пользователь авторизуется — он вернётся на ту страницу, с которой он пришёл. Адрес
# этой страницы будет передан в GET-параметре в переменной
# next : /auth/login?next=any-page-url

# дальше можно работать с этим в шаблоне:
{% if next %}
<div class="alert alert-info" role="alert">
    Вы обратились к странице, доступ к которой возможен
    только для залогиненных пользователей.<br>
    Пожалуйста, авторизуйтесь.
</div>
{% else %}
<div class="alert alert-info" role="alert">
    Пожалуйста, авторизуйтесь.
</div>
{% endif %}

"""Отображение заполненной формы из модели"""
def user_contact(request):
    ...
    # запрашиваем объект модели Contact
    contact = Contact.objects.get(pk=3)

    # создаём объект формы и передаём в него объект модели с pk=3
    form = ContactForm(instance=contact)

    # передаём эту форму в HTML-шаблон
    return render(request, 'contact.html', {'form': form})


"""Ограничение функции по типу запроса. Декоратор"""
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])


"""Тесты Unittest в Django"""
# Каждый логический набор тестов — это класс, 
# который наследуется от базового класса TestCase
from django.test import TestCase


class Test(TestCase):
    def test_example(self):
    # пишем тест тут
    ... 

# Для создания программного клиента - в модуле 
django.test
# есть класс
Client()

"""Информация из Response при тестировании"""
response = guest_client.get('/')

response.status_code  # код 200

status_code  # содержит код ответа запрошенного адреса;
client  # объект клиента, который использовался для обращения;
content  # данные ответа в виде строки байтов;
context  # словарь переменных, переданный для отрисовки 
# шаблона при вызове функции render();
request  # объект request, первый параметр view-функции, 
# обработавшей запрос;
templates  # перечень шаблонов, вызванных для отрисовки 
# запрошенной страницы;
resolver_match  # специальный объект, соответствующий 
# path() из списка urlpatterns.

##################################################
#  Создаем в ORM объект модели и тестируем его
class TaskModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаём тестовую запись в БД
        # и сохраняем ее в качестве переменной класса                
        cls.task = Task.objects.create(
            title='Заголовок тестовой задачи',
            text='Тестовый текст',
            slug='test-task'
        )

    def test_title_label(self):
        """verbose_name поля title совпадает с ожидаемым."""
        task = TaskModelTest.task
        # Получаем из свойста класса Task значение verbose_name для title
        verbose = task._meta.get_field('title').verbose_name
        self.assertEqual(verbose, 'Заголовок')

# Если в тестах Django вы применяете методы класса setUpClass() и
# tearDownClass() — обязательно вызывайте в них super(): super().setUpClass()
# и super().tearDownClass().

# к объектам, созданным в методах класса (таких как setUpClass()),
# синтаксически правильно обращаться через имя класса, а не через self.

# Правильно:
StaticURLTests.guest_client.get(...)
# Неправильно:
self.guest_client.get(...)
# (так тоже будет работать, но возможны неприятные сюрпризы).


"""Тестирование с помощью subTest"""
from django.test import TestCase
from deals.models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаём тестовую запись в БД
        # и сохраняем созданную запись в качестве переменной класса
        cls.task = Task.objects.create(
            title='Заголовок тестовой задачи',
            text='Тестовый текст',
            slug='test-task'
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        task = TaskModelTest.task
        field_verboses = {
            'title': 'Заголовок',
            'text': 'Текст',
            'slug': 'Адрес для страницы с задачей',
            'image': 'Картинка',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)


"""Тестирование на код 200 и вызов ожидаемого шаблона"""
from django.test import TestCase, Client


class StaticPagesURLTests(TestCase):
    def setUp(self):
        # Создаем неавторизованый клиент
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности адреса /page/about/."""
        response = self.guest_client.get('/page/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_uses_correct_template(self):
        """Проверка шаблона для адреса /page/about/."""
        response = self.guest_client.get('/page/about/')
        self.assertTemplateUsed(response, 'static_pages/about.html') 


#########################################################
# создаем авторизованного пользователя
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='AndreyG')
        # Создаем второй клиент
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login(self.user)

# Проверяем редиректы для неавторизованного пользователя
    def test_task_list_url_redirect_anonymous_on_admin_login(self):
        """Страница по адресу /task/ перенаправит анонимного
        пользователя на страницу логина.
        """
        response = self.guest_client.get('/task/', follow=True)
        self.assertRedirects(
            response, '/admin/login/?next=/task/')

    def test_task_detail_url_redirect_anonymous_on_admin_login(self):
        """Страница по адресу /task/test-slug/ перенаправит анонимного
        пользователя на страницу логина.
        """
        response = self.guest_client.get('/task/test-slug/', follow=True)
        self.assertRedirects(
            response, ('/admin/login/?next=/task/test-slug/')) 


"""Запуск тестов"""
# Выборочно
python3 manage.py test posts.tests.test_urls.StaticURLTests.test_homepage
# Все тесты
python3 manage.py test

"""Проверить процент покрытия тестами. Coverage"""
$ coverage run --source='posts,users' manage.py test -v 2
# == Для получения большей детализации установите для параметра
# verbosity значение 2.
# == Параметр -source='posts,users' (без пробела около запятой)
# ограничит проверку coverage модулями posts и users.
# == Параметр --source='.' запустит проверку coverage всех модулей
# в текущей директории (символ «точка» означает текущую директорию)
# и в её субдиректориях.
# == Если параметр --source не указывать — будет проверено покрытие
# тестами всех модулей проекта, включая /venv. В результате в отчёт
# будет выведена масса ненужной информации. Лучше явно указывать в
# параметре --source те модули или директории, которые нужно проверить.


"""Вывести отчет о покрытии. Coverage"""
coverage report  # в консоли
coverage html  # сформировать в html в папке htmlcov/


"""Модуль shutil"""
import shutil
# библиотека Python с прекрасными инструментами"
# для управления файлами и директориями:
# создание, удаление, копирование, перемещение, изменение папок|файлов
# Метод shutil.rmtree удаляет директорию и всё её содержимое
shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)


"""Установка django-debug-toolbar. DjDT."""
(venv) $ pip install django-debug-toolbar 
# Инструмент будет работать только в режиме разработки.
# Ниже код settings.py
DEBUG = True
# Добавьте новое приложение в 
INSTALLED_APPS = [
    # Это приложение необходимо для работы
    "django.contrib.staticfiles",
    # ...
    "debug_toolbar",
]
# Добавьте новое приложения для обработки запросов
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
# Добавьте IP адреса при обращении с которых будет доступен инструмент
INTERNAL_IPS = [
    "127.0.0.1",
]

# основной файд urls.py
from django.conf import settings

# У вас уже есть это условие
if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),) 


"""Хранение паролей"""
# 0. Устанавливаем утилиту для хранение паролей: 
pip install python-dotenv 
# 1. Создаем файл .env в корне проекта, там же где .gitignore
# Пишем там просто ключ=значение
DB_ENGINE=django.db.backends.postgresql
# 2. В нужном месте кода вставляем ссылку на ключ:
'ENGINE': os.getenv('DB_ENGINE')
# в месте, где запрашиваем пароли, вставляем вот че: 
from dotenv import load_dotenv
load_dotenv()