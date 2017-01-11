# Data Structures

In this article, I will mainly introduce the most well-known data structures on a technical level but let's first start with my understanding of data structures.

Different data structures are different representations of data. Due to these distinct features owned by these different representations, we could always describe a data structure from the following aspects:

1. The properties of a data structure;

2. The operations that could be applied on it, either to reflect some information of a data structure or manipulate the data stored in it.

3. The internal representation.

Based on the two aspects above, we first introduce one of the simplest data structure: stack.

## Stack

### Properties

The most important property, which could be used to distinguish a stack from other data structures, is "first in, last out", which means that the ealier an element is stored in a stack, the later it can be retrieved. To make it more clear, we can think of a stack as a box of which the cross section can only fit one book at one time. We can add a book to the top of the box and retrive a book from the top of the box. That is exactly how a stack works.

### Operations and Imlementations

Based on the property of a stack, there are three types of basic operations:

1. isEmpty: Check if a stack is empty or not.

2. Push: Add an element to the top of the stack.

3. Pop: Remove the element at the top of the stack.

So far, I have implemented all the operations above in Python. The implementation uses a list internally. Here is a detailed description of the implementation of the operations above:

1. isEmpty: Check if the internal list is a empty list or not.

2. Push: Append a new element to the end of a list. Inherently, the size of this list is incremented by one. Notice that here the newest pushed element is stored at the end of a list, which might be used by a pop operation.

3. Pop: Retrieve the last element in a list and then reslice the list to remove its last element.
