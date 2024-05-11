class Solution:
    def isValid(self, s: str) -> bool:

        # stack
        st = []
        for idx,i in enumerate(s):
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            elif len(st)>0:
                if (i == ']' and st[-1]=='[') or (i == ')' and st[-1]=='(') or (i == '}' and st[-1]=='{'):
                    st.pop()
                else:
                    return False
            else:
                return False
        if st == []:
            return True
        else:
            return False


        