from abc import ABC, abstractmethod

# CustomerRepository에서 customer의 행위에 대해 뭔지 먼저 알리는(?)
class CustomerRepository(ABC):

    @abstractmethod
    def create(self, nickname):
        pass

    @abstractmethod
    def findById(self, id):
        pass

