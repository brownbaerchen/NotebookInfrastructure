# %% [markdown]
## Welcome to this notebook! <br>
# In this step, this notebook will guide you how to use the add function from step_1 <br>
# First, we import all of the necessary packages. <br>
# This is also nice to see that $\lambda$ works in markdown cell.

# %%
import matplotlib.pyplot as plt
import os
import sys

cwd = os.getcwd()
root = os.path.abspath(os.path.join(cwd, "..", ".."))
if root not in sys.path:
    sys.path.append(root)

from src.step_1.dummy_add import add  # noqa: E402

# %% [markdown]
# To use the add function, simply call it via add(a,b) where a and b are of the type int, float or complex.

# %%
add(2, 3)

# %% [markdown]
# The output of the cell above should be 5

# %% [markdown]
# Using this type of notebook, you can easily create plots as well.

# %%
list = [add(i, i) for i in range(10)]
plt.plot(list)
plt.show()


# %% [markdown]
# This is just a docs on how to create simple notebooks using Jupytext. <br>
# jupytext --to ipynb --execute path/to/notebook.py <br>
# jupyter notebook path/to/notebook.ipynb <br>
