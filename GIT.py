"""Для первоначальной настройки"""
$ git config --global user.name "Ваше Имя" 
$ git config --global user.email "your_email@whatever.com"


"""перевести файл в статус "неотслеживаемый""""
$ git rm --cached <file> 


"""Клонирование репозитория git hub"""
$ git clone https://github.com/ваш-аккаунт-на-гитхабе/backend_test_homework


"""Изменение последнего коммита"""
# Для этого есть опция --amend (англ. amend, «исправить»):
git commit --amend -m "Текст вашего комментария".
# Эта команда добавит изменённые файлы в последний сделанный коммит,
# а с дополнительным флагом -m ещё и обновит комментарий:


"""Работа с историей"""
git log   
# покажет историю изменений - все закомиченные версии
git show HEAD
# детально покажет изменения в последней версии. Вместо HEAD можно
# поставить первые 7 символов кода, которые идет  в логе после слова commit
git reset 1234567
# откат к версии, где вместо этих цифр 7 символов кода, которые идет
# в логе после слова commit
git reset HEAD program.py
# откатили изменения до предыдушего коммита именно этого файла.
# Если без указания файла, откатится всё



"""vscode и gitignore """
# Добавить папку в игнор-лист гита 
# командой из корневой директории проекта (а можно дописать gitignore руками) 
echo '.vscode' >> .gitignore 


"""Удалить папку из списка отслеживаемых файлов (staging area) """
git rm -r --cached .vscode 


"""Добавить файл в гит """
git add .gitignore 


"""Основные команды для работы с ветками:"""
git branch <название_ветки>
# — создать новую ветку.
git checkout <название_ветки>
# — переключиться в ветку.
git checkout -b <название_ветки>
# — создать ветку и сразу переключиться в неё.
git branch -d <название_ветки>
# — удалить ветку. Чтобы всё прошло хорошо, нужно переключиться из удаляемой ветки.
git merge <название_ветки>
# — скопировать все изменения из ветки в ветку. Чтобы перенести изменения из ветки develop
# в ветку master, нужно находиться в ветке master и выполнить команду git merge develop.
