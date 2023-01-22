from rest_framework.routers import DefaultRouter
from api import views as api_views

router = DefaultRouter()
router.register('items', api_views.ItemViewSet)
