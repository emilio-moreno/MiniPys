s = "xyzsz"
s = " "

def can_ride(passengers, n):
	x_position = 0
	total_num_passengers = 0
	while passengers:
		print(x_position)
		print(total_num_passengers)
		print(passengers)
		print("\n")
		if total_num_passengers > n:
			return False

		# Drop-off
		passengers_copy = passengers[:]
		for passenger in passengers:
			if passenger[2] == x_position:
				total_num_passengers -= passenger[0]
				passengers_copy.remove(passenger)

		passengers = passengers_copy

		for passenger in passengers:
			if passenger[1] == x_position:
				total_num_passengers += passenger[0]

		x_position += 1
	return True

passengers = [[10, 1, 5], [2, 2, 5], [1, 1, 3]]
n = 5

print(can_ride(passengers, n))