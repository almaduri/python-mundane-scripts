import os
import subprocess


class Anime:
    def __init__(self) -> None:
        self.__parent_path = 'D:\\Videos\\anime\\'

    @staticmethod
    def get_num_of_digits(list_of_files: list) -> int:
        return len(str(len(list_of_files)))

    @staticmethod
    def get_file_num(num_to_extract: str, starting_episode: int) -> str:
        file_num = num_to_extract.split()[-1]

        if '_' in file_num:
            file_num = int(file_num.split('_')[1])
            file_num = starting_episode + file_num - 1
        else:
            file_num = starting_episode

        file_num = str(file_num)

        return file_num

    def move_to_dir_according_to_name(self,
                                      anime_name: str,
                                      digits: int,
                                      change_digits: int,
                                      starting_episode: int,
                                      is_move: int) -> None:
        os.chdir(os.path.join(self.__parent_path, 'raw'))

        # Get the total number of digits
        if change_digits:
            num_of_digits = digits
        else:
            num_of_digits = Anime.get_num_of_digits(os.listdir())

        anime_path = os.path.join(self.__parent_path, anime_name)

        # Create new directory, if directory doesn't exist
        if not os.path.isdir(anime_path):
            os.mkdir(anime_path)

        for file in os.listdir():
            num_to_extract, _ = os.path.splitext(file)
            file_num = Anime.get_file_num(num_to_extract, starting_episode)

            file_num = file_num.zfill(num_of_digits)
            new_name = f'{file_num} {anime_name}.mkv'
            new_full_path = os.path.join(anime_path, new_name)

            print(f'{file}\n--> {new_full_path}\n')

            if is_move:
                subprocess.run(['mkvmerge', '-q', '-o', new_full_path, file])

        if is_move:
            subprocess.run(['pwsh', '-Command', 'rm', '*.ts'])
