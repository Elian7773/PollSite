from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # This is the root URL pointing to the 'index' view
    path('polls/', include('polls.urls')),  # Include 'polls' app URLs
]
