from math import log
from numpy import mean


# calculate Cross Entropy
def cross_ent(a, b):
    return -sum([a[i] * log(b[i]) for i in range(len(a))])


# classification data
a = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # Actual Class Labels
b = [0.8, 0.9, 0.9, 0.6, 0.8, 0.1, 0.4, 0.2, 0.1, 0.3]  # Predicted Class Labels
# The closer a[i] and b[i] are to eachother, the better the nats score will be

# find cross entropy for each example
results = list()
for i in range(len(a)):
    # distribution of event {0, 1}
    exp = [1.0 - a[i], a[i]]  # expected
    pred = [1.0 - b[i], b[i]]  # predicted
    # find cross entropy for event
    ce = cross_ent(exp, pred)
    print('>[y=%.1f, yhat=%.1f] ce: %.3f nats' % (a[i], b[i], ce))
    results.append(ce)

# calculate avg cross entropy
mean_ce = mean(results)
print('Average Cross Entropy is: %.4f nats' % mean_ce)

# A cross entropy score between 0.2 and 0.3 is between 'Fine' and 'Not Great'
# The closer to 0 the better
# The closer to 1 the worse
# Something greater than 2 means something is probably broken
