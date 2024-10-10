#!/usr/bin/python3
"""Solves the lock boxes puzzle
The lock boxes puzzle involves determining if all boxes can be opened. 
Each box contains keys that may unlock other boxes.
"""


def look_next_opened_box(opened_boxes):
	"""Searches for the next box that has been opened but not yet checked.
	This function iterates over opened boxes to find the next one that 
	hasn't been processed (i.e., "opened" but not "opened/checked"). 
	It returns the list of keys from that box and marks the box as checked.
	Args:
		opened_boxes (dict): A dictionary that tracks which boxes have been opened 
							and their corresponding keys.

	Returns:
		list: A list of keys found in the next opened box that hasn't been checked.
			  Returns None if no such box exists.
	"""
	for index, box in opened_boxes.items():
		if box.get('status') == 'opened':
			# Mark the box as 'opened/checked' after processing its keys
			box['status'] = 'opened/checked'
			return box.get('keys')
	return None  # No more opened boxes to check


def canUnlockAll(boxes):
	"""Determines if all boxes can be unlocked starting from the first box.
	This function checks if all boxes in the list can be unlocked using the keys 
	found within them. The first box is always unlocked, and subsequent boxes 
	can only be unlocked if the keys to those boxes are found.
	Args:
		boxes (list): A list of lists where each inner list contains keys to unlock other boxes.
					  The index of the outer list represents the box number, and the keys 
					  inside it represent the keys for other boxes.

	Returns:
		bool: True if all boxes can be unlocked; otherwise, False.
	"""
	if len(boxes) <= 1 or boxes == [[]]:
		# If there is only one box or it's an empty set of boxes, return True
		return True

	aux = {}  # Auxiliary dictionary to track opened boxes and their keys
	while True:
		if len(aux) == 0:
			# Always start by opening the first box (index 0)
			aux[0] = {
				'status': 'opened',  # The box is opened but not yet checked
				'keys': boxes[0],    # Store the keys from the first box
			}

		# Fetch keys from the next box that has been opened but not yet checked
		keys = look_next_opened_box(aux)
		if keys:
			for key in keys:
				try:
					# Skip boxes that have already been opened and checked
					if aux.get(key) and aux.get(key).get('status') == 'opened/checked':
						continue
					# Open the box corresponding to the key if it hasn't been opened
					aux[key] = {
						'status': 'opened',
						'keys': boxes[key]
					}
				except (KeyError, IndexError):
					# Ignore invalid keys (i.e., keys that don't correspond to any box)
					continue
		# Continue until there are no more 'opened' boxes to process
		elif 'opened' in [box.get('status') for box in aux.values()]:
			continue
		# If all boxes are opened, break the loop
		elif len(aux) == len(boxes):
			break
		else:
			# If some boxes remain unopened and no more keys are available, return False
			return False

	# Return True if the number of opened boxes matches the total number of boxes
	return len(aux) == len(boxes)


def main():
	"""Entry point of the program for testing the canUnlockAll function."""
	canUnlockAll([[]])


if __name__ == '__main__':
	# Start the program by calling the main function
	main()
