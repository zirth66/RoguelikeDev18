import tcod as libtcod

from input_handlers import handle_keys

def main():
	screen_width = 80
	screen_height = 50

	# Place the player in the middle of the screen
	player_x = int(screen_width / 2)
	player_y = int(screen_height / 2)

	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

	libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

	con = libtcod.console_new(screen_width, screen_height)

	key = libtcod.Key()
	mouse = libtcod.Mouse()	

# Game loop, closes when windows is closed

	while not libtcod.console_is_window_closed():
		# captures user input
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		
		# 0 = console we are drawing to, color for @ symbol = white
		libtcod.console_set_default_foreground(con, libtcod.white)
		# 0 = console, player coordinates
		libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)

		libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

		#presents everything to screen
		libtcod.console_flush()

		libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)

		# We're capturing the return value of handle_keys in the variable action 
		# (which should be a dictionary, no matter what we pressed), and checking
		# what keys are inside it. If it contains a key called 'move', 
		# then we know to look for the (x, y) coordinates. If it contains 'exit', 
		# then we know we need to exit the game.
		action = handle_keys(key)

		move = action.get('move')
		exit = action.get('exit')
		fullscreen = action.get('fullscreen')

		if move:
			dx, dy = move
			player_x += dx
			player_y += dy

		if exit:
			return True

		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())





if __name__ == '__main__':

	main()