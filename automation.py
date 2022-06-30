import argparse
import anime
import t7


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", dest="name", help="Anime Name")
parser.add_argument("-o", "--option", dest="option", help="Option")
parser.add_argument("-m", "--move", dest="move", default=0, help="Is Move", type=int)

args = parser.parse_args()

anime_name = args.name
option = args.option
is_move = args.move

match option.casefold():
    case "anime":
        anime.move(anime_name, is_move)
    case "t7":
        t7.move(is_move)
    case _:
        print("Not Found")
