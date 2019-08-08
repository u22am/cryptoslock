from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'myapp1'

urlpatterns = [
    path('', views.index,name='index'),
    path('myapp1/signin', views.signin,name='signin'),
    path('myapp1/product', views.product,name='product'),
    path('myapp1/signup', views.signup,name='signup'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]
