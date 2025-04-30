from typing import List
from collections import deque
class Solution:
    def wordLadder(self, beginWord: str, endWord: str, wordList:List[str]):
        st=set(wordList)
        q=deque()
        q.append((beginWord,1))

        if endWord not in st:
            return 0
        
        while q:
            curWord, steps=q.popleft()
            for i in range(len(curWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord=curWord[:i]+c+curWord[i+1:]

                    if nextWord==endWord:
                        return steps+1
                    
                    if nextWord in st:
                        q.append((nextWord,steps+1))
                        st.remove(nextWord)

        return 0
        
test=Solution()
print(test.wordLadder("hit","cog",["hot","dot","dog","lot","log","cog"]))

        

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", 
# which is 5 words long.