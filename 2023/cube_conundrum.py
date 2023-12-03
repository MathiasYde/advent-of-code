from typing import List, Dict
from pprint import pprint

INPUT_FILEPATH = "cube_conundrum.txt"

def parse_input_file(file) -> List[List[Dict]]:
    games: Dict[List[Dict]] = {}
    
    for line in file.readlines():
        start_delimiter = line.find(":") # find first :
        substring = line[start_delimiter + 1:].strip()
        game_id = line[:start_delimiter].split(" ")[1]
        
        games[game_id] = []
        for subset in substring.split(";"):
            subset = subset.strip()
            subset_data = {}
            for subcolor in subset.split(","):
                subcolor = subcolor.strip()
                count, color = subcolor.split(" ")
                subset_data[color] = int(count)
            games[game_id].append(subset_data)
            
    return games

def cube_conundrum_part1():
    with open(INPUT_FILEPATH, "r") as file:
        data = parse_input_file(file)

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    game_id_sum = 0
    
    for game_id, game in data.items():
        disqualify_game = False
        for subgame in game:
            for color, color_count in subgame.items():
                max_count = max_cubes.get(color)
                if color_count > max_count:
                    disqualify_game = True
        
        if disqualify_game == False:
            game_id_sum += int(game_id)
            
    print(f"{game_id_sum=}")

def cube_conundrum_part2():
    with open(INPUT_FILEPATH, "r") as file:
        data = parse_input_file(file)
    
    power_sum = 0
    for game in data.values():
        minimum_cubes = {"green":0,"blue":0,"red":0}
        for subset in game:
            for color, count in subset.items():
                minimum_cubes[color] = max(minimum_cubes[color], count)
        
        power = minimum_cubes["green"] * minimum_cubes["red"] * minimum_cubes["blue"]
        print(minimum_cubes, power)
        power_sum += power
        
    print(f"{power_sum=}")

def main():
    cube_conundrum_part2()

if __name__ == "__main__":
    main()
