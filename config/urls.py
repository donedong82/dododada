from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dododada/', include('dododada.urls')),
    path('', TemplateView.as_view(template_name="main.html"), name="root"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)