Leetcode 129

Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  def dfs(root, total):
    if not root:
      return 0
    total = root.val + total * 10
    if not root.left and not root.right:
      return total

    return dfs(root.left, total) + dfs(root.right, total)
    
  return dfs(root, 0)


Solution 2:

def find_root_to_leaf_path_numbers(currentNode, pathSum):
  if currentNode is None:
    return 0

  # calculate the path number of the current node
  pathSum = 10 * pathSum + currentNode.val

  # if the current node is a leaf, return the current path sum
  if currentNode.left is None and currentNode.right is None:
    return pathSum

  # traverse the left and the right sub-tree
  return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()

Time complexity #
The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once

Space complexity #
The space complexity of the above algorithm will be O(N)O(N) in the worst case. This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
