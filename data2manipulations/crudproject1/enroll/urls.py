from django.urls import path
from .import views
urlpatterns=[
    path('',views.add_show,name='addshow'),
    path('<int:id>',views.update,name='update'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
]