import json
import random
from datetime import datetime	

#%% Function definitions
def practice(n=1, *args, show=True):
	i = 0
	ex_keys = []
	for ex in data['exercises']:
		if set(data['exercises'][ex]['tags']) >= set(args):
			ex_keys.append(ex)

	chosen_exercises = random.sample(ex_keys, n)
	if show:
		for i, ex in enumerate(chosen_exercises):
			print(f"{i}. {ex}")

		print("\n")
	return chosen_exercises


def practiced(chosen_exercises):
	frmt = "%d/%m/%y"
	str_today = datetime.today().strftime(frmt)
	for ex in chosen_exercises:
		data['exercises'][ex]['times_practiced'] += 1
		data['exercises'][ex]['practiced'] = str_today

def save(chosen_exercises, show=True):
	practiced(chosen_exercises)

	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

	print("Progress saved!\n")
	if show:
		print(json.dumps(data, indent=4))
	print("\n")


#%% Calls
filename = "Exercises/絵.json"
with open(filename) as f:
	data = json.load(f)

p = practice(3)
#save(p)