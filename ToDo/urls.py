"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import handler404, handler500, handler403
from django.urls import path
from todo_app import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # ToDos
    path('home/', views.home, name='home'),
    path('', views.home2, name='home2'),
    path('current/', views.currentToDos, name='currentToDos'),
    path('completed/', views.completedToDos, name='completedToDos'),
    path('create/', views.createToDos, name='createToDos'),
    path('todo/<int:todo_pk>', views.viewToDos, name='viewToDos'),
    path('todo/<int:todo_pk>/complete', views.completeToDos, name='completeToDos'),
    path('todo/<int:todo_pk>/delete', views.deleteToDos, name='deleteToDos'),

    # Other
    path('instruction/', views.instruction, name='instruction'),
    path('link to authors/', views.link, name='link'),
    path('support/', views.donate, name='donate'),

]
# Mistakes

handler404 = 'todo_app.views.error_404'
