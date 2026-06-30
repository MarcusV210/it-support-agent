import os
import re
from datetime import datetime

# pyrefly: ignore [missing-import]
import mammoth
# pyrefly: ignore [missing-import]
import pymupdf4llm


INPUT_DIR = "./docs/input"
OUTPUT_DIR = "./docs/md_input"
LOG_FILE = f"{OUTPUT_DIR}/conversion.log"


def clean_markdown(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def add_frontmatter(text, filename):
    return (
        "---\n"
        f"source: {filename}\n"
        f"converted: {datetime.now().strftime('%Y-%m-%d')}\n"
        "---\n\n"
        f"{text}"
    )


def convert_pdf(filepath):
    return pymupdf4llm.to_markdown(
        filepath,
        show_progress=False
    )


def convert_docx(filepath):
    with open(filepath, "rb") as f:
        result = mammoth.convert_to_markdown(f)

    return result.value


def convert_txt(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def convert_file(filepath):
    filename = os.path.basename(filepath)
    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".pdf":
        markdown = convert_pdf(filepath)

    elif extension == ".docx":
        markdown = convert_docx(filepath)

    elif extension in [".txt", ".md"]:
        markdown = convert_txt(filepath)

    else:
        raise ValueError(f"Unsupported file type: {extension}")

    markdown = clean_markdown(markdown)
    markdown = add_frontmatter(markdown, filename)

    output_file = os.path.join(
        OUTPUT_DIR,
        os.path.splitext(filename)[0] + ".md"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)


def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    for filename in os.listdir(INPUT_DIR):
        filepath = os.path.join(INPUT_DIR, filename)

        if not os.path.isfile(filepath):
            continue

        try:
            convert_file(filepath)
            write_log(f"SUCCESS | {filename}")

        except Exception as e:
            write_log(f"FAILED | {filename} | {e}")


if __name__ == "__main__":
    main()