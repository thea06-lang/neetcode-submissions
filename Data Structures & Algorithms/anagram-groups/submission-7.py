class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            result[sorted_key].append(s)
        return list(result.values())