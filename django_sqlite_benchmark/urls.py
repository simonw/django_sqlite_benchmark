from django.contrib import admin
from django.urls import path
from counters.views import counter

urlpatterns = [
    path("admin/", admin.site.urls),
    # /counter/<slug>/ runs counter view
    path("counter/<slug>/", counter),
]
