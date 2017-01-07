#Sort
##Heapsort

Heapsort is one of the sort algorithms. If we want to understand the heapsort algorithm, we first need to know what a heap is.

In this algorithm, we regard a heap as an almost complete binary tree with certain properties. An almost complete binary tree is a kind of data structure which all levels of this binary tree are all filled with leaves but the last layer may be not. And for the last layer, the leaves will be filled from left to right. Based on this, a heap could have either max-heap property or min-heap property. The max-heap property indicates that, for all parent nodes in a heap, they have larger values than their child leaves. Similarly, the min-heap property means the opposite.

When we talk about sort algorithms, we usually regard an array of elements as input. And each element has a value as well as an index to indicate its position in an array. But how can we make use of the max-heap property of a heap to build our sort algorithm? The heapsort algorithm utilizes the max-heap property wisely: the algorithm will first build a max heap where all of the nodes satisfy the max-heap property, from the input array. Then it extracts the root element, which obviously has the largest value among all elements in this array, switch this one with the element at the end of the (sorted) output array. Then this algorithm will apply some operations to recover the max-heap property, making the root element largest again. Note that before we recover the heap to a max heap, we need to decrement the heapsize by one in order to keep the last, well-sorted element untouched. After that, we exchange this element with the second last element in the output array, decrement the heapsize by one and then recover the max heap property. During each iteration, we keep applying these oeprations. The iteration will be terminated until the heapsize bocomes one. We will get a nicely sorted output array.

But there are still two questions remaining here: 

1. How can we recover the max-heap property?

2. How to build a max heap from an array as the initial max heap of this heapsort algorithm?

Actually, these two questions are quite relevant. Let us start with building a heap with no property from an array. We could put all elements layer by layer, from left to right into a binary tree. Then? How can we get a max heap?

The answer is also quite simple. We can look at the simplest case of a heap, a single node. This node itself is already a max heap, right? If we have two independent leaf nodes, these two are two max heaps without any doubts. What if these two nodes are two child leaves of a parent leaf node, we only need to consider the relation between this parent node with its left child and the relation between it with its right child; If the parent leaf has the largest value, then the heap consisting of these three nodes is already a max heap; Otherwise, exchange this parent node with its larger child node, then we could get a max heap again. Thus, assume we have two sub-heaps which are already max-heaps, we could compare the root node with its chid nodes. Once the exchange occurs, the max-heap property might be parially messed. Then if we apply this comparison recursively, we will end up with a max heap again. By applying this operation recursively in the heapsort algorithm during each iteration, the max-heap property will be recovered since only replacing the root element in the heap will not destroy its two sub max-heaps.

Besides, by using the operation above, a initial max heap which consists of all the elements in the input array could be easily built. In a almost complete binary tree, all leaf nodes without children are already max heaps. Then we could still inherit the idea that recovering max heap property from bottom layers to top layers to gurantee that the operation could be applied on a subtree of which the root node and its two children may not satisfy the max heap property but with two sub max heaps. Then we only need to apply this operaiton to the first half elements of an array because the second half elements are already max heaps. 

For more details, please refer to the implementation of this algorithm.
