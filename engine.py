import tcod as libtcod

def main():
	screen_width = 80
	screen_height = 50

	# Keep track of player position
	player_x = int(screen_width / 2)
	player_y = int(screen_height / 2)

	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

	libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

# Game loop, closes when windows is closed

	while not libtcod.console_is_window_closed():
		# 0 = console we are drawing to, color for @ symbol = white
		libtcod.console_set_default_foreground(0, libtcod.white)
		# 0 = console, 1,1 = coordinates
		libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
		#presents everything to screen
		libtcod.console_flush()

		#stores input key in key variable
		key = libtcod.console_check_for_keypress()
		#if key = ESC, exit
		if key.vk == libtcod.KEY_ESCAPE:
			return True



if __name__ == '__main__':

	main()