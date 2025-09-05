"""

HIT137 - Assignment 2 - Task 3
Recursive geometric pattern using Python's turtle graphics.

What it does
- Prompts user for::
    - number of sides, greater than or equal to 3 (>=3)
    - side length in pixels, has to be more than zero (>0)
    - recursion depth, zero or higher (no minus numbers)(>=0)
- Draws a regular polygon where each edge is replaced by an inward "dent" Koch-like recursive pattern.

"""

import turtle # Graphics libary

# safety caps - ...i broke it, so now you cant 

MAX_DEPTH = 8          # stops user going too crazy
MIN_SEG_LEN = 2.0      # dont bother drawing if too small


def draw_inward_koch_edge(t, length, depth):
    
        if depth <= 0 or length <= MIN_SEG_LEN:
            t.forward(length)
            return

        one_third = length / 3.0
        draw_inward_koch_edge(t, one_third, depth - 1)
        # FIX: inward dent requires L60, R120, L60 (for CCW polygon)
        t.left(60)
        draw_inward_koch_edge(t, one_third, depth - 1)
        t.right(120)
        draw_inward_koch_edge(t, one_third, depth - 1)
        t.left(60)
        draw_inward_koch_edge(t, one_third, depth - 1)

"""
Inward Koch like recursion:

- Base case: If recursion depth = 0, just draw a straight line.

- Recursive case: Split the line into three equal parts.

- Draw the first third straight.

- Turn left 60° and draw the second third (this starts the “dent”).

- Turn right 120° and draw the third third (completes the inward triangle).

- Turn left 60° again and draw the final third.

- Effect: Each straight line becomes 4 smaller lines with a triangular dent pointing inward.

"""


def draw_polygon_with_inward_fractal(n_sides, side_len, depth):

    try:
        screen = turtle.Screen()
        screen.title("HIT137 - Task 3 (Inward Koch Polygon)")
        screen.tracer(False) # speeds up drawing

        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)  # fastest
        angle = 360.0 / n_sides

        for _ in range(n_sides):
            draw_inward_koch_edge(t, side_len, depth)
            t.left(angle)   # CCW trace (interior on the left)
            screen.update()

        screen.update()
        screen.exitonclick()  # click to close
    except turtle.Terminator:
        print("Window closed early. Exiting cleanly.")
    except Exception as e:
        print(f"Error in draw_polygon_with_inward_fractal: {e}")

"""
What its doing:

- Creates a turtle pen.

- Hides the turtle icon and sets speed to fastest.

- Loops over the polygon’s sides:

- For each side → calls draw_inward_koch_edge with recursion depth.

- Turns left by the polygon angle (360 / n_sides) to draw the next side.

- Example: If sides = 4, you get a sqaure with each edge replaced by the inward Koch pattern.

"""


def main():
    try:
        n_sides = int(input("Enter the number of sides (>=3): "))
        side_len = float(input("Enter the side length (pixels): "))
        depth = int(input("Enter the recursion depth (>=0): "))

        if n_sides < 3 or side_len <= 0 or depth < 0:
            print("Invalid inputs: sides must be >=3, side length >0, depth >=0.")
            return

        if depth > MAX_DEPTH:
            print(f"Depth {depth} is too high. Capping to MAX_DEPTH = {MAX_DEPTH}.")
            depth = MAX_DEPTH

        draw_polygon_with_inward_fractal(n_sides, side_len, depth)
    except Exception as e:
        print(f"Error in main: {e}")
"""
What is happening:

- Asks the user for polygon sides, side length, and recursion depth.

- Validates inputs to ensure they meet criteria.

- Caps recursion depth if user enters something too high.

- Passes those values into draw_polygon_with_inward_fractal to start drawing.

"""

if __name__ == "__main__":
    main()

"""only run main if this file is executed directly, not if imported as a module."""
