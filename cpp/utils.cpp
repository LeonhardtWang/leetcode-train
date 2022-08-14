#include "base_struct.cpp"
#include <iostream>


void print_list(ListNode* node) {
    std::cout << "[";
    while (node != nullptr) {
        std::cout << node->val << ", ";
        node = node->next;
    }
    std::cout << "]\n";

}