class TradeLoopBack(object):
    """
    trading back-testing system
    """
    def __init__(self, trade_days, trade_strategy):
        """
        :param trade_days: StockTradeDays 交易数据序列
        :param trade_strategy: TradeStrategyBase 交易策略
        """
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        #交易盈亏结果序列
        self.profit_array = []
    
    def execute_trade(self):
        for ind, day in enumerate(self.trade_days):
            if self.trade_strategy.keep_stock_day > 0:
                self.profit_array.append(day.change)
            #hasattr: 用来查询对象有没有实现某个方法
            if hasattr(self.trade_strategy, 'buy_strategy'):
                self.trade_strategy.buy_strategy(ind, day, self.trade_days)
            if hasattr(self.trade_strategy, 'sell_strategy'):
                self.trade_strategy.sell_strategy(ind, day, self.trade_days)