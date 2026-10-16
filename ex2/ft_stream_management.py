import sys
from typing import TextIO


def report_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr, flush=True)


def read_file(file_name: str) -> str | None:
    archive: TextIO | None = None
    try:
        archive = open(file_name, "r", encoding="utf-8")
        return archive.read()
    except (OSError, UnicodeError) as error:
        report_error(f"Error opening file '{file_name}': {error}")
        return None
    finally:
        if archive is not None:
            archive.close()


def transform_content(content: str) -> str:
    transformed = ""
    for line in content.splitlines():
        transformed += line + "#\n"
    return transformed


def save_file(file_name: str, content: str) -> bool:
    archive: TextIO | None = None
    try:
        archive = open(file_name, "w", encoding="utf-8")
        archive.write(content)
        archive.flush()
        return True
    except (OSError, UnicodeError) as error:
        report_error(f"Error opening file '{file_name}': {error}")
        return False
    finally:
        if archive is not None:
            archive.close()


def get_destination() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        report_error("Usage: ft_stream_management.py <file>")
        return

    source_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{source_name}'")
    content = read_file(source_name)
    if content is None:
        return
    print("---\n")
    print(content, end="" if content.endswith("\n") else "\n")
    print("\n---")
    print(f"File '{source_name}' closed.")

    transformed = transform_content(content)
    print("\nTransform data:")
    print("---\n")
    print(transformed, end="")
    print("\n---")
    destination = get_destination()
    if destination == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{destination}'")
    if save_file(destination, transformed):
        print(f"Data saved in file '{destination}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
