from django.conf import settings
from django.shortcuts import  redirect
import requests

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Recipeasy_Server.settings import env
from user.models import User
from user.serializer import UserSerializer
from user.utils import get_tokens_for_user


@api_view(['GET'])
@permission_classes([AllowAny])
def KakaoLoginView(request):

    code = request.GET.get('code', None)

    headers = {
        'Access-Control-Allow-Origin': 'http://127.0.0.1:8000',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    data = {
        'grant_type': 'authorization_code',
        'client_id': env('KAKAO_CLIENT_ID'),
        'redirect_uri': env('KAKAO_REDIRECT_URI'),
        'code': code
    }

    url = 'https://kauth.kakao.com/oauth/token'

    token_req = requests.post(url, headers=headers, data=data)
    token_req_json = token_req.json()
    access_token = token_req_json.get("access_token")
    refresh_token = token_req_json.get("refresh_token")

    kakao_api_response = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
            "Access-Control-Allow-Origin": "http://127.0.0.1:8000",
        },
    ).json()

    user_id = kakao_api_response.get('id')

    username = f'Recipeasy-{user_id}'
    realname = kakao_api_response.get('properties').get('nickname')

    try: #새로운 유저를 생성하는 경우
        user = User.objects.get(username=username)

    except: #유저가 이미 존재하는 경우
        user = User(username=username, realname=realname)
        user.save()
        user = User.objects.get(username=username)

    token = get_tokens_for_user(user)

    print(token)

    data = {'realname': realname, 'username': username, 'access_token': token['access'], 'refresh_token': token['refresh']}

    return Response(data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateNicknameView(request):

    serializer = UserSerializer(data=request.data)
    print(request.data)
    print(UserSerializer())

    if serializer.is_valid():
        user = User.objects.filter(username=request.user.username)

        # 유저가 발견되지 않은 경우
        if not len(user):
            return Response({'Message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user = user[0]

        # 유저가 이미 닉네임을 설정한 경우
        if user.nickname:
            return Response({'Message': 'User already has a nickname'}, status=status.HTTP_400_BAD_REQUEST)

        user.nickname = serializer.data['nickname']
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response({'Message': 'Error occurred'}, status=status.HTTP_400_BAD_REQUEST)



