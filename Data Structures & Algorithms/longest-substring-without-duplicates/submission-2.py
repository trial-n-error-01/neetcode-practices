class Solution:
# 99% faster, optimised solution
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Fixed-size array for ASCII characters initialized to -1
    char_index = [-1] * 128
    max_len = 0
    left = 0

    for right, char in enumerate(s):
      ascii_val = ord(char)
      if char_index[ascii_val] >= left:
        left = char_index[ascii_val] + 1
      char_index[ascii_val] = right
      max_len = max(max_len, right - left + 1)

    return max_len