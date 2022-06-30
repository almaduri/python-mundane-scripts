import argparse
import os
import shutil


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", dest="name", help="Anime Name")
parser.add_argument("-o", "--option", dest="option", help="Option")
parser.add_argument("-m", "--move", dest="move", default=0, help="Is Move", type=int)

args = parser.parse_args()

anime_name = args.name
option = args.option
is_move = args.move


def anime() -> None:
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


def t7() -> None:
    os.chdir("D:/videos/t7/raw")

    programs_list = {
        "LAPOR PAK!" : "D:/videos/t7/lapor-pak!",
        "BTS" : "D:/videos/t7/bts"
    }


    def find_program(file_name: str, left_parentheses_index: int, right_parentheses_index: int) -> str:
        file_name_list = file_name.split(" ")
        date = file_name[left_parentheses_index:right_parentheses_index + 1]

        for index, value in enumerate(file_name_list):
            if date in value:
                return file_name_list[index - 1]


    def move_file(file_name: str) -> None:
        left_parentheses_index = file_name.rindex("(")
        right_parentheses_index = file_name.rindex(")")
        date_folder = file_name[left_parentheses_index + 1:right_parentheses_index]
        date = date_folder.replace(file_name[left_parentheses_index + 3], "-")

        program_name = find_program(file_name, left_parentheses_index, right_parentheses_index).casefold()

        if "bts" in program_name:
            program_path = programs_list["BTS"]
        elif "pak" in program_name:
            program_path = programs_list["LAPOR PAK!"]

        date_path = os.path.join(program_path, date)

        if not os.path.isdir(date_path):
            os.mkdir(date_path)
        
        old_name, ext = os.path.splitext(file_name)
        file_num = old_name.casefold().split("part")[1].strip()
        new_name = f"{file_num} - {old_name}{ext}"
        new_full_path = os.path.join(program_path, date, new_name)
        print(f"{file_name}\n--> {new_full_path}\n")

        if is_move:
            shutil.move(file_name, new_full_path)


    for file_name in os.listdir():
        move_file(file_name)


match option.casefold():
    case "anime":
        anime()
    case "t7":
        t7()
    case _:
        print("Not Found")
