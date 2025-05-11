# Glossary

### HEAP_ENTRY
A structure used by the heap manager to store metadata about individual allocations within the heap.

### Low Fragmentation Heap (LFH)
A special type of heap optimized to reduce fragmentation by using multiple buckets for allocations of similar sizes.

### Segment Heap
A new heap type introduced in Windows 10 to address scalability issues and improve memory allocation performance.

### Frontend Allocation
Refers to the part of the heap manager responsible for handling small memory allocation requests.

### Backend Allocation
Handles larger and less frequent memory allocations that the frontend cannot process.

### RtlAllocateHeap
An internal function responsible for allocating memory from a process's heap in the Windows heap manager.
