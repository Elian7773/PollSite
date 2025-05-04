# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),  # The home page (index view)
    path('<int:question_id>/', views.detail, name='detail'),  # Poll details page
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Voting page
    path('<int:question_id>/results/', views.results, name='results'),  # Results page
]