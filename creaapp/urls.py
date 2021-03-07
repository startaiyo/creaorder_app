from django.urls import path
from . import views

app_name="creaapp"

urlpatterns=[
  path("",views.index, name="index"),
  path("noorder",views.noorder,name="noorder"),
]