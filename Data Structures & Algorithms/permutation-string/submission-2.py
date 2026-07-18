class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation can't exist if s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        # Using arrays of size 26 is faster than dictionaries for lowercase letters
        s1_counts = [0] * 26
        window_counts = [0] * 26
        
        # 1. Initialize the first window of size len(s1)
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if s1_counts == window_counts:
            return True
            
        # 2. Slide the window one character at a time across the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character on the right
            window_counts[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character that fell off the left
            left_char_index = i - len(s1)
            window_counts[ord(s2[left_char_index]) - ord('a')] -= 1
            
            # Compare the arrays
            if s1_counts == window_counts:
                return True
                
        return False