class Solution:
  def finalValueAfterOperations(self, operations: list[str]) -> int:
    return sum(op[1] == '+' or -1 for op in operations)

# **** Java solution: ****

# class Solution {
#   public int finalValueAfterOperations(String[] operations) {
#     int ans = 0;

#     for (final String op : operations)
#       ans += op.charAt(1) == '+' ? 1 : -1;

#     return ans;
#   }
# }
