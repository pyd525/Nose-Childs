from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dice.controller.dice_controller import DiceController

# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /dice로 시작
router = DefaultRouter()
# router.register(r"game", DiceController, basename='game')

urlpatterns = [
    # path('', include(router.urls)),
]