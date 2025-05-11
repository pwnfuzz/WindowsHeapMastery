# Overview

Created: May 10, 2025 9:47 AM

In computing, Heap refers to region of the memory used for dynamic memory allocation, which is done at runtime.  Unlike stack memory, which has predefined size determined the compile time, heap memory is allocated during the execution of the program. This dynamic nature of the heap memory is essential for applications that requires better scalability and optimization, as it allows allocation of memory as per need basis resulting in optimization. 

On windows systems, heap memory management is handled by the heap manager, a critical component within the windows responsible for creation, allocation, modification and deallocation of the memory regions. By default, every process in windows has access to a process-wide heap memory which remains allocated for process’ lifetime. The default heap which is allocated to process could be used by some internal windows function or can explicitly used by the process. 

The heap manager provides several functions that allow processes to manage their heap memory. These functions include:

- `HeapCreate`
- `HeapAlloc`
- `HeapFree`
- `HeapReAlloc`
- `HeapDestory`

While the above functions provide direct access to heap, many applications and C runtime library functions such as `malloc` , `realloc` or `free` , abstract away these details. For example, when a memory allocation happens with `malloc` , it’s ultimately utilizing the `HeapAlloc` function from the process’ default heap retrieved using the `GetProcessHeap` 

Windows uses multiple heap management strategies to handle memory requests efficiently, depending on the size of the allocation made:

1. **Frontend (Small Allocations)**: The frontend is responsible for efficiently allocating small memory chunks. It is optimized for fast allocation and deallocation.
2. **Backend (Large Allocations)**: For larger memory requests that cannot be handled by the frontend, the backend comes into play. It handles larger and less frequent memory allocations.

The heap manager utilizes different heap types to cater to various allocation patterns and performance needs. These include the default process heap, **Low Fragmentation Heap (LFH)**, and the newer **Segment Heap**.

Let’s breakdown the type of heaps in the next chapter.