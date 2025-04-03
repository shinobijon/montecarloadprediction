import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
simulations = 10000

# Input assumptions (these can be adjusted to reflect realistic values)
budget = 1000  # total ad spend in USD
cpc_mean = 0.05  # average cost per click
cpc_std = 0.15  # standard deviation of CPC
ctr_mean = 0.015  # average CTR (1.5%)
ctr_std = 0.005  # standard deviation of CTR
conversion_rate_mean = 0.10  # average conversion rate (10%)
conversion_rate_std = 0.02  # standard deviation of conversion rate

# Simulate CPC, CTR, and Conversion Rate
cpc_samples = np.random.normal(cpc_mean, cpc_std, simulations)
ctr_samples = np.random.normal(ctr_mean, ctr_std, simulations)
conversion_rate_samples = np.random.normal(conversion_rate_mean, conversion_rate_std, simulations)

# Simulate results
impressions = budget / cpc_samples / ctr_samples  # Estimate total impressions
clicks = impressions * ctr_samples
conversions = clicks * conversion_rate_samples

# Plot histogram of conversions
plt.hist(conversions, bins=50, edgecolor='black')
plt.title('Monte Carlo Simulation of Facebook Ad Conversions')
plt.xlabel('Estimated Conversions')
plt.ylabel('Impressions')
plt.grid(True)
plt.show()
