class Parenthesis:
    def validParenthesis(self, s):
        temp = []
        closesParenthesis = {"}": "{", ")": "(", "]": "["}


s = "()[]{}"
obj = Parenthesis()
print(obj.validParenthesis(s))
