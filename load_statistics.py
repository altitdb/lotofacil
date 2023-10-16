import numpy as np


if __name__ == '__main__':

    list_numbers = []
    with open('results.md', 'r') as reader:
        for line in reader.readlines():
            if line != '':
                numbers = line.replace("\n", "").split(',')
                for n in range(0, 15):
                    list_numbers.append(numbers[n])

    x = np.array(list_numbers)
    unique, counts = np.unique(x, return_counts=True)

    # print(np.asarray((counts, unique)).T)

    statistics = []
    for u, c in zip(unique, counts):
        statistics.append({
            'number': u,
            'count': c
        })

    statistics = sorted(statistics, key=lambda x: x['count'], reverse=False)

    print(statistics)