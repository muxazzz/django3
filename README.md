# django3

скачиваем и распаковываем архив
создаем вирт. окружение virtualenv django3-master      
активируем его source django3-master/bin/activate
устанавливаем след. пакеты:
pip3 install psycopg2-binary    
pip3 install django-crispy-forms
pip3 install pillow 
pip3 install django

проводим миграции
python3 manage.py makemigrations
python3 manage.py migrate

запускаем сервер
python3 manage.py runserver

далее заходим в админку
http://127.0.0.1:8000/admin/

логин
admin
password
15101988


проверяем работу на странице 
http://127.0.0.1:8000/index/
