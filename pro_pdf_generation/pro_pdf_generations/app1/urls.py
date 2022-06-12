from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[
    path('av/',views.AddEmployee.as_view(),name='add_url'),
    path('sv/',views.ShowEWmployee.as_view(),name='show_url'),
    path('uv/<int:id>/',views.UpdateEmployee.as_view(),name='update_url'),
    path('dv/<int:id>/',views.DeleteEmployee.as_view(),name='delete_url'),
    path('index/',views.index,name='index'),
    path('report/<int:id>/',views.report,name='report')
    
]