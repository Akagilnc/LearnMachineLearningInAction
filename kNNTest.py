import kNN


group, labels = kNN.create_data_set()
print kNN.classify0([0, 0], group, labels, 3)