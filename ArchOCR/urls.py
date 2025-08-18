from django.urls import path
from . import views  # Import widoków z aplikacji ArchOCR


urlpatterns = [
    path("my-scans/", views.my_scans, name="my_scans"),
    # path('scan/<uuid:pk>/', views.scan_detail, name='scan_detail'),
    # path("upload/", views.upload_scan, name="upload_scan"),
    path('studio/', views.studio, name='studio'),  # widok bez wybranej strony
    path('studio/<uuid:pk>/', views.studio, name='studio_detail'),
]
