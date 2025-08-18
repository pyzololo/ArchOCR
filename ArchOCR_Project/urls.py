from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ArchOCR import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),  # logowanie/wylogowanie django default
    path('accounts/signup/', views.signup, name='signup'),
    path("", include("ArchOCR.urls")),  # wszystkie ścieżki aplikacji
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
