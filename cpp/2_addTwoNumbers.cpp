#include "utils.cpp"


int main() {
    std::vector<int> vec = {1,2,3,4,5};
    ListNode* node = build_list(vec);
    print_list(node);
}