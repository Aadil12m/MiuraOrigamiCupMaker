# Miura-Ori Cone Pattern Generator

This repository contains a Python script (`miura_ori_maker.py`) that generates a scalable vector graphics (SVG) crease pattern for a curved Miura-ori structure. The pattern maps a traditional flat Miura tessellation onto a polar coordinate system to create an origami shape that naturally folds into a cone or cup.

This script is specifically optimized for export to [Origami Simulator](https://origamisimulator.org/), a physics-based origami folding simulation tool, but the output can also be printed and folded in real life.

---

##  How to Use (Digital Simulation)

To visualize the folding process digitally, you can use the generated SVG file with Origami Simulator.

1. **Run the Script:** Execute the Python script in your terminal or IDE[cite: 1].
2. **Locate the Output:** The script will generate a file named `s1.svg` in the same directory[cite: 1].
3. **Import to Simulator:** 
   * Navigate to origamisimulator.org.
   * Click on **File** > **Open SVG** in the top menu.
   * Select your generated `s1.svg` file[cite: 1].
4. **Simulate:** Use the slider in the simulator to watch the flat sheet collapse into its 3D form. 

> **Important Note on Simulator Limitations:** Origami Simulator does not natively support "closed" topological sheets (like a seamlessly joined cylinder or cone). Because of this, the sheet will not automatically glue its left and right edges together. However, as you increase the fold percentage and let the physics solver run through its iterations, the geometry will naturally curl and approximate the intended conical cup shape.

---

##  How to Use (Real Life Physical Folding)

You can use the output SVG to fold this structure using real paper.

1. **Print or Plot:** Print the `s1.svg` file onto a standard sheet of paper or use a digital craft cutter to score the lines[cite: 1].
2. **Cut the Boundary:** Cut out the overall shape along the **Black** lines (the perimeter of the arc)[cite: 1].
3. **Pre-crease:** Score and fold all the interior lines according to the color legend below.
4. **Collapse:** Once all lines are pre-creased, gently pinch the zigzag patterns. The natural mechanics of the Miura-ori fold will force the paper to curve into a cone shape as it collapses.
5. **Secure (Optional):** To create a perfect cone, overlap the two straight edges of the arc and secure them with tape or glue.

---

##  Line Color Legend

The script uses standard RGB hex codes recognized by Origami Simulator to dictate fold behavior[cite: 1]:

| Color | Hex Code | Meaning in Simulator / Real Life |
| :--- | :--- | :--- |
| **Red** | `#FF0000` | **Mountain Fold:** Fold the crease so the peak points toward you[cite: 1]. |
| **Blue** | `#0000FF` | **Valley Fold:** Fold the crease so the dip points away from you (like a valley)[cite: 1]. |
| **Black** | `#000000` | **Boundary / Cut:** The outer perimeter of the paper[cite: 1]. |

---

##  How the Code Works

The script operates by mapping a standard 2D grid into **polar coordinates**[cite: 1]. Instead of plotting points on a traditional Cartesian plane, it calculates an angle (`theta`) and a radius (`r`) for every vertex[cite: 1]. By shifting the radius slightly back and forth at alternating intersections with an `offset`, it creates the signature "zig-zag" pattern required for a rigid-foldable Miura-ori tessellation[cite: 1]. 

### Parameter Guide

You can customize the shape of the cone by modifying the variables at the top of `miura_ori_maker.py`[cite: 1].

| Parameter | Default Value | Description |
| :--- | :--- | :--- |
| `r_top` | `400.0` | The radius of the outer (top) edge of the cone[cite: 1]. Scaled up to fit the simulator canvas[cite: 1]. |
| `r_bottom` | `0.0` | The radius of the inner (bottom) edge[cite: 1]. Set to `0.0` for a sharp point, or a larger number for a truncated cone. |
| `rows` | `10` | The number of horizontal rings (concentric arcs)[cite: 1]. Higher values create denser horizontal folds. |
| `cols` | `20` | The number of vertical zig-zag columns[cite: 1]. Higher values create a smoother curve but a more complex fold. |
| `angle_spread` | `math.pi * 1.2` | The total sweep of the arc[cite: 1]. Creates a curved arc that wraps into a cone[cite: 1]. |
| `zig_zag_intensity` | `15.0` | Controls how sharp the angles are[cite: 1]. Higher values make the peaks and valleys more pronounced. |
