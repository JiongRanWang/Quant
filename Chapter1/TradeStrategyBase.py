import six
from abc import ABCMeta, abstractclassmethod

class TradeStrategyBase(six.with_metaclass(ABCMeta, object)):
    @abstractclassmethod
    def buy_strategy(self, *args, **kwargs):
        pass
    
    @abstractclassmethod
    def sell_strategy(self, *args, **kwargs):
        pass
    
    

