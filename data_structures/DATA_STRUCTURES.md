#Data Structures
In this article, I will mainly introduce the most well-known data structures on a technical level but let's first start with my understanding of data structures.

Different data structures are different representations of data. Due to these distinct features owned by these different representations, we could always describe a data structure from the following aspects:

1. The properties of a data structure;

2. Within a data structure, what kind of operations could be applied on it either to reflect some properties of a data structure or manipulate the data stored in it.

Based on the two aspects above, we first introduce one of the simplest data structure: stack.
##Stack
###Properties
The most important property, which could be used to distinguish a stack from other data structures, is "first in, last out", which means that the ealier an element is stored in a stack, the later it can be retrieved. To make it more clear, we could regard a stack as a container of which the size can only fit one book at one time. Thus, each time we could place one book inside. So if we keep pushing books inside, every time we want to retrieve a book, we can only get the book on top of this container. That is exactly how a stack works.
###Operations and Imlementations
Based on the property of a stack, there are three types of basic operations:

1. isEmpty: Check if a stack is empty or not.

2. Push: Push an element into a stack.

3. Pop: Pop the top element in a stack.

So far, I have implemented all the operations above by Python. A list is used as a stack. The detailed description of the operations above:

1. isEmpty: Check if the list is a empty list or not.

2. Push: Append a new element to the end of a list. Inherently, the size of this list is incremented by one. Notice that here the newest pushed element is stored at the end of a list, which might be used by a pop operation.

3. Pop: Retrieve the last element in a list and then slice the list by removing its last element.  
