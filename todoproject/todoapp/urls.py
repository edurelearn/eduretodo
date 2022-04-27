from pathlib import Path
from django.urls import path
from todoapp import views


urlpatterns=[
    path('',views.login),
    path('sign/',views.sign),
    path('dashboard/',views.dashboard),
    path('update/<int:id>',views.update),
    path('updateedit/<int:id>',views.updateedit),
    path('delete/<int:id>',views.delete),
    path('logout/',views.logout),
]