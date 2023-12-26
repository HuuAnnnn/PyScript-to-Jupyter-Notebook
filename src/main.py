import os
import re


ROOT_PATH_FOLDER = "./samples"
SRC_FILE = "train.py"
TARGET_FILE = "result.ipynb"


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


def extract_import_and_script(script: str, pattern: str):
    pattern = re.compile(r"(?<=\bdef\b)", re.DOTALL | re.MULTILINE)


if __name__ == "__main__":
    ignore = ["__pycache__"]
    print(load_file_from_folder(ROOT_PATH_FOLDER, ignore))
