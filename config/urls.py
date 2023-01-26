"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.router import router
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),    
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include(router.urls)),
    path('api/categories/<int:category_pk>/items/',api_views.ItemListCreateView.as_view(),name="add_items"),
    path('api/categories/<int:category_pk>/items',api_views.ItemListCreateView.as_view(),name="add_items"),
    path('api/items/<int:item_pk>/shipments/',api_views.ShipmentListCreateView.as_view(),name="add_shipments"),
    path('api/items/<int:item_pk>/shipments',api_views.ShipmentListCreateView.as_view(),name="add_shipments"),
    path('api/shipments/',api_views.ShipmentListView.as_view(),name="shipments"),
    path('api/shipments',api_views.ShipmentListView.as_view(),name="shipments"),
    path('api/lowstock/',api_views.LowStockListView.as_view(),name="lowstock"),
    path('api/lowstock',api_views.LowStockListView.as_view(),name="lowstock"),
]
