# Manual calculation of basic statistics

sample_gpas = [
    3.5, 3.6, 3.2, 3.8, 3.4,
    3.9, 3.1, 3.5, 3.7, 3.6,
    3.3, 3.5, 3.8, 3.7, 3.4,
    3.2, 4.0, 3.6, 3.5, 3.1
]


def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def mode(data):
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes


def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def standard_deviation(data):
    return variance(data) ** 0.5


if __name__ == "__main__":
    print("Mean:", mean(sample_gpas))
    print("Median:", median(sample_gpas))
    print("Mode:", mode(sample_gpas))
    print("Min:", min(sample_gpas))
    print("Max:", max(sample_gpas))
    print("Standard Deviation:", standard_deviation(sample_gpas))
    print("Variance:", variance(sample_gpas))
