from TradeStrategyBase import TradeStrategyBase

class TradeStrategy2(TradeStrategyBase):
    """
    交易策略2: 均值回复策略，当股价连续两个交易日下跌，
    且下跌幅度超过阀值默认 s_buy_change_threshold(-10%),
    买入股票并持有 s_keep_stock_threshold (10) 天
    """
    s_keep_stock_threshold = 10
    s_buy_change_threshold = -0.10
    
    def __init__(self):
        self.keep_stock_day = 0
    
    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_ind >= 1:
            today_down = trade_day.change < 0
            yesterday_down = trade_days[trade_ind - 1].change < 0
            down_rate = trade_day.change + trade_days[trade_ind - 1].change
            if today_down and yesterday_down and down_rate < TradeStrategy2.s_buy_change_threshold:
                self.keep_stock_day += 1
        elif self.keep_stock_day > 0:
            self.keep_stock_day += 1
    
    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day >= TradeStrategy2.s_keep_stock_threshold:
            self.keep_stock_day = 0
    
    @classmethod
    def set_keep_stock_threshold(cls, keep_stock_threshold):
        cls.s_keep_stock_threshold = keep_stock_threshold
    @staticmethod
    def set_buy_change_threshold(buy_change_threshold):
        TradeStrategy2.s_buy_change_threshold = buy_change_threshold