from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.snippet_detail, name='index'),
    path('all/', views.index, name='moviesList'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]