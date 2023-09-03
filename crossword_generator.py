import random

# Function to generate a crossword grid
def generate_crossword(rows, cols):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    return grid

# Function to fill the crossword grid with user-defined words
def fill_crossword(grid, words):
    for word in words:
        direction = random.choice(['across', 'down'])
        row, col = random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)

        if direction == 'across':
            while col + len(word) > len(grid[0]):
                row, col = random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)

            for i in range(len(word)):
                grid[row][col + i] = word[i]

        elif direction == 'down':
            while row + len(word) > len(grid):
                row, col = random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)

            for i in range(len(word)):
                grid[row + i][col] = word[i]

# Function to display the crossword grid
def display_crossword(grid):
    for row in grid:
        print(' '.join(row))

# Main function
if __name__ == '__main__':
    rows, cols = 10, 10  # Adjust the size of the crossword grid

    user_words = []  # User-defined words
    num_words = int(input("Enter the number of words: "))

    for _ in range(num_words):
        word = input("Enter a word: ").strip()
        user_words.append(word)

    crossword_grid = generate_crossword(rows, cols)
    fill_crossword(crossword_grid, user_words)
    display_crossword(crossword_grid)
