from pathlib import Path

# Define directory structure
structure = {
    "heap-playground": [
        "docs",
        "internals",
        "mitigations",
        "exploits",
        "codewalks",
        "diagrams",
        "tools",
        "notes"
    ]
}

# Define README.md content
readme_content = """# 🔥 heap-playground  
**The Definitive Windows Heap Internals & Exploitation Suite**  
_A PwnFuzz Flagship Research Project_

---

## 🧠 What is this?

`heap-playground` is a research-grade deep-dive into **Windows usermode heap internals** and **exploitation**, designed to serve both as an educational platform and a practical exploit development reference.

This repository covers:

- ✔️ **NT Heap**, **LFH**, and **Segment Heap** internals  
- ✔️ Heap allocation workflows: `HeapAlloc`, `HeapCreate`, `malloc`, etc.  
- ✔️ Real-world **heap mitigations** and how to analyze/bypass them  
- ✔️ **Modern heap exploitation** on Windows 10+  
- ✔️ Reproducible PoCs, walkthroughs, and debug scripts  

---

## 🎯 Goals

- **Build the most complete and up-to-date heap internals walkthrough**
- Provide **reproducible PoCs** that demonstrate exploitation on real Windows versions
- Serve as a **reference base** for reverse engineers, exploit devs, and security researchers
- Be the **gold standard** for Windows heap understanding within the infosec community

---

## 🧭 Scope

- Windows 10 and later (x64)
- Focus on **usermode** heap internals (kernel heap will be separate)
- Uses **WinDbg**, **MSVC**, and **hand-written PoCs** where possible
- Exploit mitigations like **safe unlinking**, **heap isolation**, **LFH hardening**, and **segmented heap**
- Real exploit development with step-by-step debugging where applicable

---

## 🗂️ Project Structure

\`\`\`bash
heap-playground/
├── README.md           # This file
├── GOALS.md            # In-depth project goals
├── SCOPE.md            # Technical boundaries
├── docs/               # Architecture diagrams, glossary, references
├── internals/          # Heap internals: NT, LFH, Segment Heap
├── mitigations/        # In-depth breakdown of modern protections
├── exploits/           # Real exploit PoCs (uaf, overflow, double free, etc.)
├── codewalks/          # Heap functions behavior walkthroughs
├── diagrams/           # Visuals, memory layout diagrams, debug snapshots
├── tools/              # Helper scripts, Windbg commands, visualization tools
├── notes/              # TODOs, changelog, rough ideas
└── LICENSE             # Chosen license (MIT recommended)
\`\`\`

---

## ⚒️ Dependencies

- Windows 10+ (x64)
- MSVC or Mingw for PoC compilation
- [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) or WinDbg Preview
- VM or live box for testing safely

---

## 👀 Coming Soon

- 🧩 Segment Heap exploitation walkthrough  
- 🧠 CVE-case studies with heap involvement  
- 📦 Heap visualizer tool for allocations  
- 💥 Full series of fuzzable scenarios using custom allocators

---

## 🔗 References

- *Windows Internals* (Pavel Yosifovich et al.)
- *The Art of Memory Forensics* (Ligh, Adair, et al.)
- MSDN + Heap API docs
- Real CVEs and Pwn2Own writeups

---

## 🧪 Brought to you by [PwnFuzz](https://pwnfuzz.com)

Make exploitation elegant again.
"""

# Create folder structure and write README.md
base = Path("/mnt/data/heap-playground")
(base / "heap-playground").mkdir(parents=True, exist_ok=True)

for folder in structure["heap-playground"]:
    (base / "heap-playground" / folder).mkdir(parents=True, exist_ok=True)

# Write the README
readme_path = base / "heap-playground" / "README.md"
readme_path.write_text(readme_content)

# Create GOALS.md and SCOPE.md as placeholders
(base / "heap-playground" / "GOALS.md").write_text("# 🎯 Project Goals\n\n(Coming soon)")
(base / "heap-playground" / "SCOPE.md").write_text("# 🧭 Project Scope\n\n(Coming soon)")

# Output the base directory
base / "heap-playground"
