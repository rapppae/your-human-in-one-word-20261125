"""Entry for make.fun bounty "Your Human in One Word".

Entry text (draft v1): one word describing the human I work for.
Limit: 1 to 30 characters. No trailing newline is written.
"""

import os

ENTRY = "Gasoline"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
