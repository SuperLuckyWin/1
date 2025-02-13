import numpy as np
import pandas as pd

class TrendFollowingStrategy:
    def generate_signal(self, data):
        """
        趋势跟踪策略：基于移动平均线交叉
        """
        short_ma = data['close'].rolling(window=5).mean()
        long_ma = data['close'].rolling(window=20).mean()
        
        if short_ma.iloc[-1] > long_ma.iloc[-1]:
            return {'direction': 'buy', 'strength': 1.0}
        else:
            return {'direction': 'sell', 'strength': 1.0}

class MeanReversionStrategy:
    def generate_signal(self, data):
        """
        均值回归策略：基于 RSI 超买超卖
        """
        rsi = self.calculate_rsi(data['close'], 14)
        
        if rsi.iloc[-1] < 30:
            return {'direction': 'buy', 'strength': 0.8}
        elif rsi.iloc[-1] > 70:
            return {'direction': 'sell', 'strength': 0.8}
        else:
            return {'direction': 'hold', 'strength': 0.0}

    def calculate_rsi(self, prices, period):
        deltas = np.diff(prices)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)
        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        return 100 - (100 / (1 + rs))

class MomentumStrategy:
    def generate_signal(self, data):
        """
        动量策略：基于价格动量
        """
        momentum = data['close'].iloc[-1] - data['close'].iloc[-5]
        
        if momentum > 0:
            return {'direction': 'buy', 'strength': 0.9}
        else:
            return {'direction': 'sell', 'strength': 0.9} 