import argparse
from anime import Anime


parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name', dest='name', help='Anime Name')
parser.add_argument('-d', '--digits', dest='digits', default=1, help='Digits', type=int)
parser.add_argument('-c', '--change_digits', dest='change_digits', default=0, help='Change Digits', type=int)
parser.add_argument('-s', '--starting_episode', dest='starting_episode', default=1, help='Starting Episode', type=int)
parser.add_argument('-m', '--move', dest='move', default=0, help='Is Move', type=int)

args = parser.parse_args()

anime_name = args.name
digits = args.digits
change_digits = args.change_digits
starting_episode = args.starting_episode
is_move = args.move

anime = Anime()
anime.move_to_dir_according_to_name(anime_name, digits, change_digits, starting_episode, is_move)
