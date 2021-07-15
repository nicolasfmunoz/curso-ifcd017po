from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', login_required(views.index), name='index'),
    path('read_users/', login_required(views.read_users), name='read'),
    path('create_user/', views.create_user, name='create'),
    path('update_user/<int:id>', login_required(views.update_user), name='update'),
    path('delete_user/<int:id>', login_required(views.detele_user), name='delete'),
    path('', views.login_user, name='login'),
    path('logout/', login_required(views.logout_user), name='logout'),
]
