import os
import shutil


def move(anime_name: str, is_move: int) -> None:
    parent_path = "D:/videos/anime"

    os.chdir(os.path.join(parent_path, "raw"))

    num_of_digits = len(str(len(os.listdir())))

    anime_path = os.path.join(parent_path, anime_name)

    if not os.path.isdir(anime_path):
        os.mkdir(anime_path)

    for file in os.listdir():
        file_num, file_ext = os.path.splitext(file)
        file_num = file_num.split()[-1]

        if "_" in file_num:
            file_num = file_num.split("_")[1]
        else:
            file_num = "1"

        file_num = file_num.zfill(num_of_digits)
        new_name = f"{file_num} {anime_name}{file_ext}"
        new_full_path = os.path.join(anime_path, new_name)
        print(f"{file}\n--> {new_full_path}\n")

        if is_move:
            shutil.move(file, new_full_path)
