import sys
sys.path.append("src")

from code_scanner.scanner import scan_code
from doc_scanner.scanner import scan_docs

code_functions = scan_code("sample_repo/auth.py")
doc_sections = scan_docs("sample_repo/docs/auth.md")

print(f"Found {len(code_functions)} functions in code.")
print(f"Found {len(doc_sections)} sections in docs.\n")

doc_lookup = {doc.function_name: doc for doc in doc_sections}

mismatches = []
matched_ok = []

for func in code_functions:
       matching_doc = doc_lookup.get(func.name)

       if matching_doc is None:
           print(f"⚠️  '{func.name}' exists in code but has NO documentation at all.")
           continue

       if set(func.params) != set(matching_doc.doc_params):
           mismatches.append((func, matching_doc))
       else:
           matched_ok.append(func.name)

print("✅ Correctly documented functions:", matched_ok)
print()
print(f"🚨 {len(mismatches)} mismatch(es) detected:\n")

for func, doc in mismatches:
       print(f"  Function: {func.name}")
       print(f"    Code params: {func.params}")
       print(f"    Doc params:  {doc.doc_params}")
       print()