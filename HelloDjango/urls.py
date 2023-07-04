"""
URL configuration for HelloDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views
from formularze import views as form_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.hello),
    path("name/", views.name),
    path("losuj/", views.losowy_napis),
    path("losuj/<int:a>/<int:b>/", views.ll2),
    path("kosci/<int:ilosc>/<int:kosc>/", views.rzut),
    path("ll/", views.losuj),
    path("kosci/", views.kosci),
    path("lotek/", views.lottek),
    path('hello_form/', form_views.hello_formularz),
    path('kosci_form/', form_views.kosci),
    path('dane/', form_views.list_danych),
    path('osoba/<int:id>/', form_views.get_person),
    path('persons/', views.PersonView),
    path('delete/<int:id>/', form_views.del_person),
    path('add_person/', views.add_person_view),
    path('add_book/', views.add_book),
    path('show_books/', views.show_books),
]
