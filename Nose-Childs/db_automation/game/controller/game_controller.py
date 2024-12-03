from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework import viewsets
from game.service.game_service_impl import GameServiceImpl


class GameController(viewsets.ViewSet):
    gameService = GameServiceImpl.getInstance()

    #def requestRollDice(self, request):
    #    dice = self.diceService.rollDice()

    #    return Response(dice, status=status.HTTP_200_OK)


    #def requestFindDice(self, request):
    #    requestGetData = request.GET
    #    requestDiceNumber = requestGetData.get('number')

    #    foundDice = self.diceService.findDice(requestDiceNumber)

    #    return Response(model_to_dict(foundDice),status=status.HTTP_200_OK)
