class Solution(object):
    def reverseVowels(self, input: str) -> str:
        s = list(input)
        left, right = 0, len(s) - 1
        vowels = list("aeiou" + "aeiou".upper())
        while left < right:
            if ( s[left] in vowels ) and ( s[right] in vowels ):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in vowels:
                    left += 1
                if s[right] not in vowels:
                    right -= 1
        print(''.join(s))
    reverseVowels(object, 'leetcode')
