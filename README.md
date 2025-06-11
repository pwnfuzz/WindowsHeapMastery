# 🔥 heap-playground  
**The Definitive Windows Heap Internals & Exploitation Suite**  
_A [PwnFuzz](https://pwnfuzz.com) Flagship Research Project_

---

**`heap-playground`** is a **research-grade knowledge suite** and practical playground that dissects the internals of Windows user-mode heap memory and its exploitation pathways on modern Windows systems (Windows 10+).

This repository is part of the **debut initiative from [PwnFuzz](https://pwnfuzz.com)** — dedicated to pushing the standards of exploit research, documentation, and tooling with battle-tested depth.

---

## Objectives

- Provide a reproducible and documented **reference implementation of user-mode heap internals**
- Explain and demonstrate **heap exploitation techniques** still effective on modern systems
- Analyze the **structure** and **flow** of Windows user-mode heap mechanisms: NT Heap, Segment Heap, LFH on Windows10/11
- Cover all **relevant mitigations** implemented across OS versions (Windows 10 → latest)
<!-- - Offer **hands-on debugging, visualizations, and PoCs** using real-world tools (Windbg, custom tooling) -->

---

## Table of Contents

### Heap Internals Breakdown

- [**Overview**](./internals/overview.md)
- [**NTHeap**](./internals/nt_heap.md)
---

## Audience & Use Cases

This repository is designed for:

- **Exploit Developers** – crafting Windows heap exploits and understanding allocator behavior
- **Security Researchers** – analyzing OS-level mitigations and memory protections
- **Reverse Engineers** – diving deep into undocumented or barely-documented heap logic
- **Learners** – gaining hands-on experience with real-world allocators and PoCs

---

## Licensing

This project is licensed under the terms of the [MIT License](./LICENSE).

---

## Built by [PwnFuzz](https://pwnfuzz.com)

> Precision in Exploitation.  
> High-Impact, Research-Driven Security Projects.
