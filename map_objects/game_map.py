from map_objects.tile import Tile 

"""
We're passing in the width and height of the map (which we've defined in our engine), and initializing a 
2d array of Tiles, set to non-blocking by default. We're setting a few tiles as blocked, just for 
demonstration purposes. I've kept the code setting the tiles up out of the __init__ function, for two reasons. 
One, it may get called outside the initialization, and two, because I prefer keeping __init__ functions 
as simple as possible.
"""
class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = self.initialize_tiles()

	def initialize_tiles(self):
		tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

		# Demonstraition of blocked tiles
		tiles[30][22].blocked = True
		tiles[30][22].block_sight = True
		tiles[31][22].blocked = True
		tiles[31][22].block_sight = True
		tiles[32][22].blocked = True
		tiles[32][22].block_sight = True

		return tiles

	def is_blocked(self, x, y):
		if self.tiles[x][y].blocked:
			return True

		return False