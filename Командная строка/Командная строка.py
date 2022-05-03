ssh isakov@51.250.18.250  # статичесаий ip яндекс облако

"""Узнать параметры команды"""
from platform import mac_ver


man <название_команды>
<название_команды> --help # для Windows

"""Прочесть содержимое"""
cat logs/2019/12/apache_2019-12-01.txt

"""Пакетный менеджер APT"""
apt update  # обновление списка доступных пакетов
apt install <имя пакета>  # втоматическое скачивание и установка запрошенного пакета
apt upgrade <имя пакета>  # обновление пакета
apt remove <имя пакета>  # удаление пакета из системы

sudo apt update  # обновить индекс пакетов APT

"""Подготовка сервера к Django-проекту"""
# Менеджер пакетов pip
# Eтилиту для создания виртуального окружения venv;
# Cистему контроля версий git, чтобы клонировать ваш проект.
sudo apt install python3-pip python3-venv git -y


"""Подключение к серверу через терминал"""
# ssh имя_пользователя@хост -p порт 
ssh admin@84.201.161.196
# admin: имя пользователя, под которым будет выполнено подключение к серверу
# 84.201.161.196: ip-адрес сервера


"""сгенерировать SSH-ключ"""
ssh-keygen

"""Вывести созданный SSH-ключ в консоль"""
cat ~/.ssh/id_rsa.pub

"""Создать файл"""
touch file.txt

"""Удадить файл"""
rm file_folder/super_file.txt 

"""Копировать / Переместить"""
cp / mv 

"""увидеть состояние всех запущенных юнитов"""
sudo systemctl 

"""Запустить юнит"""
sudo systemctl start gunicorn

"""добавить юнит в список автозапуска операционной системы"""
sudo systemctl enable gunicorn  

"""проверить работоспособность демона"""
sudo systemctl status gunicorn 

"""управлять процессом под юнитом"""
sudo systemctl start/stop/restart

"""Запуск веб-сервера с WSGI"""
gunicorn --bind 0.0.0.0:8000 yatube.wsgi  # Перейдите в директорию с файлом manage.py и запустите Gunicorn

"""Установка NGINX сервера"""
sudo apt install nginx -y

"""Разрешить запросы по протоколам HTTP, HTTPS и SSH"""
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH 



"""
В операционной системе Ubuntu по умолчанию установлен файрвол ufw
"""

"""Включить Файрвол ufw"""
sudo ufw enable # !!! предварительно открыть доступ через файрвол по SSH
                # иначе после включение файрвола соединение оборвется и нельзя будет подключиться !!!

sudo ufw status # првоерить статус

"""Запуск NGINX"""
sudo systemctl start nginx


"""Перезапуск Unicorn"""
# Перезапустить все службы
sudo systemctl daemon-reload 
# Запустить демона gunicorn после перезапуска
sudo systemctl restart gunicorn
# Убедиться что gunicorn активен
sudo systemctl status gunicorn 


"""Создать группу пользователей Linux"""
sudo groupadd developer

"""Добавить в группу пользователей юзера"""
# Пользователь torvalds добавлен в группу разработчиков "developer"
sudo usermod -aG developer torvalds
"""
Команда usermod (англ. user modification — «изменение пользователя») управляет свойствами пользователя.
Ключ -G назначает пользователю новую группу,
Ключ -a (от англ. append — «добавлять») указывает, что новую группу надо добавить к списку тех групп, 
в которые уже включён пользователь. Без ключа -a прежние группы будут удалены и заменены на новую.

Будьте внимательны к регистру: ключ -g заменит главную группу пользователя (группу по умолчанию),
и пользователь может потерять доступ к своим файлам.
"""

"""Посмотреть список групп пользователя torvalds"""
groups torvalds


"""Ищменение прав доступа к файлу"""
chmod 444 strange_file.txt
# Чтобы рекурсивно изменить права доступа к директории
# (для всех вложенных файлов и папок), команду chmod выполняют с ключом -R

"""Изменить группу директории"""
chgrp developer /home/morty/yatube/ 

"""Изменить права по директоктории или файлу"""
chmod -R 775 /home/morty/yatube/

"""Создать пользователя:"""
sudo useradd van-rossum
# Изменить пароль для пользователя:
sudo passwd van-rossum


"""Права цифрами
0 — нет прав (соответствует ---);
1 — только выполнение (соответствует --x);
2 — только запись (соответствует -w-);
3 — запись и выполнение (соответствует -wx);
4 — только чтение (соответствует r--);
5 — чтение и выполнение (соответствует r-x);
6 — чтение и запись (соответствует rw-);
7 — все права (соответствует rwx).
"""

"""Вывести список процессов"""
ps -aux  # -aux добавит информацию, под каким пользтелем запущены процессы


"""Установка certbot"""
sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

"""Получение сертификата SSL"""
sudo certbot --nginx

"""Убедиться, что certbot обновляет SSL"""
sudo certbot renew --dry-run

"""Если обновление не происходит, поможет команда"""
sudo certbot renew --pre-hook "service nginx stop" --post-hook "service nginx start" 
# Эта команда обновит сертификат и перезапустит nginx.


"""Установка PostgreSQL"""
sudo apt update 
sudo apt install postgresql postgresql-contrib -y 

"""Проверить, что все работает - вернуть время"""
sudo -u postgres psql -c 'select now()'

"""Запустить psql от имени суперпользователя postgres"""
sudo -u postgres psql 

"""Служебные команды psql
\? # Справка по командам консольного клиента psql
\h # Справка по доступным командам SQL
\h <команда> # Справка по конкретной команде
\du # Список пользователей
\dt # Список таблиц 
"""

"""Подключение PostgreSQL к Django"""
# Установите в виртуальное окружение драйвер для работы с postgres
pip install psycopg2-binary==2.8.6 


"""Копирование файла с локалки на сервер"""
python manage.py dumpdata > dump.json  # на локалке
# Данные сохранятся в dump.json 
scp dump.json isakov@51.250.18.250:/home/isakov/hw05_final/yatube/


"""Перенос базы с SQLite на PostgreSQL"""
# Закинуть dump.json на сервер через scp и выполнить там

python3 manage.py shell  
# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

python manage.py loaddata dump.json


"""###############################################################"""
"""DOCKER"""
"""###############################################################"""

"""Быстрая установка на UBUNTU"""
# Установка утилиты для скачивания файлов
sudo apt install curl
# Эта команда скачает скрипт для установки докера
curl -fsSL https://get.docker.com -o get-docker.sh
# Эта команда запустит его
sh get-docker.sh


"""Запуск образа на новом месте"""
docker run <имя образа>

"""Просмотр и удаление"""
# Список образов/контейнеров на локалке
docker image ls
docker container ls

# Вызов справки по команде
docker container --help 

# Удалить контейнер
docker container rm <CONTAINER_ID>

"""Сборка образа"""
docker build -t yamdb .
# build — команда сборки образа по инструкциям из Dockerfile.
# -t yambd — ключ, который позволяет задать имя образу, а потом и само имя.
# . — точка в конце команды — путь до Dockerfile, на основе которого производится сборка.

"""Создание и запуск контейнера"""
docker run --name <имя контейнера> -it -p 8000:8000 yamdb 
# run — команда запуска нового контейнера.
# --name my_project — ключ, который позволяет задать имя контейнеру, и само имя.
# -it — комбинация этих ключей даёт возможность передавать в контейнер команды из вашего терминала.
# -p 8000:8000 — указывает публичный порт контейнера. Левая часть — внешний порт контейнера, правая — порт, на который будет перенаправлен запрос.
# yamdb — образ, из которого будет запущен контейнер.

"""Обычный запуск существующего контейнера"""
docker container start <CONTAINER ID>
docker container stop <CONTAINER ID> 

"""Открыть терминал контейнера"""
docker exec -it <CONTAINER ID> bash 

"""Посмотреть команды для образа докер"""
docker container 


"""########################"""
"""Связка нескольких контейнеров Docker-Compose"""
# В Dockerfile указываем запуск через Gunicorn или проделываем другие подготовительные процедуры
# Создаем файл docker-compose.yaml  -  на подобии Docker, но описывает взаимодействие нескольких контейнеров
# Запускаем всё командой
docker-compose up

"""ПЕРЕ сборка"""
docker-compose up -d --build 
# Для пересборки команда up выполняется с параметром --build.
# Чтобы логи не мешали управлять контейнерами через терминал, развёртывание
# контейнеров выполняется в «фоновом режиме»: для этого применяется ключ -d.


"""Логирование"""
"""Посмотреть логи"""
docker logs --follow <container_name> 
# Логи можно сохранить в файл командой docker logs
<container_name> > docker.log

# или найти в них нужную информацию
grep <поисковый-запрос>.


"""Првоерить потербляемые контейнерами ресурсы"""
docker stats 


"""Чистка места в Docker"""
# Показать статистику
docker system df 

# Все неактивные (остановленные) контейнеры удаляются командой 
docker container prune.

# Удалить "висячие" образы, которые не ссылаются контейнеры
docker image prune

# Удалить вообще всё, что не используется (неиспользуемые образы,
# остановленные контейнеры, тома, которые не использует
# ни один контейнер, билд-кеш)
docker system prune


"""Загрузка образа c/на DockerHub"""
# Локально создать образ с нужным названием и тегом:
docker build -t billglasses/gates:v2.11.1989 . 
# Авторизоваться через консоль:
docker login
# Загрузить образ на DockerHub:
docker push billglasses/gates:v2.11.1989

# Вытащить обновленную версию контейнера из DockerHub
docker pull <imagename>

# Удалить контейнеры определенного docker-compose, оставить только образы
docker-compose down -v


docker-compose exec web python manage.py dumpdata > fixtures.json 