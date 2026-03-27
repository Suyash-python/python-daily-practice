def is_palindrome(text):
    text = str(text)

    if text == text[::-1]:
        return True
    
    else:
        return False
    
print(is_palindrome("madam"))
print(is_palindrome(121))
print(is_palindrome("hello"))
