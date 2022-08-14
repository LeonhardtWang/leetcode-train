#include <vector>
#include "string.h"

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

ListNode* build_list(std::vector<int> list, bool reverse=false) {
    ListNode* res = nullptr;
    if (list.empty()) {
        return res;
    }
    size_t init = reverse ? 0 : list.size() - 1;
    for (size_t i = init; i >= 0 && i < list.size(); reverse ? i++ : i--) {
        ListNode curr_node(list[i], res);
        res = &curr_node;
    }
    return res;
};






