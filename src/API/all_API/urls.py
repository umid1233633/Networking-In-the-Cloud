from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, InvoiceViewSet, TaskViewSet, InfoViewSet, UserGetViewSet, CollaborationViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenBlacklistView)


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'info', InfoViewSet, basename='info')
router.register(r'collaborations', CollaborationViewSet, basename='collaboration')
router.register(r'users', UserGetViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/logout/', TokenBlacklistView.as_view()),

]