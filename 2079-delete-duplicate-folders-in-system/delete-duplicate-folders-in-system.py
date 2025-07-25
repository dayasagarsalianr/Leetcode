class TrieNode:
  def __init__(self):
    self.children: dict[str, TrieNode] = {}
    self.deleted = False


class Solution:
  def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
    ans = []
    root1 = TrieNode()
    subtreeToNodes: dict[str, list[TrieNode]] = collections.defaultdict(list)

    # Construct the Trie
    for path in sorted(paths):
      node = root1
      for s in path:
        node = node.children.setdefault(s, TrieNode())

    # For each subtree, fill in the {subtree encoding: [root1]} hash table
    def buildSubtreeToRoots(node: TrieNode) -> str:
      subtree = '(' + ''.join(s + buildSubtreeToRoots(node.children[s])
                              for s in node.children) + ')'
      if subtree != '()':
        subtreeToNodes[subtree].append(node)
      return subtree

    buildSubtreeToRoots(root1)

    # Mark nodes that should be deleted
    for nodes in subtreeToNodes.values():
      if len(nodes) > 1:
        for node in nodes:
          node.deleted = True

    # Construct the answer array for nodes that haven't been deleted
    def constructPath(node: TrieNode, path: list[str]) -> None:
      for s, child in node.children.items():
        if not child.deleted:
          constructPath(child, path + [s])
      if path:
        ans.append(path)

    constructPath(root1, [])
    return ans