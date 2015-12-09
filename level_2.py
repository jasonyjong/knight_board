#!/usr/bin/env python

import tools

# global variables for board
width = 8
height = 8

def main():
	print "What is the start location?"
	start_x_coor, start_y_coor = tools.get_input_coordinates(width, height)

	print "What is the end location?"
	unique_end_coor = False
	while not unique_end_coor:
		end_x_coor, end_y_coor = tools.get_input_coordinates(width, height)
		if (start_x_coor == end_x_coor) and (start_y_coor == end_y_coor):
			print "Same as start.  Enter new end location:"
			unique_end_coor =  False
		else:
			unique_end_coor =  True

	# initialize start/end points
	board = [['.' for x in range(height)] for x in range(width)]
	board[start_x_coor][start_y_coor] = 'S'
	board[end_x_coor][end_y_coor] = 'E'

	# initialize to memorize order of moves in each spot
	board_with_moves = [['.' for x in range(height)] for x in range(width)]
	board_with_moves[start_x_coor][start_y_coor] = []

	# continue loop until we hit step in which nothing changes.
	continue_loop = True
	current_step = 0
	while continue_loop:
		continue_loop = False

		for y in range(len(board[0])):
			for x in range(len(board)):
				if board_with_moves[x][y] != '.' and len(board_with_moves[x][y]) == current_step:
					modified = draw_knight_move(board_with_moves, x, y)
					if modified:
						continue_loop = True

		# shortest move found! We can now print results and exit.
		if board_with_moves[end_x_coor][end_y_coor] != '.':
			move_to_end = board_with_moves[end_x_coor][end_y_coor]

			# print the move number in each spot
			for num_move in range(1, len(move_to_end)):
				x, y = tools.string_to_coor(move_to_end[num_move])
				board[x][y] = num_move

			tools.print_board(board)

			# print sequence of move
			print 'Sequence of moves: '
			for num_move in range(0, len(move_to_end)):
				x, y = tools.string_to_coor(move_to_end[num_move])
				print '(' , x, ', ', y, ')'
			print '(' , end_x_coor, ', ', end_y_coor, ')'

			exit()

		current_step += 1

def draw_knight_move(board, x_coor, y_coor):
	modified = False
	if (x_coor - 2) >= 0 and (y_coor - 1) >= 0:
		val = board[x_coor - 2][y_coor - 1]
		# if we have never landed on element
		if val == '.':
			board[x_coor - 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor - 2) >= 0 and (y_coor + 1) < height:
		val = board[x_coor - 2][y_coor + 1]
		if val == '.':
			board[x_coor - 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor + 2) < width and (y_coor - 1) >= 0:
		val = board[x_coor + 2][y_coor - 1]
		if val == '.':
			board[x_coor + 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor + 2) < width and (y_coor + 1) < height:
		val = board[x_coor + 2][y_coor + 1]
		if val == '.':
			board[x_coor + 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor - 1) >= 0 and (y_coor - 2) >= 0:
		val = board[x_coor - 1][y_coor - 2]
		if val == '.':
			board[x_coor - 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor - 1) >= 0 and (y_coor + 2) < height:
		val = board[x_coor - 1][y_coor + 2]
		if val == '.':
			board[x_coor - 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor + 1) < width and (y_coor - 2) >= 0:
		val = board[x_coor + 1][y_coor - 2]
		if val == '.':
			board[x_coor + 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	if (x_coor + 1) < width and (y_coor + 2) < height:
		val = board[x_coor + 1][y_coor + 2]
		if val == '.':
			board[x_coor + 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			modified = True

	return modified

if __name__ == "__main__":
    main()
