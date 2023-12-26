import os
import re


def load_file_from_folder(path: str, ignore: list[str] = []) -> list[str]:
    assert os.path.isdir(path), "The path must be a folder"
    traverse_files = os.listdir(path)
    sub_files = []

    # Using recursion to load all file from path
    for file_path in traverse_files:
        full_file_path = os.path.join(path, file_path)
        if os.path.isdir(full_file_path) and file_path not in ignore:
            folder_sub_files = load_file_from_folder(full_file_path, ignore)
            sub_files.append((file_path, folder_sub_files))

        # We just concern to the python script file for converting purpose
        if ".py" in file_path:
            sub_files.append(file_path)

    return sub_files


def load_file(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()

    return data


def get_script_from_folder(folder_structure: list) -> list[str]:
    script_files = []
    for child in folder_structure:
        if type(child) == tuple:
            _, files = child
            script_files.extend(files)
        else:
            script_files.append(child)
    return script_files


def extract_import_and_script(
    script: str,
    pattern: str = r"(?<=\bdef\b)",
) -> tuple[str, str]:
    pattern = re.compile(pattern, re.DOTALL | re.MULTILINE)
    match = pattern.search(script)
    if match:
        # Extract import and script parts
        import_part = script[: match.start()]
        script_part = script[match.start() :]
        return import_part, script_part
    else:
        raise Exception("Not found")


if __name__ == "__main__":
    ROOT_PATH_FOLDER = "./samples"
    SRC_FILE = "train.py"
    TARGET_FILE = "result.ipynb"
    ignore = ["__pycache__"]
    files = load_file_from_folder(ROOT_PATH_FOLDER, ignore)
    scripts = get_script_from_folder(files)
