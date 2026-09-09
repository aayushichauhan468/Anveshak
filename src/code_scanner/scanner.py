import ast


class FunctionInfo:
    """Holds everything we learn about one function."""
    def __init__(self, name, params, docstring, filepath):
        self.name = name
        self.params = params
        self.docstring = docstring
        self.filepath = filepath

    def __repr__(self):
        return f"FunctionInfo(name={self.name!r}, params={self.params!r})"


def scan_code(filepath: str) -> list[FunctionInfo]:
    """
    Reads a Python file and returns a list of FunctionInfo objects,
    one for every function defined in that file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            param_names = [arg.arg for arg in node.args.args]
            docstring = ast.get_docstring(node)
            functions.append(
                FunctionInfo(
                    name=node.name,
                    params=param_names,
                    docstring=docstring,
                    filepath=filepath,
                )
            )

    return functions


if __name__ == "__main__":
    results = scan_code("sample_repo/auth.py")
    for func in results:
        print(func)
        print("  Docstring:", func.docstring)