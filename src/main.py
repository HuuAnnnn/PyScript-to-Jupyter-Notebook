import os
import re
import nbformat


def tree(path: str) -> list[str | list[str]]:
    assert os.path.isdir(path), "The path must be a folder"
    traverse_files = os.listdir(path)
    folder_structure = []
    for file in traverse_files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            children_files = tree(file_path)
            folder_structure.append((file, children_files))
        else:
            folder_structure.append(file)
    return folder_structure


def find_path_file(parent: str, file_name: str):
    path = []
    traverse_files = os.listdir(parent)
    for file in traverse_files:
        file_path = os.path.join(parent, file)
        if file_name == file:
            path.extend([parent, file])
            return path
        if os.path.isdir(file_path):
            sub_path = find_path_file(file_path, file_name)
            if sub_path:
                path.extend(sub_path)
                return path


def get_path_of_file(parent: str, file_name: str) -> str:
    path = find_path_file(parent, file_name)
    return os.path.join(*path)


def load_file(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()

    return data


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


def is_custom_package(import_script: str, script_files: list[str]) -> bool:
    for script_file in script_files:
        # Removing .py for comparing purpose
        if script_file.replace(".py", "") in import_script:
            return True
    return False


def classify_library(import_script: str):
    lines = import_script.split("\n")
    for line in lines:
        pass


if __name__ == "__main__":
    ROOT_PATH_FOLDER = "./samples"
    SRC_FILE = "./samples/train.py"
    TARGET_FILE = "result.ipynb"

    # target_content = load_file(SRC_FILE)
    # import_part, script_part = extract_import_and_script(target_content)
    print(get_path_of_file(ROOT_PATH_FOLDER, "node2vec.py"))
