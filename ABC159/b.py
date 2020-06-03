def checkPalindrome(str1, str2):
    for i in range(len(str1) // 2):
        if str1[i] != str2[i]:
            return False
    return True


s = input()
rs = ''.join(list(reversed(s)))
cri1 = checkPalindrome(s, rs)

s2 = s[:len(s) // 2]
rs2 = ''.join(list(reversed(s2)))
cri2 = checkPalindrome(s2, rs2)

s3 = s[len(s) // 2 + 1:len(s)]
rs3 = ''.join(list(reversed(s3)))
cri3 = checkPalindrome(s3, rs3)

if cri1 and cri2 and cri3:
    print('Yes')
else:
    print('No')
