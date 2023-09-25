from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

 

urlpatterns = [
    path('register/',views.register ,name='register'),
    path('signin/',views.signin,name='signin'),
    path('fileupload/',views.fileupload,name='fileupload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

