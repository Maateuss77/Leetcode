def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    num = x
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return x == rev


case_1 = isPalindrome(121)
case_2 = isPalindrome(-121)
case_3 = isPalindrome(10)
print(f"caso 1 = {case_1}, caso 2 = {case_2}, caso 3 = {case_3}")

