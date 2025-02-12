Contributed by : Sundaram Agnihotri ( student )
linkedin  : https://www.linkedin.com/in/sundaram-agnihotri/

class Solution {
public:
    int maximumSum(vector<int>& nums) {
    int maxSum = -1;
    unordered_map<int, int> digitSumMap;

    for (int num : nums) {
        int digitSum = 0, temp = num;
        while (temp) {
            digitSum += temp % 10;
            temp /= 10;
        }
        if (digitSumMap.count(digitSum)) {
            maxSum = max(maxSum, digitSumMap[digitSum] + num);
        }
        digitSumMap[digitSum] = max(digitSumMap[digitSum], num);
    }

    return maxSum;
    }
};
