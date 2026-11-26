#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — writes one fortune cookie line to entry.txt."""
import os


def main():
    line = "The bug you have hunted for three days lives in the line you keep skipping because it looks fine."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
