Linked lists are useful when:

-> The number of elements changes frequently.
-> There are many insertions and deletions.
->  You don't need fast random access by index.
| Feature             | Array                               | Linked List                     |
| ------------------- | ----------------------------------- | ------------------------------- |
| Memory              | Contiguous (adjacent)               | Non-contiguous (scattered)      |
| Size                | Usually fixed or resized by copying | Can grow and shrink dynamically |
| Access by index     | O(1)                                | O(n)                            |
| Insert at beginning | O(n)                                | O(1)                            |
| Delete at beginning | O(n)                                | O(1)                            |
| Memory overhead     | Low                                 | Higher (stores links)           |
| Cache performance   | Better                              | Generally worse                 |

| Array                                | Linked List                            |
| ------------------------------------ | -------------------------------------- |
| Contiguous memory                    | Nodes can be anywhere in memory        |
| O(1) indexing                        | O(n) indexing                          |
| Insert/Delete in middle: O(n)        | Insert/Delete after a known node: O(1) |
| Fixed-size allocation (conceptually) | Dynamic size                           |


"When do you use while current vs while current.next?"

A good answer is:

while current: Use when you need to process every node in the list (printing, counting, searching, summing, etc.).
while current.next: Use when you need to stop at the last node so you can safely modify its next pointer (for example, inserting a node at the end).

Golden Rule for interview: 
new_node.next = current.next   # Save the rest of the list
current.next = new_node        # Connect the new node
Never reverse the above two lines

Steps to remember:
Draw the list.
Circle the pointer you're about to overwrite.
Ask: "Have I saved what it was pointing to?"
Only then update the pointer.


Tricky Question:
head
 |
 v
10 → 20 → 30 → 40
We want to insert 25 at position = 2.
After executing:

new_node.next = current.next
but before executing:

current.next = new_node

What does head look like?

Hint: Remember that head hasn't changed yet. Think about:

Where does current point?
Where does new_node point?
What can you reach by starting from head?

Answer:
current holds 20 and pointing to 20 
new_node points to 25 and it has its next value as 30 so basically the structure would look like 25->30->40->none
Since We have not changed this pointer yet:

current.next = new_node
So the original list is still intact.

Starting from head, we still have:
head
 |
 v
10 → 20 → 30 → 40 → None
Separately, we also have:

new_node
 |
 v
25 → 30 → 40 → None
So there are two paths to node 30:

head
 |
 v
10 → 20 → 30 → 40
          ↑
          |
25 ───────┘
^
|
new_node

"What happens to the deleted node?"

"After updating the head, the old first node is no longer referenced by the linked list. In Python, once there are no references to that node, it becomes eligible for garbage collection."

| Operation           | Pointers Needed    |
| ------------------- | ------------------ |
| Traverse            | `current`          |
| Insert at beginning | `head`             |
| Insert at end       | `current`          |
| Insert at position  | `current`          |
| Delete first        | `head`             |
| Delete last         | `prev` + `current` |

Insert at Position:
for _ in range(position - 1): 

Delete at Position 
for _ in range(position): 

-> Insertion: You want current to stop at the previous node, where you'll insert after it.
-> Deletion: You want current to stop at the node to delete, while prev stops at the previous node.

This difference is one of the most common sources of off-by-one errors.

Reverse Linked List:
Reversed Part

10 → None
^
|
prev



Remaining Part

20 → 30 → None
^
|
current

Note: 
prev is building the reversed list.
current is walking through the remaining list.
next_node temporarily remembers where to go next.

Thumb Rule:
When you need to traverse every node, then use : 
while current:

When you need to look ahead, then use: 
while current.next

Always ask yourself: 
Do I want to process the current node or do I want to stop before the last node? 
If you're printing, counting, summing, searching, or finding max/min, you almost always want: 
while current:

| Loop Condition        | Last Node Processed? | Common Use                                                      |
| --------------------- | -------------------- | --------------------------------------------------------------- |
| `while current:`      | ✅ Yes                | Traverse, print, count, sum, search                             |
| `while current.next:` | ❌ No                 | Stop one node before the end (e.g., insert at end, delete last) |


## Slow and fast pointers 

slow = head

fast = head

while fast and fast.next:

    slow = slow.next

    fast = fast.next.next

slow always moves 1 step 

fast always moves 2 steps

To identify cycle in a linked list just check whether the slow==fast or not 


Why do we use a dummy node in the case of merge two linked list?
The dummy node avoids special handling for the head of the merged list. Every node is added using the same logic, and at the end we simply return dummy.next.


| Problem             | Fast Pointer Setup                                        | Where `slow` ends                 |
| ------------------- | --------------------------------------------------------- | --------------------------------- |
| Find middle         | `fast = head`                                             | Middle node                       |
| Detect cycle        | `fast = head`                                             | Meets `fast` if a cycle exists    |
| Remove Nth from end | Move `fast` ahead by **n** (or **n+1** with a dummy node) | At or just before the target node |

| Problem             | Initial Setup                                              | Pointer Movement         |
| ------------------- | ---------------------------------------------------------- | ------------------------ |
| Find Middle         | `slow = head`, `fast = head`                               | `slow += 1`, `fast += 2` |
| Detect Cycle        | `slow = head`, `fast = head`                               | `slow += 1`, `fast += 2` |
| Remove Nth From End | `slow = dummy`, `fast = dummy`, move `fast` ahead by `n+1` | `slow += 1`, `fast += 1` |

