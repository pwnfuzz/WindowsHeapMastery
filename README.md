# 🔥 heap-playground  
**The Definitive Windows Heap Internals & Exploitation Suite**  
_A [PwnFuzz](https://pwnfuzz.com) Flagship Research Project_

---

## 🧠 About

**`heap-playground`** is a **research-grade knowledge suite** and practical playground that dissects the internals of Windows user-mode heap memory and its exploitation pathways on modern Windows systems (Windows 10+).

This repository is part of the **debut initiative from [PwnFuzz](https://pwnfuzz.com)** — dedicated to pushing the standards of exploit research, documentation, and tooling with battle-tested depth.

---

## 🎯 Project Objectives

- Provide a reproducible and documented **reference implementation of heap internals**
- Explain and demonstrate **heap exploitation techniques** still effective on modern systems
- Analyze the **structure, flow, and evolution** of Windows heap mechanisms: NT Heap, Segment Heap, LFH
- Cover all **relevant mitigations** implemented across OS versions (Windows 10 → latest)
- Offer **hands-on debugging, visualizations, and PoCs** using real-world tools (Windbg, custom tooling)

---

## Table of Contents

### 🧠 Project Docs
- [README.md](./README.md) – Project introduction, usage, and structure
- [GOALS.md](./GOALS.md) – Research and development objectives
- [SCOPE.md](./SCOPE.md) – Defined boundaries and supported platforms

### 📖 Documentation (`/docs`)
- [Overview](./docs/overview.md) – Introduction to heap concepts and allocator hierarchy
- [Glossary](./docs/glossary.md) – Definitions of key terms used throughout the project
- [References](./docs/references.md) – External whitepapers, blogs, and Microsoft docs

### 🔬 Heap Internals (`/internals`)
- [NT Heap](./internals/nt_heap.md) – Internal structures, backend/virtual allocations
- [Segment Heap](./internals/segment_heap.md) – Segment tree layout, metadata, frontend vs backend
- [LFH (Low Fragmentation Heap)](./internals/lfh.md) – Buckets, subsegment caching, frontend logic

### 🛡️ Mitigations (`/mitigations`)
- [Global Mitigations](./mitigations/global.md) – DEP, ASLR, CFG, GS
- [NT Heap Specific](./mitigations/nt_heap.md)
- [Segment Heap Specific](./mitigations/segment_heap.md)
- [LFH Specific](./mitigations/lfh.md)

### ⚙️ Allocation Behaviors (`/allocation_behaviors`)
- [HeapAlloc vs malloc](./allocation_behaviors/heapalloc_vs_malloc.md)
- [HeapCreate + HeapFree Lifecycle](./allocation_behaviors/heapcreate_flow.md)
- [Front-end vs Back-end handling](./allocation_behaviors/frontend_backend.md)

### 💥 Exploitation Techniques (`/exploitation_techniques`)
- [Heap Overflows](./exploitation_techniques/heap_overflow.md)
- [Use-After-Free](./exploitation_techniques/uaf.md)
- [Front-end Bucket Corruption](./exploitation_techniques/lfh_corruption.md)
- [Freelist Attacks](./exploitation_techniques/freelist.md)
- [Bypassing LFH with Fake Subsegments](./exploitation_techniques/lfh_bypass.md)
- [Segment Heap Exploits](./exploitation_techniques/segment_bypass.md)

### 🧪 Proof-of-Concepts (`/pocs`)
- [Use-After-Free PoCs](./pocs/uaf/)
- [Heap Overflow PoCs](./pocs/overflow/)
- [Heap Spray Templates](./pocs/heap_spray/)

### 🛠️ Tooling (`/tools`)
- [WinDbg Scripts](./tools/windbg/) – Automation for debugging
- [Heap Visualizer (WIP)](./tools/visualizer/) – Interactive heap memory maps

### 🧾 Notes (`/notes`)
- [Roadmap](./notes/roadmap.md)
- [Changelog](./notes/changelog.md)
- [Dev Notes](./notes/dev_log.md)

---

## 🧩 Audience & Use Cases

This repository is designed for:

- 🧠 **Exploit Developers** – crafting Windows heap exploits and understanding allocator behavior
- 🔬 **Security Researchers** – analyzing OS-level mitigations and memory protections
- 🛠️ **Reverse Engineers** – diving deep into undocumented or barely-documented heap logic
- 🎓 **Learners** – gaining hands-on experience with real-world allocators and PoCs

---

## 📢 Licensing

This project is licensed under the terms of the [MIT License](./LICENSE).

---

## 🧠 Built by [PwnFuzz](https://pwnfuzz.com)

> Precision in Exploitation.  
> High-Impact, Research-Driven Security Projects.
