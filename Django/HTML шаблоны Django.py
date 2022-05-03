"""Фильтры в HTML-шаблонах."""
# выполняет HTML теги из VIEW функции
safe 
# выведет количество символов из переданного значения
length
# заменяет символы перевода строки \n на HTML-теги <br>.
linebreaksbr
# работает только с объектами типа date и datetime: он форматирует дату по маске.
date
{{ pub_date|date:"j.m.Y" }} {# выведет 2.02.2020 #} 
{{ pub_date|date:"j F Y" }} {# выведет 2 февраля 2020 #}
{{ pub_date|date:"d.m.y" }} {# выведет 02.02.20 #}
{{ pub_date|date:"d M Y" }} {# выведет 02 фев 2020 #} 
# преобразует регистр букв в формат «каждое слово с заглавной» 
title
# обрежет текст до первых четырёх слов
truncatewords:4


"""Циклы в HTML-шаблонах."""
for
{% for key, value in dict_data.items %}
  Ключ '{{ key }}': Значение '{{ value }}'
{% endfor %} 
# Помимо обычных переменных в циклах создаются и вспомогательные, 
# они доступны в специальной переменной forloop:
forloop.counter — текущий счетчик выполнений цикла, начинается с 1;
forloop.counter0 — текущий счетчик выполнения цикла, начинается с 0;
forloop.revcounter — сколько итераций осталось до конца цикла, начинается с 1;
forloop.revcounter0 — сколько итераций осталось до конца цикла, начинается с 0;
forloop.first — вернёт True на первой итерации цикла, в остальных случаях вернёт False;
forloop.last — вернёт True на последней итерации цикла, в остальных случаях вернёт False;
forloop.parentloop — если цикл был запущен внутри другого цикла, то в этой переменной находится переменная forloop родительского цикла.
# Необязательный тег {% empty %}, вложенный в for, сработает, если переданный в цикл список пуст:
<ul>
  {% for news in news_list %}
    <li>{{ news.title }}</li>
  {% empty %}
    <li>Список новостей пуст.</li>
  {% endfor %}
</ul> 

# Вложенный в for тег {% ifchanged %} запоминает значение переданных параметров или своего тела
# между запусками цикла, — и если они не поменялись, скрывает его.
# В этом листинге HTML-заголовок <h2> с названием месяца будет выводиться на страницу только 
# если в предыдущей итерации цикла название месяца было другим.
<h1>Архив новостей за {{ year }}</h1>

{% for news in news_items %}
  {% ifchanged %}
    <h2>{{ news.pub_date|date:"F" }}</h2>
  {% endifchanged %}

  <h3>{{ news.pub_date|date:"d.m.Y" }} | {{ news.title}}</h3>
{% endfor %} 