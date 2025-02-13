#include <iostream>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

struct MarketData {
    uint64_t timestamp;
    double price;
    double volume;
};

extern "C" {
    const char* process_market_data(const char* data) {
        auto market_data = json::parse(data);
        MarketData md = {market_data["timestamp"], market_data["price"], market_data["volume"]};
        
        // 示例处理逻辑
        if (md.price > 100.0) {
            return "buy";
        } else {
            return "sell";
        }
    }
} 