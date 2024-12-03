from account.entity.account import Account
from account.repository.account_repository import AccountRepository
from django.forms import model_to_dict


class AccountRepositoryImpl(AccountRepository):


    __accountNameList = []

    #싱글톤 패턴
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def __processUserInput(self):
        userInputName = input("생성하고자 하는 이름을 입력하세요: ")
        return userInputName

    def createName(self):
        userInputAccountName = self.__processUserInput()
        account = Account(string=userInputAccountName)  # accountName으로
        account.save()


        return model_to_dict(account)

    def findById(self, id):
        return Account.objects.get(id=id)


