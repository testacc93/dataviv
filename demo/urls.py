"""dataviv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from demo import views
from rest_framework.urlpatterns import  format_suffix_patterns

# from webapp import views
urlpatterns = [
    path('populationtotal/<cityname>', views.Total_pop.as_view()),
    path('populationmale/<cityname>', views.Male_pop.as_view()),
    path('populationfemale/<cityname>', views.Female_pop.as_view()),
    path('0-6populationtotal/<cityname>', views.Zero_to_six_populationtotal.as_view()),
    path('0-6populationmale/<cityname>', views.Zero_to_six_malepopulationtotal.as_view()),
    path('0-6populationfemale/<cityname>', views.Zero_to_six_femalepopulationtotal.as_view()),
    path('literatestotal/<cityname>', views.Literatestotal.as_view()),
    path('literatesmale/<cityname>', views.Maleliteratestotal.as_view()),
    path('literatesfemale/<cityname>', views.Femaleliteratestotal.as_view()),
    path('sexratio/<cityname>', views.Sexratio.as_view()),
    path('childsexratio/<cityname>', views.Childsexratio.as_view()),
    path('effectiveliteracyratetotal/<cityname>', views.Effectiveliteracyratetotal.as_view()),
    path('effectiveliteracyratemale/<cityname>', views.Effectiveliteracyratemale.as_view()),
    path('effectiveliteracyratefemale/<cityname>', views.Effectiveliteracyratefemale.as_view()),
    path('totalgraduates/<cityname>', views.Totalgraduates.as_view()),
    path('malegraduates/<cityname>', views.Malegraduates.as_view()),
    path('femalegraduates/<cityname>', views.Femalegraduates.as_view()),
    path('location/<cityname>', views.Location.as_view()),
    path('', views.add_data),

    path('add_data/', views.add_data),
    path('update_data/<pk>', views.update_data),

    # 6populationfemale



    # path('demo', views.Cities_list.as_view()),
    # path('demo', views.Cities_list.as_view()),
    # path('demo', views.Cities_list.as_view()),
    # path('demo', views.Cities_list.as_view()),
    # path('demo', views.Cities_list.as_view()),

]
