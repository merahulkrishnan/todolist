from . import views
from django.urls import path

urlpatterns = [
    path('login/demo/', views.demo, name='demo'),
    path('', views.newhome, name='newhome'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    # path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    # path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    # path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    # path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),

]
