class Solution(object):
    def twoSum(self, nums, target):
       num_to_index = {}
       for i, num in enumerate(nums):
           if target - num in num_to_index:
               return [num_to_index[target - num], i]
           num_to_index[num] = i
           
           
# penjelasan
# 1. membuat dictionary num_to_index
# 2. melakukan perulangan dengan enumerate untuk mendapatkan index dan value
# 3. jika target - num ada di num_to_index maka return index dari target - num dan index dari num
# 4. jika tidak ada maka masukkan num ke num_to_index dengan index i
# 5. selesai