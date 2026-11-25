import os
import sys


def main() -> int:
    """Write the battery's last text to its charger as entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.
    LINE = "Performance review: availability 0/10, communication 'omw' since breakfast, reliability — actually showed up at 1% like a guy texting 'u up?' at 2am. Terminated."
    content = LINE + "\n"

    # Validate
    if not (1 <= len(content) <= 200):
        raise ValueError(f"content length {len(content)} not in 1..200")
    if not content.strip():
        raise ValueError("content is only whitespace")
    if content.count('\n') != 1:
        raise ValueError(f"content has {content.count(chr(10))} newlines, expected exactly 1")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort mirror to /output/entry.txt if different
    if os.path.abspath(output_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(f"{output_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
