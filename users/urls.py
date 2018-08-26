"""定义users的url模式"""

from django.urls import path

from django.contrib.auth.views import LoginView#导入类
from . import views

app_name = 'users'

#修改模板路径
LoginView.template_name = 'users/login.html'


urlpatterns = [
#登录界面
	path('login/', LoginView.as_view(), 
	name='login'),
#注销
	path('logout/$',views.logout_view,name='logout'),
#注册页面
	path(r'^register/$', views.register, name='register'),

]

