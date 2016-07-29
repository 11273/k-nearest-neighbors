import csv
import math
import operator


def load_data_set(filename):
    with open(filename, newline='') as iris:
        data_reader = csv.reader(iris, delimiter=',')
        return list(data_reader)


def get_classes(training_set):
    return list(set([c[-1] for c in training_set]))


def find_euclidean_distance(sample, training_set, attributes):
    distances = []
    dist = 0
    for data in training_set:
        for x in range(attributes):
            dist += (float(data[x]) - sample[x]) ** 2
        distances.append((data, math.sqrt(dist)))
        dist = 0
    distances.sort(key=operator.itemgetter(1))
    return distances


def find_neighbors(distances, k):
    return distances[0:k]


def find_response(neighbors, classes):
    votes = [0, 0, 0]

    for instance, _ in neighbors:
        for ctr, c in enumerate(classes):
            if instance[-1] == c:
                votes[ctr] += 1
    return max(enumerate(votes), key=operator.itemgetter(1))


def main():
    k = 3
    file = '../iris-dataset.csv'
    attributes = 4

    # load the Iris data set
    training_set = load_data_set(file)

    # generate response classes from data set
    classes = get_classes(training_set)

    # test data
    test_instance = [5.4, 3.2, 1.5, 0.3]

    # calculate distance from each instance in training data
    distances = find_euclidean_distance(test_instance, training_set, attributes)
    # find k nearest neighbors
    neighbors = find_neighbors(distances, k)

    # get the class with maximum votes
    index, value = find_response(neighbors, classes)
    print('The predicted class is : ' + classes[index])
    print('Number of votes : ' + str(value) + ' out of ' + str(k))


if __name__ == '__main__':
    main()
