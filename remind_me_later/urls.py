from django.contrib import admin
from django.urls import path
from remindme_app.views import reminder_save

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reminder-save/', reminder_save, name='reminder_save')
]
