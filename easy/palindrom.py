class Solution(object):
    def isPalindrome(self, x):

        # jika negatif mengembalikan false
        if x < 0: 
            return False

        # mengonversi bilangan bulat menjadi string
        str_x = str(x)

        # ::-1 untuk membaca string dari belakang
        return str_x == str_x[::-1]
    

sol = Solution()
print(sol.isPalindrome(1211))
print(sol.isPalindrome(121))
print(sol.isPalindrome(1221))
print(sol.isPalindrome(-121))

