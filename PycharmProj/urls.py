from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('movies/', include('Api_Assign.urls')),
]
