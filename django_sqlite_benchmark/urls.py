from django.contrib import admin
from django.urls import path
from counters.views import counter
from write.views import write_row_from_json

urlpatterns = [
    path("admin/", admin.site.urls),
    # /counter/<slug>/ runs counter view
    path("counter/<slug>/", counter),
    path("write/", write_row_from_json),
]
