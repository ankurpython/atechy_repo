from django.contrib import admin
from django.urls import path, include
from authapp import views as V2
#from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
#router.register('api',V1.EmployeeCRUDCBV)
#router.register('users',V2.UserRegisterView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
