#!/usr/bin/env python

import tools

# global variables for board
width = 8
height = 8

def main():
	print "What is the start location?"
	start_x_coor, start_y_coor = tools.get_input_coordinates(width, height)

	# make sure end location not same as start location
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

	# print initial version
	tools.print_board(board)

	# initialize
	current_x_coor = start_x_coor
	current_y_coor = start_y_coor

	# start getting coordinates, and check validity of them in each move
	while not (current_x_coor == end_x_coor and current_y_coor == end_y_coor):
		next_x_coor, next_y_coor = tools.get_input_coordinates(width, height)
		if tools.is_valid_knight_move(current_x_coor, current_y_coor, next_x_coor, next_y_coor):
			# if over start, replace with 'S'
			if current_x_coor == start_x_coor and current_y_coor == start_y_coor:
				board[current_x_coor][current_y_coor] = 'S'
			else:
				board[current_x_coor][current_y_coor] = '.'

			# mark current location
			board[next_x_coor][next_y_coor] = 'K'
			current_x_coor = next_x_coor
			current_y_coor = next_y_coor

			tools.print_board(board)
		else:
			print 'Not a valid knight move.'

if __name__ == "__main__":
    main()
