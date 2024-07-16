class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I' : 1,
            'V' : 5, 
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        result = 0
        prev  = 0
        
        for char in s: 
            current = roman_to_int[char]
            result += current
            if current > prev:
                result -= 2 * prev
            prev = current
        return result
                
                
    
    
    
# test 
print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))

# penjelasan
# 1. membuat dictionary roman_to_int
# 2. membuat variabel result dan prev dengan nilai 0
# 3. melakukan perulangan untuk setiap karakter di s
# 4. mengambil nilai dari karakter tersebut
# 5. menambahkan nilai tersebut ke result
# 6. jika nilai tersebut lebih besar dari prev maka kurangkan 2 * prev dari result

        
# Time complexity: O(n)
# Space complexity: O(1)
# Penjelasan:
# 1. Perulangan dilakukan sebanyak n kali, dimana n adalah panjang dari s
# 2. Operasi lain dilakukan dalam konstanta waktu
# 3. Sehingga time complexity adalah O(n)
# 4. Space complexity adalah O(1) karena hanya menggunakan konstanta space
# 5. Sehingga space complexity adalah O(1)
