class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Handle edge cases
        if not strs or len(strs) == 0:
            return ""
        
        # Step 2: Use first string as reference
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            
            # Step 3: Check this character in all other strings
            for j in range(1, len(strs)):
                # If we reached end of any string OR characters don't match
                if i == len(strs[j]) or strs[j][i] != current_char:
                    return strs[0][:i]  # Return prefix up to previous character
        
        # Step 4: If we complete loop, first string is the common prefix
        return strs[0]