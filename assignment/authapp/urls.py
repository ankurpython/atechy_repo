from django.urls import path
from authapp.views import MyObtainTokenPairView,UserCreateView,UserRetrieveView,UserUpdateView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-create/', UserCreateView.as_view(), name='auth_register'),
    path('retrieve/<int:id>/', UserRetrieveView.as_view(), name='retrieve_user'),
    path('update/<int:id>/', UserUpdateView.as_view(), name='update_user'),
    # path('delete/<int:id>/', UserDestroyView.as_view(), name='delete_user'),

]
