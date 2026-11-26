import os

ENTRY = "I Googled that thirty seconds ago and then said it like I'd always known it."


def main():
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
