class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the delimiter '#' to extract the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # Extract the exact substring after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])

            i = end
        return res


