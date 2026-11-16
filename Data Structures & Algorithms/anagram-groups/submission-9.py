class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            #use .join() to glue the array into one word. For example: ['a', 'e', 't'] -> "aet"
            sorted_key = "".join(sorted(s))
            # find the sorted key and append the string that has that combination as the value
            result[sorted_key].append(s)
        return list(result.values())