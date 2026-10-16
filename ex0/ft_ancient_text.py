import sys
from typing import TextIO


def read_file(file_name: str) -> str | None:
    archive: TextIO | None = None
    try:
        archive = open(file_name, "r", encoding="utf-8")
        return archive.read()
    except (OSError, UnicodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    finally:
        if archive is not None:
            archive.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    content = read_file(file_name)
    if content is None:
        return
    print("---\n")
    print(content, end="" if content.endswith("\n") else "\n")
    print("\n---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
