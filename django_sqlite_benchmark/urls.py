from django.contrib import admin
from django.urls import path
from counters.views import counter, hello_word
from write.views import write_row_after_read_from_json, write_row_from_json

urlpatterns = [
    path("admin/", admin.site.urls),
    # /counter/<slug>/ runs counter view
    path("counter/<slug>/", counter),
    path("write/", write_row_from_json),
    path("write_after_read/", write_row_after_read_from_json),
    path("hello/", hello_word),
]
