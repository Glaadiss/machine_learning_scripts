import numpy as np

# define variable a with numbers in the range from 0 to 7 (not inclusive)
a = np.arange(start=0, stop=7)

# define variable b with numbers in the range from 2 to 17 in steps of 4
b = np.arange(start=2, stop=17, step=4)

# similar to b but without explicit decleration of the input arguments names
c = np.arange(100, 95, -1)

x = np.concatenate([np.zeros(2), np.arange(0, 3.6, 0.6), np.ones(3)])
# take out elements 2 through 5 (notice 6 is not included)
x[1:5]

# take the last element of x
x[-1]

# return every other element of x starting from the 2nd
x[1::2]

# PI in y in positions 1, 3, ... 9
y = x
y[1::2] = np.pi

# multiply array
x = np.arange(1, 6)  # array([1, 2, 3, 4, 5])
y = np.arange(2, 12, 2)  # array([ 2,  4,  6,  8, 10])
x * y  # array([ 2,  8, 18, 32, 50])

X = ["dsaaaew", "dsaaasa", "dsaaads"]
X = np.array([list(var) for var in X])
# using all 4 letters,
X = X[:, 0:4]


# for using e.g. only third letter or first and last try X[:,[2]] and X[:, [0,3]]

def get_matrix(string_data):
    rows = string_data.replace('−', '-').split("\n")
    data = [xx.split(" ") for xx in rows]
    return np.matrix(data, dtype=float)
