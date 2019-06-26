#实现函数casino（）： 假设有100个赌徒，每个赌徒都有1000000元，并且每个人都想在赌场玩1000万次，在不同的胜率，赔率和手续费下casino（）函数返回总体统计结果，代码如下：
import numpy as np 
gamblers = 100
def casino(win_rate, win_once = 1, loss_once = 1, commission = 0.01):
    """
    win_once: 每次赢的钱数
    """
    my_money = 1000000
    play_cnt = 10000000
    for _ in np.arange(0,play_cnt):
        w = np.random.binomial(1,win_rate)
        if w:
            my_money += win_once
        else:
            my_money -= loss_once
        my_money -= commission
        if my_money <= 0:
            break 
    return my_money

heaven_moneys = [casino(0.5,commission=0) for _ in np.arange(0,gamblers)]
cheat_moneys = [casino(0.4,commission=0) for _ in np.arange(0,gamblers)]
commission_moneys = [casino(0.5, commission=0.01) for _ in np.arange(0,gamblers)]
