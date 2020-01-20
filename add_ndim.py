def add(Z1, Z2):
    return [z1 + z2 for z1, z2 in zip(Z1, Z2)]


def add_ndim(Z1, Z2):
    # assumes Z1 and Z2 have same, regular dimensions
    if isinstance(Z1[0], list):
        return [add_ndim(z1, z2) for z1, z2 in zip(Z1, Z2)]
    return add(Z1, Z2)


Z1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
Z2 = [[[1, 0], [0, 1]], [[0, 1], [1, 0]]]

if __name__ == "__main__":
    print(add_ndim(Z1, Z2))
