import pickle

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

fname = "pickled_list.pk"

# write list to file
# open it in write/binary mode
with open(fname, "wb") as f:
    pickle.dump(x, f)

# read the list from the file
# open it in read/binary mode
with open(fname, "rb") as f:
    y = pickle.load(f)

print(y)