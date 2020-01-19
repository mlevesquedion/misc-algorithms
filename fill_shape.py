from itertools import groupby


def print_grid(grid):
    print("\n".join(map(str, grid)))


def fill_shape(points):
    # assumes shape is closed, fills by row
    fill_points = []
    for (row, group) in groupby(sorted(points), key=lambda x: x[0]):
        group = list(group)
        for ((_, col), (_, nextcol)) in zip(group, group[1:]):
            for missing_col in range(col + 1, nextcol):
                fill_points.append((row, missing_col))
    return points + fill_points


if __name__ == "__main__":
    grid = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 1, 1],
    ]
    print("before filling: ")
    print_grid(grid)

    shape = [
        (rowi, coli)
        for rowi, row in enumerate(grid)
        for coli, value in enumerate(row)
        if value
    ]
    filled = fill_shape(shape)

    for (rowi, coli) in filled:
        grid[rowi][coli] = 1

    print("after filling: ")
    print_grid(grid)
