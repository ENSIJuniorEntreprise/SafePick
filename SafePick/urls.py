from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('food/', views.foodApi),
    path('cosmetics/', views.cosmeticApi),
    path('food/<int:product_code>/<str:field_name>/', views.get_productF_field, name='get_product_field'),
<<<<<<< Updated upstream
    path('products/<str:product_id>/<str:collection_name>/', views.Alternatives, name='Alternatives'),
=======
    path('products/<str:product_id>/<str:collection_name>/', views.Alternatives, name='similar_products'),
>>>>>>> Stashed changes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
