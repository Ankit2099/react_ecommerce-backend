from django.urls import path
from account.views import user_registration, login_view, test_token, get_product


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('login/', login_view, name='user_registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test_token/', test_token, name='test_token'),
    path('get_product/', get_product, name='get_product'),
]