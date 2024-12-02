from django.forms import model_to_dict
from rest_framework import viewsets, status  #rest_framework? : API 서버를 쉽게 구축할 수 있도록 돕는 라이브러리
from rest_framework.response import Response # 라이브러리

from rest_framework import viewsets
from dice.service.dice_service_impl import DiceServiceImpl


class DiceController(viewsets.ViewSet):
    diceService = DiceServiceImpl.getInstance()

    def requestRollDice(self, request):
        dice = self.diceService.rollDice()

        return Response(dice, status=status.HTTP_200_OK)


    def requestFindDice(self, request):
        requestGetData = request.GET
        requestDiceNumber = requestGetData.get('number')

        foundDice = self.diceService.findDice(requestDiceNumber)

        return Response(model_to_dict(foundDice),status=status.HTTP_200_OK)


#def requestEveryDice(self, request):
#    diceList = self.diceService.findEveryDice()

    # diceList 중 JSON 변환 할 항목들을 미리 지정하고
    # serializer.data로 변환한 항목을 리턴함
#    serializer = DiceSerializer(diceList, many=True)

#    return Response(serializer.data, status=status.HTTP_200_OK)