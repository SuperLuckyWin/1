def filter_signals(signals):
    """
    综合多策略信号，生成最终决策
    """
    buy_strength = sum(s['strength'] for s in signals if s['direction'] == 'buy')
    sell_strength = sum(s['strength'] for s in signals if s['direction'] == 'sell')
    
    if buy_strength > sell_strength and buy_strength > 0.7:
        return 'buy'
    elif sell_strength > buy_strength and sell_strength > 0.7:
        return 'sell'
    else:
        return 'hold'