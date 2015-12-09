#!/usr/bin/env python

import tools

# global variables for board
width = 32
height = 32

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

	# initialize start/end
	board = [['.' for x in range(height)] for x in range(width)]
	board[start_x_coor][start_y_coor] = 'S'
	board[end_x_coor][end_y_coor] = 'E'

	# initialize board w/ moves
	board_with_moves = [['.' for x in range(height)] for x in range(width)]
	board_with_moves[start_x_coor][start_y_coor] = []

	board_with_moves_set = [['.' for x in range(height)] for x in range(width)]
	board_with_moves_set[start_x_coor][start_y_coor] = set([])

	continue_loop = True
	current_step = 0
	while continue_loop:
		continue_loop = False

		for y in range(len(board[0])):
			for x in range(len(board)):
				if board_with_moves[x][y] != '.' and len(board_with_moves[x][y]) == current_step:
					modified = draw_knight_move(board_with_moves, board_with_moves_set, x, y)
					if modified:
						continue_loop = True

		current_step += 1

		# print out percentage more to go through
		if current_step % 30 == 0:
			print 'About ', ( current_step / 10.24), '% done.'

	# shortest move found!
	move_to_end = board_with_moves[end_x_coor][end_y_coor]

	for num_move in range(1, len(move_to_end)):
		x, y = tools.string_to_coor(move_to_end[num_move])
		board[x][y] = num_move

	tools.print_board(board)

	print 'Sequence of moves: '
	for num_move in range(0, len(move_to_end)):
		x, y = tools.string_to_coor(move_to_end[num_move])
		print '(' , x, ', ', y, ')'
	print '(' , end_x_coor, ', ', end_y_coor, ')'

def draw_knight_move(board, board_with_moves_set, x_coor, y_coor):
	modified = False
	if (x_coor - 2) >= 0 and (y_coor - 1) >= 0:
		val = board[x_coor - 2][y_coor - 1]

		# if spot not already encountered in move...
		if tools.coor_to_string(x_coor - 2, y_coor - 1) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor - 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
			
			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor - 2, y_coor - 1))
			board_with_moves_set[x_coor - 2][y_coor - 1] = curr_set

			modified = True

	if (x_coor - 2) >= 0 and (y_coor + 1) < height:
		val = board[x_coor - 2][y_coor + 1]
		if tools.coor_to_string(x_coor - 2, y_coor + 1) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor - 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor - 2, y_coor + 1))
			board_with_moves_set[x_coor - 2][y_coor + 1] = curr_set

			modified = True

	if (x_coor + 2) < width and (y_coor - 1) >= 0:
		val = board[x_coor + 2][y_coor - 1]
		if tools.coor_to_string(x_coor + 2, y_coor - 1) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor + 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor + 2, y_coor - 1))
			board_with_moves_set[x_coor + 2][y_coor - 1] = curr_set

			modified = True

	if (x_coor + 2) < width and (y_coor + 1) < height:
		val = board[x_coor + 2][y_coor + 1]
		if tools.coor_to_string(x_coor + 2, y_coor + 1) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor + 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor + 2, y_coor + 1))
			board_with_moves_set[x_coor + 2][y_coor + 1] = curr_set

			modified = True

	if (x_coor - 1) >= 0 and (y_coor - 2) >= 0:
		val = board[x_coor - 1][y_coor - 2]
		if tools.coor_to_string(x_coor - 1, y_coor - 2) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor - 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor - 1, y_coor - 2))
			board_with_moves_set[x_coor - 1][y_coor - 2] = curr_set

			modified = True

	if (x_coor - 1) >= 0 and (y_coor + 2) < height:
		val = board[x_coor - 1][y_coor + 2]
		if tools.coor_to_string(x_coor - 1, y_coor + 2) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor - 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor - 1, y_coor + 2))
			board_with_moves_set[x_coor - 1][y_coor + 2] = curr_set

			modified = True

	if (x_coor + 1) < width and (y_coor - 2) >= 0:
		val = board[x_coor + 1][y_coor - 2]
		if tools.coor_to_string(x_coor + 1, y_coor - 2) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor + 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor + 1, y_coor - 2))
			board_with_moves_set[x_coor + 1][y_coor - 2] = curr_set

			modified = True

	if (x_coor + 1) < width and (y_coor + 2) < height:
		val = board[x_coor + 1][y_coor + 2]
		if tools.coor_to_string(x_coor + 1, y_coor + 2) not in board_with_moves_set[x_coor][y_coor]:
			board[x_coor + 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]

			curr_set = board_with_moves_set[x_coor][y_coor].copy()
			curr_set.add(tools.coor_to_string(x_coor + 1, y_coor + 2))
			board_with_moves_set[x_coor + 1][y_coor + 2] = curr_set

			modified = True

	return modified

if __name__ == "__main__":
    main()
