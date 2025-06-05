class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str:
        # Initialize the parent array for union-find structure to point
        # each element to itself.
        parent = list(range(26))
      
        # The find function uses path compression for finding the
        # representative of a set.
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Merge the sets of characters in strings s1 and s2
        for i in range(len(s1)):
            char_s1, char_s2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            parent_s1, parent_s2 = find(char_s1), find(char_s2)
            # Link the sets by rank (in this case, by smallest representative).
            if parent_s1 < parent_s2:
                parent[parent_s2] = parent_s1
            else:
                parent[parent_s1] = parent_s2

        # Build the resulting equivalent string based on the base string
        # by replacing each character with its smallest equivalent.
        result = []
        for char in base_str:
            char_index = ord(char) - ord('a')
            result.append(chr(find(char_index) + ord('a')))
      
        # Join and return the computed characters as a single string.
        return ''.join(result)