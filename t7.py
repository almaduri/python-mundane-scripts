import os
import shutil


os.chdir("")
# os.chdir("D:\\videos\\t7\\raw")

programs_list = {
    "LAPOR PAK!" : "",
    "BTS" : ""
    # "LAPOR PAK!" : "D:\\videos\\t7\\lapor-pak!",
    # "BTS" : "D:\\videos\\t7\\bts"
}


def find_program(file_name: str, left_parentheses_index: int, right_parentheses_index: int) -> str:
        file_name_list = file_name.split(" ")
        date = file_name[left_parentheses_index:right_parentheses_index + 1]

        for index, value in enumerate(file_name_list):
            if date in value:
                return file_name_list[index - 1]


def move_file(file_name: str, is_move: int) -> None:
    left_parentheses_index = file_name.rindex("(")
    right_parentheses_index = file_name.rindex(")")
    date_folder = file_name[left_parentheses_index + 1:right_parentheses_index]
    date = date_folder.replace(file_name[left_parentheses_index + 3], "-")
    day, month, year = date.split("-")
    
    if len(year) == 2:
        year = f"20{year}"

    date = f"{year}-{month}-{day}"

    program_name = find_program(file_name, left_parentheses_index, right_parentheses_index).casefold()

    if "bts" in program_name:
        program_path = programs_list["BTS"]
    elif "pak" in program_name:
        program_path = programs_list["LAPOR PAK!"]

    date_path = os.path.join(program_path, date)

    # Create new directory, if directory doesn't exist
    if not os.path.isdir(date_path):
        os.mkdir(date_path)
    
    old_name, ext = os.path.splitext(file_name)
    file_num = old_name.casefold().split("part")[1].strip()
    new_name = f"{file_num} - {old_name}{ext}"
    new_full_path = os.path.join(program_path, date, new_name)
    print(f"{file_name}\n--> {new_full_path}\n")

    if is_move:
        shutil.move(file_name, new_full_path)


def move_to_dir_according_to_name(is_move: int) -> None:
    for file_name in os.listdir():
        move_file(file_name, is_move)
