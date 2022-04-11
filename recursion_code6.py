#check if the string is palindrome, return True or False 

string = "madam"
# string = "reterrr"
n = len(string)
 
def palindrome(word , i ,  n ):
    if i >=  n//2:
        return True
    if word[i] != word[n-i-1]:
        return False 
    return palindrome(word, i+1, n)
    
print(palindrome(string, 0 , n))