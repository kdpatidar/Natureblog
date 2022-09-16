from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static  
urlpatterns = [
    path('', home , name='home'),
    path('register/', sign_up, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',logout_user, name='logout'),
    path('blogs/', show_blog, name='blogs'),
    path('addpost/', add_blog, name='addpost'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
 
    
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)