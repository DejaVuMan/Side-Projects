import numpy as np
from scipy.special import expit
from scipy.linalg import norm
# sklearn utility
from sklearn.base import BaseEstimator, ClassifierMixin

class LogRegression(BaseEstimator, ClassifierMixin):
    # Logistic Regression -- Minimizing by gradient descent.
    # assume unit term has been appended to X

    def __init__(self, maxiter=1000, tol=1e-6):
        # max number of iterations
        self.maxiter = maxiter
        # tolerance
        self.tol = tol

    def predict(self, x):
        return np.rint(self.predict_prob(x).astype(np.int))

    def predict_prob(self, x):
        return expit(x @ self.weights)

    def fit(self, x, y):
        # gradient descent method with learning rate that is optimal
        #  If x is input of a 2d array and y is a 1d array
        # we assume that first column of x is all 1's for bias, and y has label (0/1)
        # the output is then self, aka trained logistic regression model

        # number of examples and features
        m, n = x.shape

        # initialize weights
        self.weights = np.zeros((n, ))

        # find optimal learning rate
        alpha = 2 * m / norm(x)

        # training using gradient descent and optimal stepsize
        for _ in range(self.maxiter):
            # compute gradient
            grad = x.t @ (self.predict_prob(x) - y) / m

            # update weights
            self.weights -= alpha * grad

            # check convergence
            if norm(grad) ** 2 < self.tol:
                break

        return self

