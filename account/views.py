from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ProductSerializer
from .models import Product
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserRegistrationSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status = 400)


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        data = request.data
        # print(data)
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refersh = RefreshToken.for_user(user)
            refersh_token = str(refersh)
            access_token = str(refersh.access_token)
            # print(user)
            return Response({'access_token': access_token, 'refresh_token' : refersh_token, 'email': user.email}, status=201)
        return Response(serializer.errors, status = 400)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    # print(request.headers)
    print(request.auth)
    print(request.user)
    return Response({"success": "good luck"})


@api_view(['GET'])
def get_product(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return  Response(serializer.data)


# class GetProductByCategoryId(APIView):
#     def get(self, request, category_id, format=None):
#         try:  
#             products = Product.objects.filter(category_id=category_id)
#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return HttpResponse("Error")