class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            # Format: <length> + <delimiter> + <string>
            encoded_str += f"{len(s)}#{s}"
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # The substring s[i:j] represents the length of the string
            length = int(s[i:j])
            
            # Move the pointer right past the '#'
            i = j + 1
            
            # Extract the actual string using the known length
            res.append(s[i : i + length])
            
            # Advance pointer to the start of the next encoded block
            i += length
            
        return res