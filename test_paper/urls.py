from django.urls import path
from .views import start_test, get_qn, submit_test

urlpatterns = [
    path("start_test/", start_test, name="start_test"),
    path("qn/<int:qn_id>/", get_qn, name="qn"),
    path("submit_test/", submit_test, name="submit_test"),
]
