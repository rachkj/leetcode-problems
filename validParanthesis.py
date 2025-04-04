class ValidParanthesis:
    def validParanthesis(self, s:str)->bool:
        m={
            '(':')',
            '{':'}',
            '[':']'
        }
        st=[]
        for c in s:
            if c in m:
                st.append(c)
            elif m[st[-1]]==c and len(st)>0:
                st.pop()
        return len(st)==0
    
validP=ValidParanthesis()
print(validP.validParanthesis("()[]{}"))
print(validP.validParanthesis("([])"))
print(validP.validParanthesis("(]"))




# Input: s = "()[]{}"
# Output: true