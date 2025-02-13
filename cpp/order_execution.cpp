#include <iostream>
#include <string>

extern "C" {
    void execute_order(const char* order) {
        std::string order_str(order);
        std::cout << "Executing order: " << order_str << std::endl;
    }
} 