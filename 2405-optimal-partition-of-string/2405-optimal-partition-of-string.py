class Solution:
    def partitionString(self, s: str) -> int:
        st, count = set(), 0
        for ch in s:
            if ch not in st:
                st.add(ch)
            else:
                count += 1
                st = set([ch])
        return count + 1
        