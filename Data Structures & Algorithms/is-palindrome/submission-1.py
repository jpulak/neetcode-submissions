class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        new = ""
        for i in s:
            if i.isalpha() or i.isalnum():
                new +=i
        new = new.lower()

        return new == new[::-1]
        
       
        