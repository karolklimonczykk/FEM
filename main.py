import math
import numpy as np
import matplotlib.pyplot as plt

# Length of the beam
L = 5

# Number of elements
num_elements = 10

# Diameter of the beam
diameter = 0.175

# Applied force
F = 1800

# Element length
element_length = L / num_elements

# Moment of inertia
I = (math.pi * pow(diameter, 4)) / 64

# Young's modulus
E = 2.0e11

# Cross-sectional area
A = (math.pi * (pow(diameter / 2, 2)))

# Axial stiffness factor
a1 = E * (A / element_length)

# Flexural stiffness factor
a2 = E * (I / pow(element_length, 3))

# Total number of nodes
total_nodes = num_elements + 1

# Total number of degrees of freedom
total_dofs = total_nodes * 3

print(total_dofs)

# Element stiffness matrix
ke = np.matrix([[a1, 0, 0, -a1, 0, 0],
                [0, 12 * a2, 6 * a2, 0, -12 * a2, 6 * a2],
                [0, 6 * a2, 4 * a2, 0, -6 * a2, 2 * a2],
                [-a1, 0, 0, a1, 0, 0],
                [0, -12 * a2, -6 * a2, 0, 12 * a2, -6 * a2],
                [0, 6 * a2, 2 * a2, 0, -6 * a2, 4 * a2]])

print("ELEMENT MATRIX ke:")
print(ke)
print("______________________________________________________________________________")

# Global stiffness matrix assembly
K = np.zeros((total_dofs, total_dofs))
for i in range(0, num_elements):
    K[0 + (3 * i):6 + (3 * i), 0 + (3 * i):6 + (3 * i)] += ke
print("GLOBAL MATRIX (before applying boundary conditions): ")
print(K)
print("______________________________________________________________________________")

# Applying boundary conditions by eliminating rows and columns
print("GLOBAL MATRIX (after applying boundary conditions): ")
K = np.delete(K, [0, 1, 16], axis=0)
K = np.delete(K, [0, 1, 16], axis=1)
print(K)
print("______________________________________________________________________________")

# Generating load vector
load_vector = np.zeros(len(K))
load_vector[len(load_vector) - 2] = -F

print("LOAD VECTOR: ")
print(load_vector)
print("______________________________________________________________________________")

# Solving for displacement vector
displacement_vector = np.linalg.solve(K, load_vector)
print("DISPLACEMENT VECTOR: ")
print(displacement_vector)
print("______________________________________________________________________________")

# Analytical solution for displacement
analytical_displacement = (F * pow(L, 3)) / (12 * E * I)
print("Analytical solution for displacement: ")
print(analytical_displacement)

# Displacement calculated using FEM
fem_displacement = displacement_vector[len(displacement_vector) - 2]
print("Displacement calculated using Finite Element Method (FEM): ")
print(abs(fem_displacement))

# Error calculation
error = abs(abs(fem_displacement) - analytical_displacement)
print("Measurement accuracy error: ")
print(error)
print("______________________________________________________________________________")

# Plotting the displacement results
x = np.zeros(11)
for i in range(1, 11):
    x[i] = i * element_length
y = np.zeros(11)
for i in range(0, 10):
    y[i + 1] = displacement_vector[1 + (i * 3)]

plt.plot(x, y, marker='o')
plt.title('Displacement Plot at Finite Element Mesh Nodes')
plt.xlabel('Distance [m]')
plt.ylabel('Displacements [m]')
plt.grid(True)
plt.show()
