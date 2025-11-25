# import numpy as np
# from scipy.signal import TransferFunction

# def analyze_z_transfer_function(num, den):
#     # Create a Transfer Function object
#     system = TransferFunction(num, den)

#     # Get the poles and zeros
#     zeros = system.zeros
#     poles = system.poles
#     print("Zeros:", zeros)
#     print("Poles:", poles)

#     # Stability Analysis (Z-domain logic)
#     stable = all(np.abs(pole) < 1 for pole in poles)
#     print("Stability:", "Stable" if stable else "Unstable")


# num = [1, -0.5]        
# den = [1, -0.2, 0.3]   

# analyze_z_transfer_function(num, den)






# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import TransferFunction, bode

# def analyze_z_transfer_function(num, den):
#     # Create Transfer Function object
#     system = TransferFunction(num, den)

#     # Poles and Zeros
#     zeros = system.zeros
#     poles = system.poles

#     print("Zeros:", zeros)
#     print("Poles:", poles)

#     # Stability (Z-domain: poles must be inside unit circle)
#     stable = all(np.abs(pole) < 1 for pole in poles)
#     print("Stability:", "Stable" if stable else "Unstable")

#     # Causality analysis (simple check)
#     causal = len(den) >= len(num)
#     print("Causality:", "Causal" if causal else "Non-Causal")

#     # Time invariance
#     time_invariant = True
#     print("Time Invariance:", "Time Invariant" if time_invariant else "Time Variant")

#     # Bode plot
#     w, mag, phase = bode(system)

#     # Plot
#     plt.figure(figsize=(12, 8))

#     # Magnitude plot
#     plt.subplot(2, 1, 1)
#     plt.semilogx(w, mag)
#     plt.title("Bode Magnitude Plot")
#     plt.xlabel("Frequency [rad/s]")
#     plt.ylabel("Magnitude [dB]")
#     plt.grid()

#     # Phase plot
#     plt.subplot(2, 1, 2)
#     plt.semilogx(w, phase)
#     plt.title("Bode Phase Plot")
#     plt.xlabel("Frequency [rad/s]")
#     plt.ylabel("Phase [degrees]")
#     plt.grid()

#     plt.tight_layout()
#     plt.show()


# # -----------------------------------------------------
# # Example system H(z) = (z^2 + 0.5) / (z^2 - 1.5z + 0.5)
# # -----------------------------------------------------

# num = [1, 0.5]       # numerator coefficients
# den = [1, -1.5, 0.5] # denominator coefficients

# analyze_z_transfer_function(num, den)







# postlab
#1
# import sympy as sp
# def z_transform_unit_step():
#     z = sp.symbols('z')
#     U_z = 1 / (1 - z**-1)
#     print("Z-transform of unit step u[n]:")
#     print("U(z) =", sp.simplify(U_z))
#     pole = 1  
#     print("\nPole at:", pole)
#     if abs(pole) < 1:
#         print("System is: Stable")
#     else:
#         print("System is: Unstable")
# z_transform_unit_step()




#2
import numpy as np
def analyze_Hz():
    num = np.poly([0.7, 0.9]) * 0.5    
    den = np.poly([0.6, 0.4])           
    print("Numerator Coefficients:", num)
    print("Denominator Coefficients:", den)
    zeros = np.roots(num)
    poles = np.roots(den)
    print("\nZeros:", zeros)
    print("Poles:", poles)
    stable = all(np.abs(p) < 1 for p in poles)
    print("\nStability:", "Stable" if stable else "Unstable")
analyze_Hz()
