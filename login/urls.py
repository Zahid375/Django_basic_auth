from django.urls import path
from login import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
urlpatterns = [
    path('',views.index,name="home"),
    path('registration/',views.registration,name="registration"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('login/',views.UserLogin,name="login"),
    path('logout/',views.UserLogout,name="logout"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
