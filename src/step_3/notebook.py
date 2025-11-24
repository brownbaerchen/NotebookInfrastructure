# %% [markdown]
# Welcome to this notebook!
# In this step, this notebook will guide you how to use the add function from step_1
# First, we need to define / import the add function.

# %%
import os
import sys

cwd = os.getcwd()
root = os.path.abspath(os.path.join(cwd, "..", ".."))
if root not in sys.path:
    sys.path.append(root)

# %%
from src.step_1.dummy_add import add

# %% [markdown]
# To use the add function, simply call it via add(a,b) where a and b are of the type int, float or complex.

# %%
add(2, 3)

# %% [markdown]
# The output of the cell above should be 5

# %% [markdown]
# Using this type of notebook, you can easily create plots as well

# %%
import matplotlib.pyplot as plt

list = [add(i, i) for i in range(10)]
plt.plot(list)
plt.show()


# %% [markdown]
# This is just a docs on how to create simple notebooks using Jupytext. The notebook won't be automatically run and the output won't be saved.
# jupytext --to ipynb path/to/notebook.py
# jupyter notebook path/to/notebook.ipynb
