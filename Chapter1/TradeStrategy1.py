from TradeStrategyBase import TradeStrategyBase
class TradeStrategy1(TradeStrategyBase):
    """
    交易策略1: 追涨策略， 当股价上涨一个阀值默认为7%时
    买入股票并持有s_keep_stock_threshold(20)天
    """
    s_keep_stock_threshold = 20
    def __init__ (self):
        self.keep_stock_day = 0
        self.__buy_change_threshold = 0.07
    
    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_day.change > self.__buy_change_threshold:
            self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            # self.keep_stock_day > 0 means having stocks, then increasing the days
            self.keep_stock_day += 1
        
    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day >= TradeStrategy1.s_keep_stock_threshold:
            self.keep_stock_day = 0
    
    @property
    def buy_change_threshold(self):
        # getter function, 它使得buy_change_threshold成为一个属性
        return self.__buy_change_threshold
    @buy_change_threshold.setter
    def buy_change_threshold(self, buy_change_threshold):
        if not isinstance(buy_change_threshold, float):
            raise TypeError('buy_change_threshold must be float!')
        self.__buy_change_threshold = round(buy_change_threshold,2)
    
