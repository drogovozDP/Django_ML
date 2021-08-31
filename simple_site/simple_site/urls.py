from django.contrib import admin
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', include('mainApp.urls'))
]
