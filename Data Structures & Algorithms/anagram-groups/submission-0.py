class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #optimal O(m*n) solution
        res = defaultdict(list) #mapping chartCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26 #a ... z

            for c in s:
                count[ord(c) - ord("a")] +=1

            res[tuple(count)].append(s)
        
        return list(res.values())

