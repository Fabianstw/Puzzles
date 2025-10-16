from aocd import get_data

lines = []


data = get_data(day=2, year=2024).split("\n")
for line in data:
	split = line.rstrip().split(" ")
	newLine = []
	for spli in split:
		newLine.append(int(spli))
	
	lines.append(newLine)

def is_safe(report):
	if len(report) < 2:
		return True  # Trivial case: 0 or 1 levels are always safe
	
	# Determine the trend (increasing or decreasing)
	increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
	decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
	
	return increasing or decreasing


def is_fixable(report):
	for i in range(len(report)):
		# Create a new report with one level removed
		modified_report = report[:i] + report[i + 1:]
		if is_safe(modified_report):
			return True  # Found a fixable configuration
	return False


def count_safe_reports_with_dampener(reports):
	safe_count = 0
	for report in reports:
		if is_safe(report) or is_fixable(report):
			safe_count += 1
	return safe_count


# Analyze example reports
example_safe_count = count_safe_reports_with_dampener(lines)
print(example_safe_count)