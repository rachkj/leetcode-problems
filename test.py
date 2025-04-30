class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m={
            '(':')',
            '{':'}',
            '[':']'
        }
        st=[]

        for c in s:
            if c in m:
                st.append(c)
                print(st)
            elif len(st)>0 and m[st[-1]]==c:
                st.pop()

        return len(st)==0
    
test=Solution()
print(test.isValid("()"))