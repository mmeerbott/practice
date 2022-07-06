class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = strs[0]
        
        for string in strs:
            longest_common_prefix = self.getSharedPrefix(longest_common_prefix, string)
            
        return longest_common_prefix
        
    def getSharedPrefix(self, first: str, second: str) -> str:
        prefix = ''
        for a, b in zip(first, second):
            if a == b:
                prefix = prefix + a
            else:
                return prefix
        return prefix
