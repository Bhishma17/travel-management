# reviews/urls.py
from django.urls import path
from .views import review_list, add_review
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', review_list, name='review_list'),
    path('add/', add_review, name='add_review'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
