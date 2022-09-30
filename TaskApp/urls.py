from TaskApp import views
from django.urls import path  


urlpatterns=[
    path('task',views.taskApi),
    path('task/<int:id>',views.taskApi)
]