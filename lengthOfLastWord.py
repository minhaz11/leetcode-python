def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    final = s.split()
    return len(final[-1])
print(lengthOfLastWord("Hello World"))