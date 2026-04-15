class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #Make a list of alphabet space
            for c in s:
                count[ord(c) - ord("a")] += 1 #take the ASCII and subtract from a
            res[tuple(count)].append(s)
        return list(res.values())