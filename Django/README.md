1- **python -m pip install Django** = Django modüllerini yüklemek için kullanılır.
2-Terminalde cd (Change Directory) ile django_learning_project içerisine girin. cd django_learning_project
3- **django-admin startproject <projectName>** yazın ve bekleyin, Explorer kısmına dosyalar gelecektir. (Djamgonun çalışıp çalışmadığı kontrol edilir.)
4- **python manage.py migrate** (django_learning_project içerisinde olduğunuzdan emin olun.)
5- **python manage.py runserver** (Terminalde çıkan url ile çalışıp çalışmadığını kontrol edebilirsiniz.)
6- **python manage.py startapp first_app**
7- Sunucuya bağlandıktan sonra URL ile girişte hata verecektir. URL kısmında yazdığınız URL' slash koyup uygulama isminizi yazmanız gerekiyor.
http://127.0.0.1:8000/first_app 
8- URL kısmında boş bıraktığımız PATH kısmına about yazdığımıza:
9 -URL kısmında bulunan first_app kısmını firstapp/ yaptığımızda bir önceki madde geçersiz oluyor. Yazdıklarımı görmemiz için yazmamız gereken
http://127.0.0.1:8000/first_app/about

Model View Template = MVT
Model = Models
View = Views - Urls
Template = HTML - CSS - JavaScript

10- Debug modunu kapatmak için settings.py dosyaysına girip True olan değeri False yapın altında bulunan host kısmını "127.0.0.1" ya da hangi URL ile giriyorsanız onu yazın.
