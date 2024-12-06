from collections import defaultdict

from ..utils.common import load_input, timer

# We can handle the input as a matrix
MATRIX = tuple(load_input(4, 1))


@timer
def problem1_solution():
    # Parse matrix's rows and columns
    rows = defaultdict(str)
    cols = defaultdict(str)
    # Indexes' difference is constant in all diagonals parallel to the main-diagonal
    diag_diff = defaultdict(str)
    # Indexes' sum is constant in all diagonals parallel to the anti-diagonal
    diag_sum = defaultdict(str)
    for i, row in enumerate(MATRIX, start=1):
        # Each input line is a row
        rows[i] = row
        for j, char in enumerate(row, start=1):
            # Each char of the row belongs to a different column
            cols[j] += char
            # Diagonals parallel to the main-diagonal: the char goes to the end
            diag_diff[i - j] += char
            # Diagonals parallel to the anti-diagonal: the char goes at the start
            diag_sum[i + j] = char + diag_sum[i + j]
    return sum(
        s.count("XMAS") + s.count("SAMX")
        for s in (
            list(rows.values())
            + list(cols.values())
            + list(diag_diff.values())
            + list(diag_sum.values())
        )
    )


@timer
def problem2_solution():
    count = 0
    # Use ``range(1, len(o) - 1)`` since we need to check first the "A"s: if they
    # appear at matrix's border, we can safely ignore them cause there's no way we can
    # retrieve a cross-MAS with them
    for i in range(1, len(MATRIX) - 1):
        for j in range(1, len(MATRIX[i]) - 1):
            char = MATRIX[i][j]
            if char == "A":
                diag_1 = "".join([MATRIX[i - 1][j - 1], char, MATRIX[i + 1][j + 1]])
                diag_2 = "".join([MATRIX[i - 1][j + 1], char, MATRIX[i + 1][j - 1]])
                if diag_1 in ("MAS", "SAM") and diag_2 in ("MAS", "SAM"):
                    count += 1
    return count


def main():
    print(f"** Solution to problem 1: {problem1_solution()} **")
    print(f"** Solution to problem 2: {problem2_solution()} **")


if __name__ == "__main__":
    main()
