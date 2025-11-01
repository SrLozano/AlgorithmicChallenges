class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode each string as: length + '#' + string
        return ''.join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        
        while i < len(s):
            # 1. Find the position of the separator '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract length
            length = int(s[i:j])
            
            # 3. Extract the word
            word = s[j+1:j+1+length]
            result.append(word)
            
            # 4. Move index to after the word
            i = j + 1 + length
        
        return result