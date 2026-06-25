import math

# --- YOUR CUP PARAMETERS ---
# We scale the 50mm and 4mm up by 10x so it fits nicely in the simulator's viewbox
r_top = 400.0  
r_bottom = 0.0
rows = 10       # Number of horizontal rings
cols = 20      # Number of vertical zig-zags
angle_spread = math.pi * 1.2  # Creates a curved arc that wraps into a cone
zig_zag_intensity = 15.0      # How sharp the angles are

def generate_svg():
    svg = []
    svg.append('<svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">')
    
    # 1. Calculate perfect vertices (no floating point tears!)
    vertices = {}
    for j in range(rows + 1):
        # Grade the radius from bottom to top
        base_r = r_bottom + (r_top - r_bottom) * (j / rows)
        for i in range(cols + 1):
            # The Miura alternating zig-zag offset
            offset = zig_zag_intensity if (i + j) % 2 == 0 else -zig_zag_intensity
            r = base_r + offset
            
            # Map to polar coordinates (curved sheet)
            theta = (math.pi - angle_spread)/2 + (i / cols) * angle_spread
            
            # Center the arc at the bottom of the canvas
            x = 500 + r * math.cos(theta)
            y = 850 - r * math.sin(theta)
            vertices[(i, j)] = (x, y)
            
    # Helper to draw lines
    def draw_line(p1, p2, color):
        return f'<line x1="{p1[0]:.4f}" y1="{p1[1]:.4f}" x2="{p2[0]:.4f}" y2="{p2[1]:.4f}" stroke="{color}" stroke-width="1.5"/>'

    red = "#FF0000"   # Mountain
    blue = "#0000FF"  # Valley
    black = "#000000" # Cut/Boundary

    # 2. Draw Horizontal Rings
    for j in range(rows + 1):
        for i in range(cols):
            if j == 0 or j == rows:
                color = black # Top and bottom rims
            else:
                color = red   # Horizontal folds are all mountains
            svg.append(draw_line(vertices[(i, j)], vertices[(i+1, j)], color))

    # 3. Draw Vertical Zig-Zags
    for i in range(cols + 1):
        for j in range(rows):
            if i == 0 or i == cols:
                color = black # Left and right edges
            else:
                # Vertical folds alternate Mountain/Valley column by column
                color = red if i % 2 == 0 else blue
            svg.append(draw_line(vertices[(i, j)], vertices[(i, j+1)], color))

    svg.append('</svg>')
    return "\n".join(svg)

# Print the SVG to the console so you can copy it
with open("s1.svg", "w") as file:
    file.write(generate_svg())