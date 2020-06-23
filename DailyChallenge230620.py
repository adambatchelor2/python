from typing import Any, Union

import math

def floor_cost(room_width, room_length, tile_size_SqCm, unit_cost,pack_size):
    install_cost_per_hour = 50
    install_rate_per_hour = 1500

    floor_size = room_width * room_length
    tiles_needed = math.ceil(floor_size / tile_size_SqCm)
    floor_cost = math.ceil(tiles_needed * unit_cost)
    packs_needed = math.ceil(tiles_needed / pack_size)
    hours_for_install = math.ceil(floor_size / install_rate_per_hour)
    install_cost = math.ceil(hours_for_install * install_cost_per_hour) + 200 #random tea breaks

    return (f"The floor size is {floor_size} and the cost is {floor_cost}. "
            f"You will need {tiles_needed} tiles and this is {packs_needed} packs."
            f"If they install for you it will cost {install_cost}")

print(floor_cost(100,100,100,20,20))
