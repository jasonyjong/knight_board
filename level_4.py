#!/usr/bin/env python

import tools

def main():
	special_board = import_special_board()

	width = len(special_board)
	height = len(special_board[0])
	tools.print_board(special_board)

	# get list of teleport spots
	teleport_list = []
	for y in range(len(special_board[0])):
		for x in range(len(special_board)):
			if special_board[x][y] == 'T':
				teleport_list.append(tools.coor_to_string(x, y))

	# get input for data.  We don't want to start on an element for simplicity.
	print "What is the start location?"
	valid_start_coor = False
	while not valid_start_coor:
		start_x_coor, start_y_coor = tools.get_input_coordinates(width, height)
		element = special_board[start_x_coor][start_y_coor]
		if element == 'W' or element == 'R' or element == 'B' or element == 'T' or element == 'L':
			print "Start has element.  Enter new start location:"
			valid_start_coor =  False
		else:
			valid_start_coor =  True

	print "What is the end location?"
	unique_end_coor = False
	while not unique_end_coor:
		end_x_coor, end_y_coor = tools.get_input_coordinates(width, height)
		element = special_board[end_x_coor][end_y_coor]
		if (start_x_coor == end_x_coor) and (start_y_coor == end_y_coor):
			print "Same as start.  Enter new end location:"
			unique_end_coor =  False
		elif element == 'W' or element == 'R' or element == 'B' or element == 'T' or element == 'L':
			print "End has element.  Enter new end location:"
			unique_end_coor =  False
		else:
			unique_end_coor =  True

	# mark start/end location
	board = [['.' for x in range(height)] for x in range(width)]
	board[start_x_coor][start_y_coor] = 'S'
	board[end_x_coor][end_y_coor] = 'E'

	# initialize board storing moves
	board_with_moves = [['.' for x in range(height)] for x in range(width)]
	board_with_moves[start_x_coor][start_y_coor] = []

	# store number of moves.  Important because of our elements
	board_with_num_moves = [['.' for x in range(height)] for x in range(width)]
	board_with_num_moves[start_x_coor][start_y_coor] = 0

	continue_loop = True
	current_step = 0
	teleport_done = False
	while continue_loop:
		continue_loop = False

		for y in range(len(board[0])):
			for x in range(len(board)):
				if board_with_moves[x][y] != '.' and board_with_num_moves[x][y] == current_step:
					modified = draw_knight_move(board_with_moves, board_with_num_moves, special_board, x, y, current_step + 1, width, height)
					if modified:
						continue_loop = True

		# shortest move found!
		if board_with_moves[end_x_coor][end_y_coor] != '.':
			move_to_end = board_with_moves[end_x_coor][end_y_coor]

			special_board_to_print = [row[:] for row in special_board]
			for num_move in range(1, len(move_to_end)):
				x, y = tools.string_to_coor(move_to_end[num_move])
				special_board_to_print[start_x_coor][start_y_coor] = 'S'
				special_board_to_print[end_x_coor][end_y_coor] = 'E'
				special_board_to_print[x][y] = board_with_num_moves[x][y]

			tools.print_board(special_board_to_print)

			print 'Sequence of moves: '
			for num_move in range(0, len(move_to_end)):
				x, y = tools.string_to_coor(move_to_end[num_move])
				print '(' , x, ', ', y, ')'
			print '(' , end_x_coor, ', ', end_y_coor, ')'

			# we want to check if sequence of moves are all valid
			valid_knight_moves = True
			for idx in range(1, len(move_to_end)):
				prev_x, prev_y = tools.string_to_coor(move_to_end[idx - 1])
				x, y = tools.string_to_coor(move_to_end[idx])

				if not tools.is_valid_knight_move(prev_x, prev_y, x, y) and move_to_end[idx] not in teleport_list:
					print 'Invalid'
					valid_knight_moves = False
					break

			if valid_knight_moves:
				print '--- All valid knight moves'
			else:
				print '--- Invalid knight moves'

			exit()

		current_step += 1

		# check if anything has landed on teleport locations.
		# because we care about shortest moves, if we land on one, then move all other moves to teleport.
		if not teleport_done:
			for teleport_str in teleport_list:
				t_x, t_y = tools.string_to_coor(teleport_str)
				if board_with_moves[t_x][t_y] != '.':
					for teleport_str in teleport_list:
						t_x_, t_y_ = tools.string_to_coor(teleport_str)
						if board_with_moves[t_x_][t_y_] == '.':
							board_with_moves[t_x_][t_y_] = board_with_moves[t_x][t_y][:]
							board_with_num_moves[t_x_][t_y_] = board_with_num_moves[t_x][t_y]
					break

def import_special_board():
	f = open('special_board.txt', 'r')

	special_board = []
	for line in f:
		special_board.append([c for c in line.strip()])

	return [list(a) for a in zip(*special_board)]

def draw_knight_move(board, board_with_num_moves, special_board, x_coor, y_coor, step, width, height):
	modified = False
	if (x_coor - 2) >= 0 and (y_coor - 1) >= 0:
		val = board[x_coor - 2][y_coor - 1]
		element = special_board[x_coor - 2][y_coor - 1]
		# if never landed on spot or block element
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor - 1] != 'B' and special_board[x_coor - 1][y_coor - 1] != 'B') or \
				(special_board[x_coor - 1][y_coor] != 'B' and special_board[x_coor - 2][y_coor] != 'B'):

				board[x_coor - 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor - 2][y_coor - 1] = step

				if element == 'W':
					board_with_num_moves[x_coor - 2][y_coor - 1] += 1
				elif element == 'L':
					board_with_num_moves[x_coor - 2][y_coor - 1] += 4

				modified = True

	if (x_coor - 2) >= 0 and (y_coor + 1) < height:
		val = board[x_coor - 2][y_coor + 1]
		element = special_board[x_coor - 2][y_coor + 1]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor + 1] != 'B' and special_board[x_coor - 1][y_coor + 1] != 'B') or \
				(special_board[x_coor - 1][y_coor] != 'B' and special_board[x_coor - 2][y_coor] != 'B'):

				board[x_coor - 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor - 2][y_coor + 1] = step

				if element == 'W':
					board_with_num_moves[x_coor - 2][y_coor + 1] += 1
				elif element == 'L':
					board_with_num_moves[x_coor - 2][y_coor + 1] += 4

				modified = True

	if (x_coor + 2) < width and (y_coor - 1) >= 0:
		val = board[x_coor + 2][y_coor - 1]
		element = special_board[x_coor + 2][y_coor - 1]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor - 1] != 'B' and special_board[x_coor - 1][y_coor - 1] != 'B') or \
				(special_board[x_coor + 1][y_coor] != 'B' and special_board[x_coor + 2][y_coor] != 'B'):

				board[x_coor + 2][y_coor - 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor + 2][y_coor - 1] = step

				if element == 'W':
					board_with_num_moves[x_coor + 2][y_coor - 1] += 1
				elif element == 'L':
					board_with_num_moves[x_coor + 2][y_coor - 1] += 4

				modified = True

	if (x_coor + 2) < width and (y_coor + 1) < height:
		val = board[x_coor + 2][y_coor + 1]
		element = special_board[x_coor + 2][y_coor + 1]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor + 1] != 'B' and special_board[x_coor + 1][y_coor + 1] != 'B') or \
				(special_board[x_coor + 1][y_coor] != 'B' and special_board[x_coor + 2][y_coor] != 'B'):

				board[x_coor + 2][y_coor + 1] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor + 2][y_coor + 1] = step

				if element == 'W':
					board_with_num_moves[x_coor + 2][y_coor + 1] += 1
				elif element == 'L':
					board_with_num_moves[x_coor + 2][y_coor + 1] += 4

				modified = True

	if (x_coor - 1) >= 0 and (y_coor - 2) >= 0:
		val = board[x_coor - 1][y_coor - 2]
		element = special_board[x_coor - 1][y_coor - 2]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor - 1] != 'B' and special_board[x_coor][y_coor - 2] != 'B') or \
				(special_board[x_coor - 1][y_coor] != 'B' and special_board[x_coor - 1][y_coor - 1] != 'B'):

				board[x_coor - 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor - 1][y_coor - 2] = step

				if element == 'W':
					board_with_num_moves[x_coor - 1][y_coor - 2] += 1
				elif element == 'L':
					board_with_num_moves[x_coor - 1][y_coor - 2] += 4

				modified = True

	if (x_coor - 1) >= 0 and (y_coor + 2) < height:
		val = board[x_coor - 1][y_coor + 2]
		element = special_board[x_coor - 1][y_coor + 2]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor + 1] != 'B' and special_board[x_coor][y_coor + 2] != 'B') or \
				(special_board[x_coor - 1][y_coor] != 'B' and special_board[x_coor - 1][y_coor + 1] != 'B'):

				board[x_coor - 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor - 1][y_coor + 2] = step

				if element == 'W':
					board_with_num_moves[x_coor - 1][y_coor + 2] += 1
				elif element == 'L':
					board_with_num_moves[x_coor - 1][y_coor + 2] += 4

				modified = True

	if (x_coor + 1) < width and (y_coor - 2) >= 0:
		val = board[x_coor + 1][y_coor - 2]
		element = special_board[x_coor + 1][y_coor - 2]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor - 1] != 'B' and special_board[x_coor][y_coor - 2] != 'B') or \
				(special_board[x_coor + 1][y_coor] != 'B' and special_board[x_coor + 1][y_coor - 1] != 'B'):

				board[x_coor + 1][y_coor - 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor + 1][y_coor - 2] = step

				if element == 'W':
					board_with_num_moves[x_coor + 1][y_coor - 2] += 1
				elif element == 'L':
					board_with_num_moves[x_coor + 1][y_coor - 2] += 4

				modified = True

	if (x_coor + 1) < width and (y_coor + 2) < height:
		val = board[x_coor + 1][y_coor + 2]
		element = special_board[x_coor + 1][y_coor + 2]
		if val == '.' and element != 'R' and element != 'B':
			if (special_board[x_coor][y_coor + 1] != 'B' and special_board[x_coor][y_coor + 2] != 'B') or \
				(special_board[x_coor + 1][y_coor] != 'B' and special_board[x_coor + 1][y_coor + 1] != 'B'):

				board[x_coor + 1][y_coor + 2] = board[x_coor][y_coor][:] + [tools.coor_to_string(x_coor, y_coor)]
				board_with_num_moves[x_coor + 1][y_coor + 2] = step

				if element == 'W':
					board_with_num_moves[x_coor + 1][y_coor + 2] += 1
				elif element == 'L':
					board_with_num_moves[x_coor + 1][y_coor + 2] += 4

				modified = True

	return modified

if __name__ == "__main__":
    main()
