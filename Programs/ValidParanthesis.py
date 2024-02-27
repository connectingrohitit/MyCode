class Solution:

    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


print(Solution.is_valid('()'))
print(Solution.is_valid("(){}[]"))
print(Solution.is_valid("(]"))