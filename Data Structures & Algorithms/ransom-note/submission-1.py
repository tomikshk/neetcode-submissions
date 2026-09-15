class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterset={}
        for i in magazine:
            if i in counterset:
                counterset[i]+=1
            else:
                counterset[i]=1  

        for i in ransomNote:
            if i not in counterset:
                return False
            elif counterset[i]==1:
                del counterset[i]
            else:
                counterset[i]-=1
        return True

        