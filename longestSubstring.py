class LongestSubstring:
    def longestSubstring(self, s:str)->int:
        maxCount=0
        for i in range(len(s)):
            st=set()
            st.add(s[i]) #a
            count=1      #1
            for j in range(i+1,len(s)): 
                if s[j] not in st:    
                    st.add(s[j])
                    count+=1
                else:
                    break
            if count>maxCount:
                maxCount=count
        return maxCount
    
test=LongestSubstring()
print(test.longestSubstring("bbbbb"))



# Input: s = "abcabcbb"
# Output: 3