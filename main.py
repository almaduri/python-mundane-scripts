import argparse
from anime import Anime
# import t7


parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name', dest='name', help='Anime Name')
parser.add_argument('-o', '--option', dest='option', help='Option')
parser.add_argument('-s', '--starting_episode', dest='starting_episode', default=1, help='Starting Episode', type=int)
parser.add_argument('-m', '--move', dest='move', default=0, help='Is Move', type=int)

args = parser.parse_args()

anime_name = args.name
option = args.option
starting_episode = args.starting_episode
is_move = args.move

if option:
    match option.casefold():
        case 'anime':
            anime = Anime()
            anime.move_to_dir_according_to_name(anime_name, starting_episode, is_move) if anime_name else print('No Name Specified')
        # case 't7':
        #     t7.move_to_dir_according_to_name(is_move)
        case _:
            print('Not Found')
else:
    print('No Option Specified')
