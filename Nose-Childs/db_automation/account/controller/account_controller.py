from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.response import Response

from db_automation.account.service.account_service_impl import AccountServiceImpl


class AccountController(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()


    def requestCreateName(self, request):
        name = self.accountService.create()

        return Response(name, status=status.HTTP_200_OK)

    def requsstFineAccount(self,request):
        requestGetData = request.GET
        requestAccountId = requestGetData.get('accountId')

        foundAccount = self.accountService.findAccount(requestAccountId)

        return Response(
            model_to_dict(foundAccount),
            status.HTTP_200_OK
        )