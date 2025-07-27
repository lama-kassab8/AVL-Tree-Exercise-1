# 🌳 AVL Tree Implementation in Python

This is a clean, beginner-friendly implementation of an **AVL Tree**, a type of self-balancing Binary Search Tree (BST), written in Python using object-oriented programming.

## ✅ Features Implemented

### `Node` Class
- Represents a single tree node.
- Attributes:
  - `data`: The value stored in the node.
  - `left`: Pointer to the left child.
  - `right`: Pointer to the right child.
  - `height`: Height of the node in the tree.

### `AVLTree` Class
- Implements the core logic of the AVL tree.
- Methods implemented so far:
  - `get_height(node)`: Safely returns the height of a node (0 if `None`).
  - `balance_factor(node)`: Returns the balance factor (left height - right height).
  - `right_rotation(y)`: Fixes a left-left imbalance.
  - `left_rotation(y)`: Fixes a right-right imbalance.

## 🛠️ Features To Be Added

- `insert(root, key)`: 
  - Recursively inserts a new key like in a BST.
  - Updates heights.
  - Checks balance factor.
  - Rebalances using the appropriate rotation (LL, RR, LR, RL).

- `rebalance(node)`:
  - Centralizes logic for checking balance and deciding which rotation to apply.
  - Called inside `insert()` and `delete()`.

- `delete(root, key)`:
  - Removes a node from the tree.
  - Updates height.
  - Rebalances as needed.
  - Uses helper like `find_min()` to replace deleted nodes with inorder successors.

## 📌 Notes

- Balance factor must stay within **[-1, 0, 1]** for all nodes.
- Rotations are used to maintain balance after every insert/delete.
- This implementation focuses on **clarity** and **learning**, not just performance.

## 🧠 Learning Purpose

This AVL Tree project is part of a personal learning journey to master:
- Tree data structures
- Recursion
- Object-oriented programming in Python
- Self-balancing logic for search efficiency

