import streamlit as st
import numpy as np

# Function to generate a Minesweeper grid
def generate_grid(rows, cols, num_mines):
    grid = np.zeros((rows, cols), dtype=int)
    mines = np.random.choice(rows * cols, num_mines, replace=False)
    
    for mine in mines:
        r, c = divmod(mine, cols)
        grid[r, c] = -1  # Representing mines with -1
    
    # Calculating numbers around mines
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == -1:
                continue
            
            count = sum(
                grid[r + dr, c + dc] == -1
                for dr in [-1, 0, 1] for dc in [-1, 0, 1]
                if 0 <= r + dr < rows and 0 <= c + dc < cols
            )
            grid[r, c] = count
    
    return grid

def main():
    st.title("Minesweeper Game")
    rows, cols = 8, 8  # Grid size
    num_mines = 10  # Number of mines
    
    if st.button("Generate New Board"):
        grid = generate_grid(rows, cols, num_mines)
        st.session_state.grid = grid  # Store in session state
    
    if "grid" in st.session_state:
        st.write("### Minesweeper Grid")
        st.write(st.session_state.grid)

if __name__ == "__main__":
    main()
