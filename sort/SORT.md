#Sort
##Heapsort

Heapsort is one of the sorting algorithms. If we want to understand the heapsort algorithm, we first need to know what a heap is.

A heap is a kind of data structure based on binary tree. If we have an array of number as input, we could build a heap by filling the binary tree layer by layer, and in each layer, from the left to the right according to each element's index.
Also a heap could have some properties. In this algorithm, we will use max heap property, which means that every element in this tree has larger value than its children nodes. 
 
The heapsort algorithm utilizes the max heap property. For a max heap, the root node element has the largest value. Since our goal of this sorting is to reorder this array from its smallest value to its largest value, we could extract the largest element and put it at the end of this heap. Then during the next iteration, we build max heap property while decrementing the heapsize by 1 to leave the sorted elements untouched and repeat exchanging. The iteration will be terminated until the heapsize becomes 1.

To be more specific, the implementation details of building max heap property from a random heap and building a max heap is from a unordered array are also worth mentioning. First we explain how to build max heap property from a random heap. By checking the root node of this heap, we compare it with its left child and right child. If any of its two children has larger value than it, swap the elements of the root node and the node with largest value. Since the previous root node will have new children nodes due to this exchange, so it may lead to a contradiction to the max heap property. Thus, we need apply the whole procedure recursively to gurantee all the subtrees after exchange remain the max heap property. As for builidng a max heap, we only need to apply this procedure of building max heap property from the middle element in this array since the rest of elements already satisfy the max heap property (these elements do not have any children nodes thus they are already max heaps).   
