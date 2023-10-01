from django.urls import path
from . import views

app_name = "Requests"

urlpatterns = [
        path("addservise/", views.add_service_view, name="add_service_view"),
        path("service/", views.service_view, name="service_view"),
        path("update/<service_id>", views.service_update_view, name="service_update_view"),
        path("details/<service_id>", views.service_detail_view, name="service_detail_view"),
        path("delete/<service_id>", views.service_delete_view, name="service_delete_view"),
        path("addrequest/<service_id>", views.add_request_view, name="add_request_view"),
        path("requests/", views.show_request_view, name="show_request_view"),
        path("manage/", views.manage_request, name="manage_request"),
        path("updatestatus/<servicerequest_id>", views.update_status, name="update_status"),

]