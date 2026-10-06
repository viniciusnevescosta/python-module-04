def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r", encoding="utf-8") as archive:
                return (True, archive.read())
        if action == "write":
            with open(file_name, "w", encoding="utf-8") as archive:
                archive.write(content)
            return (True, "Content successfully written to file")
        return (False, f"Unknown archive action: '{action}'")
    except (OSError, UnicodeError) as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive(__file__)
    print((success, content))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("vault_copy.txt", "write", content))


if __name__ == "__main__":
    main()
