from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ArchOCR import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", include("ArchOCR.urls")),  # wszystkie ścieżki aplikacji
    path("accounts/", include("django.contrib.auth.urls")),  # logowanie/wylogowanie
    path('accounts/signup/', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include  # Importujemy include do obsługi URL-i aplikacji
# from ArchOCR import views
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),  # Panel administracyjny Django
#     path('', include('ArchOCR.urls')),  # Mapowanie na URL-e aplikacji ArchOCR
#
#     path('process_image/', views.process_image, name='process_image'),
#
#     # Wbudowane widoki logowania/wylogowania/zmiany hasła itp.:
#     path('accounts/', include('django.contrib.auth.urls')),
#
#     # Rejestracja (nasz widok):
#     path('accounts/signup/', views.signup, name='signup'),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
