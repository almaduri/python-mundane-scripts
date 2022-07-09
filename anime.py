import os
import shutil


def get_num_of_digits(list_of_files: list) -> int:
    return len(str(len(list_of_files)))


def is_dir_exist(dir: str) -> bool:
    return os.path.isdir(dir)


def get_file_num(num_to_extract: str) -> str:
    file_num = num_to_extract.split()[-1]

    if "_" in file_num:
        file_num = file_num.split("_")[1]
    else:
        file_num = "1"
    
    return file_num


def move_to_dir_according_to_name(anime_name: str, is_move: int) -> None:
    parent_path = "D:\\videos\\anime"

    os.chdir(os.path.join(parent_path, "raw"))

    # Get the total number of digits
    num_of_digits = get_num_of_digits(os.listdir())

    anime_path = os.path.join(parent_path, anime_name)

    # Create new directory, if directory doesn't exist
    if not is_dir_exist(anime_path):
        os.mkdir(anime_path)

    for file in os.listdir():
        num_to_extract, file_ext = os.path.splitext(file)
        file_num = get_file_num(num_to_extract)

        file_num = file_num.zfill(num_of_digits)
        new_name = f"{file_num} {anime_name}{file_ext}"
        new_full_path = os.path.join(anime_path, new_name)
        print(f"{file}\n--> {new_full_path}\n")

        if is_move:
            shutil.move(file, new_full_path)
