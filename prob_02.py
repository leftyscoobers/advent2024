input_file = 'input_02.txt'
raw_data = [l.strip().split() for l in open(input_file, 'r').readlines()]

reports = [[int(x) for x in l] for l in raw_data]

def is_safe(report):
	l1 = report[:-1]
	l2 = report[1:]
	diffs = [b - a for a, b in zip(l1, l2)]
	safe = False
	if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
		safe = True
		grade_3_or_less = [abs(d) < 4 for d in diffs]
		if not all(grade_3_or_less):
			safe = False
	return safe

safe = [is_safe(r) for r in reports]
print(f'Part 1: n safe reports is {sum(safe)}')

# Now we can remove up to one value in a list to "make it safe". 
# A dumb way to do this would be, for unsafe reports, check what happens if we remove each value until it works or we're out of values.

def is_safe_with_dampener(report):
	report_safe = is_safe(report)
	
	if report_safe:
		return True
	else:
		for i, r in enumerate(report):
			print(f'i = {i}, r = {r}')
			damp_report = report[:i] + report[i+1:]
			if is_safe(damp_report):
				return True
		return False

safe_w_dampener = [is_safe_with_dampener(r) for r in reports]
print(f'Part 2: n safe after applying dampener is {sum(safe_w_dampener)}')


