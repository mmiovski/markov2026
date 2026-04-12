from scipy.stats import poisson

# initialize total sum
ttl = 0.0

# range to k = 30 since poisson probs after 30 are essentially 0
for k in range(30):

    # compute sum and add to total for each k = 1,2,...,30 (0,1,...,29)
    ttl += poisson.pmf(k, 1.5) * (1 - poisson.cdf(k, 2))

# print total
print(round(ttl, 5))