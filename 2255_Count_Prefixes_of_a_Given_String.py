class Solution:
    def countPrefixes_loop(self, words: list[str], s: str) -> int:
        number_of_prefixes = 0
        s_length = len(s)
        for word in words:
            if len(word) > s_length:
                return number_of_prefixes
            if s.startswith(word):
                number_of_prefixes += 1
        return number_of_prefixes


test_sol = Solution()
res = Solution.countPrefixes(test_sol,
                             words=["a", "b", "c", "ab", "bc", "abc"], s="abc")
print(res)
