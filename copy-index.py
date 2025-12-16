from pathlib import Path
import shutil

html_dir = Path("html")
output_dir = Path("output")

# Find all .tree files in html/ directory
for tree_file in html_dir.glob("*.tree"):
    # Extract the base name (e.g., "bool" from "bool.tree")
    base_name = tree_file.stem

    # Define source and destination paths
    source = output_dir / base_name / "index.html"
    destination = output_dir / base_name / f"{base_name}.html"

    # Copy the file if source exists
    if source.exists():
        print(f"Copying {source} -> {destination}")
        shutil.copy2(source, destination)
    else:
        print(f"Warning: {source} does not exist, skipping")
