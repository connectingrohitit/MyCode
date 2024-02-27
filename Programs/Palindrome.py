class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        palindrome = False
        str1 = [int(a) for a in str(x)]
        n = len(str1)
        if n <= 1:
            return palindrome
        else:
            string = str(x)
            for i in range(0, n):
                if str1[i] == str1[-(i + 1)]:
                    palindrome = True
                else:
                    palindrome = False
                    break
        return palindrome


print(Solution.is_palindrome(122))
