def isAnagram(s, t):
    # l1 = ''.join(sorted(s))
    # l2 = ''.join(sorted(t))
    # return l1 == l2
    l1 = sorted(s)
    l2 = sorted(t)
    return l1 == l2

# Example 1:
# Input: 
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
# Output: true

# Example 2:
# Input: 
s = "rat"
t = "car"
print(isAnagram(s, t))
# Output: false
