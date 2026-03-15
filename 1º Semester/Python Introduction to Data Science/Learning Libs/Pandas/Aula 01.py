import pandas as pd
import numpy as np
from IPython.core.display_functions import display
from IPython.display import display, Math

s1 = pd.Series([1, 2, 3, 4, 5, 6, 7])
s2 = pd.Series(["a", "b", "c", "d","e"])
s3 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d","e"])
array = [1, 2, 3, 4, 5]
s4 = pd.Series(array)
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
s5 = pd.Series(dictionary)
s6 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [4, 3, 2, 1]})


# print(s1, s2, s3, s4, s5, s6, sep="\n\n")
display(s6)

