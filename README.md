# Heat Conduction in a Slab

This repository contains Python code for simulating heat conduction in a slab with various boundary conditions, thermal properties, and heat generation. The temperature distribution is calculated and visualized based on the governing heat conduction equations.

## Project Overview

This project explores the thermal behavior of a slab of material with thickness \( L \), subject to heat generation \( Q_g \) and different boundary conditions. The temperature at the slab ends and the effect of thermal conductivity \( K \) are taken into account to calculate the temperature distribution across the slab. 

### Key Features:
- Solves heat conduction problems with heat generation within the slab.
- Visualizes temperature distribution using Python's `matplotlib` library.
- Supports various thermal boundary conditions and parameters like slab length, heat generation, and thermal conductivity.

## Formulas Used

### 1. **Temperature Distribution Without Heat Generation (Linear)**
When the slab is not subjected to any internal heat generation but is subject to known temperatures at its ends, the temperature distribution is linear. The equation is:
\[ T(x) = -\frac{(T_1 - T_2)}{L} \cdot x + T_1 \]

Where:
- \( T_1 \) and \( T_2 \) are the temperatures at the ends of the slab.
- \( L \) is the length of the slab.
- \( T(x) \) is the temperature at a distance \( x \) from one end of the slab.

### 2. **Temperature Distribution With Heat Generation**
When there is uniform heat generation within the slab, the temperature distribution becomes parabolic:
\[ T(x) = -\frac{Q_g}{2K} \cdot x^2 + \frac{(T_2 - T_1)}{L} \cdot x + \frac{Q_g \cdot L \cdot x}{2K} + T_1 \]

Where:
- \( Q_g \) is the rate of heat generation per unit volume.
- \( K \) is the thermal conductivity of the material.
- \( L \) is the thickness of the slab.
- \( T(x) \) is the temperature at a point \( x \) in the slab.

### 3. **Temperature Distribution With Symmetrical Conditions (Axisymmetric Heat Transfer)**
In the case of symmetrical heat transfer across a slab where both surfaces are at the same temperature \( T_1 \), the equation becomes:
\[ T(x) = 4 \cdot ( \zeta - \zeta^2 ) \cdot (T_{max} - T_1) + T_1 \]
Where:
- \( T_{max} = T_1 + \frac{Q_g \cdot L^2}{8 \cdot K} \) is the maximum temperature at the center of the slab.
- \( \zeta = \frac{x}{L} \) is the normalized position along the slab.

### 4. **Convective Heat Transfer from the Slab to Surroundings**
When heat is transferred from the slab to the surrounding fluid at temperature \( T_{\infty} \) (ambient temperature), the heat transfer coefficient \( h \) at the wall can be calculated as:
\[ h = \frac{Q_g \cdot L}{2 \cdot \theta_w} \]
Where:
- \( \theta_w = T_w - T_{\infty} \) is the temperature difference between the wall and the fluid.
- \( T_w \) is the temperature at the wall.

The temperature distribution under these conditions is given by:
\[ T(x) = \frac{Q_g}{8K} \cdot (L^2 - 4x^2) + \frac{Q_g \cdot L}{2h} + T_{\infty} \]

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iammohith/Heat-Conduction-in-a-slab.git
   ```
   
2. **Install dependencies**:
   Make sure you have Python installed, and then install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the simulations**:
   The Python scripts simulate different cases of heat conduction through the slab. To run a script, execute:
   ```bash
   python script_name.py
   ```

4. **Modify Parameters**:
   You can change parameters such as \( T_1 \), \( T_2 \), \( L \), \( Q_g \), and \( K \) in the scripts to test different thermal scenarios.

## Visualizations

The temperature distributions are plotted using `matplotlib`. Each script generates a plot showing the temperature across the slab. Here's an example of a typical temperature distribution graph:
- **X-axis**: Distance from one end of the slab.
- **Y-axis**: Temperature at that distance.

## References

1. **Heat and Mass Transfer: Fundamentals & Applications**  
   *Afshin J. Ghajar and Yunus A Çengel*  
   [Link to book](https://www.mheducation.com/)

2. **Heat and Mass Transfer**  
   *R.K. Rajput*  
   [Link to book](https://www.schandpublishing.com/)

3. **Python Documentation**  
   Official Python documentation for libraries like `numpy` and `matplotlib`:  
   [Python Documentation](https://docs.python.org/3/)

## License

This project is open source and available under the [MIT License](LICENSE).
