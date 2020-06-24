"""
Title: Find Cost of Tile to Cover W x L Floor
Description:
Ask the user to enter in a width, length and the cost per 1 unit of flooring.
Have the program calculate how much it would cost to cover the area specified with the flooring.
Tips:
This is a relatively simple program. Be sure to first find out how much area the floor is
and then multiply that by the cost per unit of flooring. Start with some simple numbers that you
can quickly calculate in your head. Try a 100 x 100 cm room with each unit of flooring costing £1.00.
Added Difficulty:
How many packs of tiles would be needed? Also figure
out how much labor costs would be given that the average flooring team can only put in 5000 square cm
of flooring per hour at a cost of £50.00/hr.
"""
# Imports
from math import ceil  # import the ceil function, this is a round up function


# Classes
class tile:
    def __init__(self, width, length, pack, cost):
        self.width = width
        self.length = length
        self.pack = pack
        self.cost = cost
        self.area = self._area()

    def _area(self):
        return self.width * self.length

    def __str__(self):
        return f"<width: {self.width}; length: {self.length}; pack: {self.pack}; cost: {self.cost}; area: {self.area}>"


class floor:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = self._area()

    def _area(self):
        return self.width * self.length

    def __str__(self):
        return f"<width: {self.width}; length: {self.length}; area: {self.area}>"


class quote:
    def __init__(self, tile, floor):
        self.hourly_rate = 50.0
        self.hourly_area = 5000
        self.breakages = 0.05
        self.tile = tile
        self.floor = floor
        self.needed_net = self._needed_net()
        self.needed_gross = self._needed_gross()
        self.packs = self._packs()
        self.price = self._price()
        self.labour = self._labour()
        self.total = self._total()

    def _needed_net(self):
        return self.floor.area / self.tile.area

    def _needed_gross(self):
        need = (self.floor.area / self.tile.area)
        breakages = need * self.breakages
        return ceil(need + breakages)

    def _packs(self):
        return ceil(self.needed_gross / self.tile.pack)

    def _price(self):
        return float(self.packs * self.tile.cost)

    def _labour(self):
        return float(ceil(self.floor.area / self.hourly_area) * self.hourly_rate)

    def _total(self):
        return float(self.price + self.labour)

    def __str__(self):
        output = "\n\n"
        output += '\n' + ("=" * 44)
        output += "\n          ____              _\n         / __ \            | |\n        | |  | |_   _  ___ | |_ ___\n        | |  | | | | |/ _ \| __/ _ \\\n        | |__| | |_| | (_) | ||  __/\n         \___\_\\\__,_|\___/ \__\___|"
        output += '\n' + ("=" * 44)
        output += f"\nTile(s): L: {self.tile.length}cm, W: {self.tile.width}cm"
        output += f"\nPack: {self.tile.pack}, Cost (each): £{self.tile.cost}"
        output += f"\nRoom: L: {self.floor.length}cm, W: {self.floor.width}cm"
        output += '\n' + ("-" * 44)
        output += f"\nTiles Needed: {self.needed_gross}, Price For Tiles: £{self.price}"
        output += f"\nPacks: {self.packs}"
        output += f"\nLabour @ £{self.hourly_rate} per {self.hourly_area}cm: £{self.labour}"
        output += '\n' + ("=" * 44)
        output += f"\nTOTAL inc Labour: £{self.total}"
        output += '\n' + ("=" * 44)
        output += "\n\n"
        return output

    # def print(self):
    #     with open('quote.txt', "w", "utf-8") as f:
    #         out = self.__str__()
    #         f.write(out)


# Main
t = tile(10, 10, 10, 5)
f = floor(100, 100)
q = quote(t, f)
q2 = quote(tile(10, 10, 10, 5), floor(100, 100))
print(q)
print(q2)
q.print()