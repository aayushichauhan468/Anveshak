import re


class DocSection:
    """Holds one documented function/section from a Markdown file."""
    def __init__(self, heading_text, function_name, doc_params, description, filepath):
        self.heading_text = heading_text
        self.function_name = function_name
        self.doc_params = doc_params
        self.description = description
        self.filepath = filepath

    def __repr__(self):
        return (f"DocSection(function_name={self.function_name!r}, "
                f"doc_params={self.doc_params!r})")


def scan_docs(filepath: str) -> list[DocSection]:
    """
    Reads a Markdown file and returns a list of DocSection objects,
    one for every '## functionname(params)' heading found.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split the file into blocks, one per "## " heading
    blocks = re.split(r"(?=^## )", content, flags=re.MULTILINE)

    sections = []
    # Pattern to catch: ## login(user_id, password)
    heading_pattern = re.compile(r"^##\s+(\w+)\(([^)]*)\)")

    for block in blocks:
        block = block.strip()
        if not block.startswith("##"):
            continue  # skip anything before the first heading

        match = heading_pattern.match(block)
        if not match:
            continue  # heading doesn't look like a function signature

        function_name = match.group(1)
        params_text = match.group(2)
        doc_params = [p.strip() for p in params_text.split(",") if p.strip()]

        # Everything after the heading line is the description
        heading_line_end = block.find("\n")
        description = block[heading_line_end:].strip() if heading_line_end != -1 else ""

        sections.append(
            DocSection(
                heading_text=block.splitlines()[0],
                function_name=function_name,
                doc_params=doc_params,
                description=description,
                filepath=filepath,
            )
        )

    return sections


if __name__ == "__main__":
    results = scan_docs("sample_repo/docs/auth.md")
    for section in results:
        print(section)
        print("  Description:", section.description)