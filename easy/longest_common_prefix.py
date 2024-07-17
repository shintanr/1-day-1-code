class Solution(object):
    def longestCommonPrefix(self, strs):
        # jika string kosong maka mengembalikan nilai ''
        if not strs:
            return ''
        
        for i in range(len(strs[0])): # perulangan untuk setiap karakter di string pertama
            for string in strs[1:]: # perulangan untuk setiap string di strs[1:]
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    
    # Time complexity: O(n * m)
    # kenapa time complexity nya O(n * m)?
    # 1. Perulangan dilakukan sebanyak panjang dari strs[0]
    # 2. Perulangan dilakukan sebanyak panjang dari string terpendek di strs
    # 3. Sehingga time complexity adalah O(n * m)
    
    
    # misalnya di situ ada 3 string yitu flower, flow, dan flight
    # time complexity nya adalah O(5 * 3) = O(15)
    
# test
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix([""]))
print(Solution().longestCommonPrefix(["aba", "caba", "baca",]))
print(Solution().longestCommonPrefix(["12", "123", "1234", "1"]))


# Penjelasan:
# 1. Jika strs kosong, maka return ''
# 2. Lakukan perulangan sebanyak panjang dari strs[0]
# 3. Lakukan perulangan untuk setiap string di strs[1:]
# 4. Jika i >= len(string) atau string[i] != strs[0][i], maka return strs[0][:i]
# 5. Jika tidak ada yang return, maka return strs[0]
# 6. Sehingga time complexity adalah O(n * m) dimana n adalah panjang dari strs dan m adalah panjang dari string terpendek di strs
# 7. Space complexity adalah O(1) karena hanya menggunakan konstanta space
# 8. Sehingga space complexity adalah O(1)