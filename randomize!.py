import json
import random

#%% Function definitions
def practice(n=1, show=True):
	ex_keys = list(data['exercises'].keys())
	chosen_exercises = random.sample(ex_keys, n)
	if show:
		for i, ex in enumerate(chosen_exercises):
			print(f"{i}. {ex}")

		print("\n")
	return chosen_exercises


def practiced(chosen_exercises):
	for ex in chosen_exercises:
		data['exercises'][ex]['times_practiced'] += 1

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

p = practice(2)
save(p)