#!/usr/bin/env python

def coor_to_string(x, y):
	return str(x) + ',' + str(y)

def string_to_coor(val):
	 x, y = val.split(',')
	 return int(x), int(y)

# prints board.
def print_board(board):
	for y in range(len(board[0])):
		row_string = ''
		for x in range(len(board)):
			row_string += str(board[x][y]) + ' '
		print row_string

# checks if knight move is valid
def is_valid_knight_move(current_x_coor, current_y_coor, next_x_coor, next_y_coor):
	if ((current_x_coor - 2) == next_x_coor or (current_x_coor + 2) == next_x_coor) and ((current_y_coor - 1 == next_y_coor) or (current_y_coor + 1 == next_y_coor)):
		return True
	elif ((current_y_coor - 2) == next_y_coor or (current_y_coor + 2) == next_y_coor) and ((current_x_coor - 1 == next_x_coor) or (current_x_coor + 1 == next_x_coor)):
		return True
	else:
		return False

# generically get input coordinates within bounds
def get_input_coordinates(width, height):
	has_x_coor = False
	while not has_x_coor:
		try:
			x_coor = int(raw_input('Enter x coordinate: '))
			if x_coor >= width or x_coor < 0:
				print "   Not within bounds"
				has_x_coor = False
			else:
				has_x_coor = True
		except ValueError:
			print "   Not valid integer"
			has_x_coor = False

	has_y_coor = False
	while not has_y_coor:
		try:
			y_coor = int(raw_input('Enter y coordinate: '))
			if y_coor >= height or y_coor < 0:
				print "   Not within bounds"
				has_y_coor = False
			else:
				has_y_coor = True
		except ValueError:
			print "   Not valid integer"
			has_y_coor = False

	return x_coor, y_coor
