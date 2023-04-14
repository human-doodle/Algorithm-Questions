'''

Implement an efficient algorithm for substring search using hashing. A naive algorithm for
determining if a string s1 is a substring of another string s2 is to iterate through every length n (let n be the
length of string s1 and m be the length of string s2) substring of s2 and to determine if s1 is equal to that
substring. This algorithm runs in O(n ∗ (m − n)). A better approach is to hash string s1, let’s say its hash
is h, and to find if there is a length n substring of string s2 that has the same hash h. Of course, having
the same hash doesn’t guarantee that two strings are the same, so once you find a substring with hash h,
you have to compare the two strings to check if they actually are the same–although, a good hash function
produces fewer false positives.
For this lab, you can use the following hash function:
h(sm−1sm−2sm−3...s0) = (26m−1.id(sm−1) + 26m−2.id(sm−2) + ... + 260.id(s0))%1009
id of a character is its position in the English alphabet. ‘a’ is 1, ‘b’ is 2, ‘c’ is 3 etc. You may assume both
strings will only contain lower case letters from the English alphabet.
Examples of computing the hash:
h(′cat′) = (262.3 + 261.1 + 260.20)%1009 = 2074%1009 = 56
h(′toys′) = (263.20 + 262.15 + 261.25 + 260.19)%1009 = 362329%1009 = 98
You might have noticed that iterating through length n substrings of s2, computing the hashs and comparing
with s1’s hash still costs us O(n ∗ (m− n)). It is your job to find an efficient way to compute the above hash
on length n substrings of s2 such that the whole process only costs O(m).
Examples
>>> is_substring("cat", "cats")
True
>>> is_substring("toy", "toys are us")
True
>>> is_substring("oat", "tao of life")
False

'''

def is_substring(s1, s2):
  
  '''
  Unicode code point of the character: ord()
  '''
    
    m, n = len(s2), len(s1)
    if m < n:
        return False

    # Compute the hash of s1
    h1 = 0
    for i in range(n):
        h1 = (h1 * 26 + ord(s1[i]) - ord('a') + 1) % 1009

    # Compute the initial hash of the first n characters of s2
    h2 = 0
    for i in range(n):
        h2 = (h2 * 26 + ord(s2[i]) - ord('a') + 1) % 1009

    # Compare the hash of s1 with the hash of every length n substring of s2
    if h1 == h2:
        return True
    
    # Compare the hash of s1 with the hash of every length n substring of s2
    if h1 == h2:
        return True
    for i in range(n, m):
        h2 = ((h2 - (ord(s2[i - n]) - ord('a') + 1) * (26 ** (n)))+ ord(s2[i]) - ord('a') + 1) % 1009
        if h1 == h2:
            return True

    return False
