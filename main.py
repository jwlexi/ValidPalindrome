def isPalindrome(s):
        s = s.lower()
        temp = s[:len(s)]
        arr = []
        arra1 = []

        for x in range(len(s)):
            if(s[x].isalnum()):
                arra1.append(s[x])

        for x in range(len(temp[::-1])):
            if(temp[x].isalnum()):
                arr.append(temp[x])

        if(arr == arra1[::-1]):
            return True;
        return False;
inp = input("Enter your Palindrome: ")      
print(isPalindrome(inp))
                