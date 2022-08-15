# My Django Blog

_A blog built by Django framework and has features such as comment system, star rating system, separate author and manager, hot articles, most visited articles (visit counting system), ...._

<br>

# Starting 🚀

_These instructions allow you to get a copy of the running project on your local machine._

## Pre-requisites 📋
_You need to have a 3.X version of Python_

## Installation 🔧

- Make a git clone or download it in zip
```bash
git clone https://github.com/irania9O/My-Django-Blog.git
```
- Get in the directory

```bash
cd My-Django-Blog
```

- Install from your terminal with pip requirements.txt:

```bash
pip install -r requirements.txt
```

- Create new migrations based on the changes you have made to your models:

```bash
python manage.py makemigrations
```

- Apply migrations:
```bash
python manage.py migrate
```

- To Create an admin user
```bash
python manage.py createsuperuser
```

<br>

# Start the development server 🧮:

```bash
python manage.py runserver
```
- Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. 
You should see the admin’s login screen and home page on your local domain – e.g., http://127.0.0.1:8000/.
<br>

# Screenshots
![home](./screenshots/home.jpg)
![article_detail](./screenshots/article_detail.jpg)
![comments](./screenshots/comments.jpg)
![profile](./screenshots/profile.jpg)
![article_list_admin](./screenshots/article_list_admin.jpg)
![add_article](./screenshots/add_article.jpg)

