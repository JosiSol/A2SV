class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        decrypted = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # Double-digit number case
                num = int(s[i:i + 2])
                decrypted += chr(ord('a') + num - 1)
                i += 3
            else:
                # Single-digit number case
                num = int(s[i])
                decrypted += chr(ord('a') + num - 1)
                i += 1
        return decrypted
