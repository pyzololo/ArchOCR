from django.urls import path
from . import views  # Import widoków z aplikacji ArchOCR

urlpatterns = [
    path('', views.home, name='home'),  # Strona główna
    path('process_image/', views.process_image, name='process_image'),  # Przesyłanie obrazu
    path("my-scans/", views.my_scans, name="my_scans"),
]

