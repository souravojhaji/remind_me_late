# remind_me_later
* first get the clone of project
* git clone https://github.com/souravojhaji/remind_me_later
* Instructions for run this project

* first create virtual environment and activate it

```
pip install python-dotenv
python -m venv venv
```

* for windows
```
.\venv\Scripts\activate
```

* for ubuntu
```
source venv/bin/activate
```

* for install requirements or depedencies
```
pip install -r requirements.txt
```
* for run this project
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* urls to save date, time and message 
```
url: http://127.0.0.1:8000/api/reminder-save/
```
