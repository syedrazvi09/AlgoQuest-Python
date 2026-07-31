class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        # Build frequency arrays
        for c in s1:
            need[ord(c) - ord('a')] += 1

        # First window
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if need == window:
            return True

        left = 0

        # Slide window
        for right in range(len(s1), len(s2)):

            # Add new character
            window[ord(s2[right]) - ord('a')] += 1

            # Remove old character
            window[ord(s2[left]) - ord('a')] -= 1

            left += 1

            if need == window:
                return True

        return False