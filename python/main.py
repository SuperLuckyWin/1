import os
import ctypes
import pandas as pd
from strategy import TrendFollowingStrategy, MeanReversionStrategy, MomentumStrategy
from signal_filter import filter_signals
from optimizer import optimize_parameters

# 检查环境变量是否设置
if not all([os.getenv("BITGET_API_KEY"), os.getenv("BITGET_SECRET_KEY"), os.getenv("BITGET_PASSPHRASE")]):
    raise ValueError("Please set BITGET_API_KEY, BITGET_SECRET_KEY, and BITGET_PASSPHRASE environment variables.")

# 加载 C++/Rust 编译的动态库
cpp_lib = ctypes.CDLL('./cpp/build/libmarket_data.so')
rust_lib = ctypes.CDLL('./rust/target/release/librust_strategy.so')

def main():
    # 示例市场数据
    data = pd.DataFrame({
        'close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    })
    
    # 生成策略信号
    trend_strategy = TrendFollowingStrategy()
    mean_reversion_strategy = MeanReversionStrategy()
    momentum_strategy = MomentumStrategy()
    
    signals = [
        trend_strategy.generate_signal(data),
        mean_reversion_strategy.generate_signal(data),
        momentum_strategy.generate_signal(data)
    ]
    
    # 过滤信号
    decision = filter_signals(signals)
    print(f"Final decision: {decision}")
    
    # 优化参数
    optimized_params = optimize_parameters(data)
    print(f"Optimized parameters: {optimized_params}")

if __name__ == "__main__":
    main() 