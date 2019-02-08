import math as m
import numpy as np
import matplotlib.pyplot as plt

def dbinom( observed, size, prob):
    return ( m.factorial(size) / (m.factorial(observed)*m.factorial(size-observed))) * prob**observed * (1-prob)**(size-observed)


x = dbinom(6, size=9, prob=0.67)
print(x)

# check against
# https://github.com/cavaunpeu/statistical-rethinking


# 2E1 - Which of the expressions belowc orrespond to the statement:the probability of rain on Monday?
# (2) Pr(rain|Monday)

# 2E2 - Which of the following statements corresponds to the expression: Pr(Monday|rain)?
# (3) The probability that it is Monday, given that it is raining.

# 2E3. Which of the expressions below correspond to the statement: the probability that it is Monday, given that it is raining?
# (1) Pr(Monday|rain)

def plotGribApprox(w, n, nb_points):
    p_grid = np.linspace(0, 1, nb_points)
    prior = np.full( (1, nb_points), 1)
    print(prior)
    likelihood = dbinom( w , size=n , prob=p_grid )
    unstd_posterior = likelihood * prior
    # standardize the posterior, so it sums to 1
    posterior = unstd_posterior / np.sum(unstd_posterior)
    print(posterior)
    plt.xlabel('probability of water')
    plt.ylabel('posterior probability')
    plt.plot( p_grid , posterior[0])
    plt.show()

#plotGribApprox(6, 9, 5)

# 2M1
#plotGribApprox(3, 3, 50)
#plotGribApprox(3, 4, 50)
#plotGribApprox(5, 7, 50)

# 2M2
def plotGribApprox2(w, n, nb_points):
    p_grid = np.linspace(0, 1, nb_points)
    prior = 
    print(prior)
    likelihood = dbinom( w , size=n , prob=p_grid )
    unstd_posterior = likelihood * prior
    # standardize the posterior, so it sums to 1
    posterior = unstd_posterior / np.sum(unstd_posterior)
    print(posterior)
    plt.xlabel('probability of water')
    plt.ylabel('posterior probability')
    plt.plot( p_grid , posterior[0])
    plt.show()


