from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, TokenSerializer
from apps.users.models import User
import jwt
from datetime import datetime, timedelta
import os


def generate_tokens(user):
    secret_key = os.getenv('JWT_SECRET', 'your-secret-key')
    expires_in = int(os.getenv('JWT_EXPIRES_IN', '3600'))

    access_token_payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),
        'iat': datetime.utcnow(),
    }

    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7),
        'iat': datetime.utcnow(),
    }

    access_token = jwt.encode(access_token_payload, secret_key, algorithm='HS256')
    refresh_token = jwt.encode(refresh_token_payload, secret_key, algorithm='HS256')

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        tokens = generate_tokens(user)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
            },
            'tokens': tokens
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        tokens = generate_tokens(user)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
            },
            'tokens': tokens
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    refresh_token = request.data.get('refresh_token')
    if not refresh_token:
        return Response({'error': '缺少refresh_token'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        secret_key = os.getenv('JWT_SECRET', 'your-secret-key')
        payload = jwt.decode(refresh_token, secret_key, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
        tokens = generate_tokens(user)
        return Response(tokens)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token已过期'}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({'error': 'Token无效'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
