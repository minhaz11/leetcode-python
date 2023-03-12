def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        for left in range(len(s) - 9):
            curr = s[left:left+10]
            if curr in seen:
                ans.add(curr)
            seen.add(curr)
        return list(ans)
