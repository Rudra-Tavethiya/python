

from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',index,name='index'),
    path('register',register,name='register'),
    path('delete',delete,name='delete'),
    path('edit',edit,name='edit'),
           

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
