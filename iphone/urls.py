from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    index,
    Iphone_list_view,
    Iphone_detail_view,
    Iphone_create_view,
    Iphone_delete_view,
    Iphone_update_view,
)

urlpatterns = [
    path('list_view/', Iphone_list_view.as_view(), name='list_view'),
    path('details/<int:id>/', Iphone_detail_view.as_view(), name='details_view'),
    path('index/', index, name='index'),
    path('create/', Iphone_create_view.as_view(), name='create_phone_view'),
    path('delete/<int:id>/', Iphone_delete_view.as_view(), name='delete_phone_view'),
    path('update/<int:id>/', Iphone_update_view.as_view(), name='update_phone_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
