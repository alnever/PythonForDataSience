import matplotlib.pyplot as plt
import numpy as np
from data import gdp_cap
from data import life_exp
from data import pop
from data import col


plt.scatter(gdp_cap, life_exp)
# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

plt.show()
plt.clf()

# Bubble Plot

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop *= 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop, c = col, alpha = .8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Display the plot
plt.show()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()

