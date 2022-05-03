"""Логирование через loggong"""
import logging

# уровни логирования
logging.debug('123')  # Когда нужна отладочная информация 
logging.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logging.warning('Большая нагрузка, хелп')  # Когда что-то идёт не так, но работает
logging.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logging.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо

# По умолчанию покажется только последние три строки. Для редактирования
# минимального уровня есть команда
logging.basicConfig(level=logging.DEBUG)

# формат вывода логов по умолчанию
УРОВЕНЬ ВАЖНОСТИ:текущий пользователь:сообщение 
# для изменения формата вывода логов есть команда:
logging.basicConfig(format='%(asctime)s, %(levelname)s, %(name)s, %(message)s')
# список атрибутов: https://docs.python.org/3/library/logging.html#logrecord-attributes


"""Cохранение логов в файл"""
from logging.handlers import RotatingFileHandler
logging.basicConfig(filename='main.log', filemode='w') 
# Значения параметра filemode:
# w — содержимое файла перезаписывается при каждом запуске программы;
# x — создать файл и записывать логи в него; если файл с таким именем уже
# существует — будет ошибка;
# a — дописывать новые логи в конец указанного файла.

# а тут настраиваем логгер для текущего файла .py. Если используется
# код ниже, то в basicConfig нужен только format
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000, backupCount=5)
logger.addHandler(handler) 

# чтобы логи выводились в терминал, при исполнении файла пишем:
tail -f main.log

# запись исключения в лог
try:
    42 / 0
except Exception as error:
    logging.error(error, exc_info=True) 