# include <vector>
# include <map>


using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      std::map<int, int> num2idx;
      for (int i = 0; i < nums.size(); i++) {
          int num = nums[i];
          num2idx.insert({num, i});
      } 
      for (int i = 0; i < nums.size(); i++) {
          int curr_num = target - nums[i];
          if (num2idx.find(curr_num) != num2idx.end() && num2idx[curr_num] != i) {
              return std::vector<int>({i, num2idx[curr_num]});
          }
      }
      return std::vector<int>({});
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {2,7,11,15};
    int target = 9;
    std::vector<int> res = solution.twoSum(nums, target);

    return 0;
}

