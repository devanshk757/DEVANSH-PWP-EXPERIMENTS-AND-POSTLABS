import numpy as np
# # Define two input signals
# x = [1, 2, 3, 4]
# h = [1, 0, -1]
# # Length of the output signal = len(x) + len(h) - 1
# N = len(x) + len(h) - 1
# linear_conv = np.zeros(N)
# # Perform linear convolution using formula
# for n in range(N):
#     for k in range(len(x)):
#         if 0 <= n - k < len(h):
#             linear_conv[n] += x[k] * h[n - k]
# print("Linear Convolution:", linear_conv)





# import numpy as np
# # Define two input signals
# x = [12, 7, 10, 4]
# h = [12, 7, -10]
# # Length for circular convolution
# N = max(len(x), len(h))
# # Zero-pad the shorter sequence
# x_padded = np.pad(x, (0, N - len(x)), mode='constant')
# h_padded = np.pad(h, (0, N - len(h)), mode='constant')
# # Initialize output
# circular_conv = np.zeros(N)
# # Perform circular convolution using formula
# for n in range(N):
#     for k in range(N):
#         circular_conv[n] += x_padded[k] * h_padded[(n - k) % N]
# print("Circular Convolution:", circular_conv)




# import numpy as np
# import matplotlib.pyplot as plt
# # Define two signals
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 4, 5, 6])
# # Length of cross-correlation output = len(x) + len(y) - 1
# N = len(x) + len(y) - 1
# cross_corr = np.zeros(N)
# # Perform cross-correlation using formula
# # Formula: r_xy[n] = sum_k x[k] * y[k + n] 
# for n in range(-len(y)+1, len(x)):
#     sum_val = 0
#     for k in range(len(x)):
#         if 0 <= k + n < len(y):
#             sum_val += x[k] * y[k + n]
#     cross_corr[n + len(y) - 1] = sum_val  # shift index to start from 0
# # Plot cross-correlation
# plt.stem(cross_corr)
# plt.title('Cross-Correlation')
# plt.show()
# print("Cross-Correlation:", cross_corr)





# import numpy as np
# import matplotlib.pyplot as plt
# # Define a signal
# x = np.array([1, 2, 3, 4, 5])
# # Length of autocorrelation output = 2*len(x) - 1
# N = 2 * len(x) - 1
# auto_corr = np.zeros(N)
# # Perform autocorrelation using formula
# # Formula: r_xx[n] = sum_k x[k] * x[k+n]
# for n in range(-len(x)+1, len(x)):
#     sum_val = 0
#     for k in range(len(x)):
#         if 0 <= k + n < len(x):
#             sum_val += x[k] * x[k + n]
#     auto_corr[n + len(x) - 1] = sum_val  # shift index to start from 0
# # Plot autocorrelation
# plt.stem(auto_corr)
# plt.title('Autocorrelation')
# plt.show()
# print("Autocorrelation:", auto_corr)











#postlab
#1
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import convolve
from numpy.fft import fft, ifft
import os

# === File paths ===
audio_path = r"D:\DEGREE SEM 3\PWP MS\exp18\audio.wav"
ir_path = r"D:\DEGREE SEM 3\PWP MS\exp18\impulse.wav"


# === Read the audio and impulse response files ===
audio_rate, audio = wavfile.read(audio_path)
ir_rate, ir = wavfile.read(ir_path)

# === Convert stereo to mono (if needed) ===
if audio.ndim > 1:
    audio = np.mean(audio, axis=1)
if ir.ndim > 1:
    ir = np.mean(ir, axis=1)

# === Normalize the signals ===
audio = audio.astype(float) / np.max(np.abs(audio))
ir = ir.astype(float) / np.max(np.abs(ir))

# === Linear convolution ===
linear_conv = convolve(audio, ir, mode="full")

# === Circular convolution using FFT ===
N = len(audio) + len(ir) - 1
A = fft(audio, N)
B = fft(ir, N)
circular_conv = np.real(ifft(A * B))

# === Plot all signals ===
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(audio, color="blue")
plt.title("Original Audio Signal – 06 Devansh Karia")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(linear_conv, color="green")
plt.title("Linear Convolution (Audio * Impulse Response)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(circular_conv, color="red")
plt.title("Circular Convolution (FFT-based)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# === Normalize and save outputs ===
linear_conv_norm = (linear_conv / np.max(np.abs(linear_conv)) * 32767).astype(np.int16)
circular_conv_norm = (circular_conv / np.max(np.abs(circular_conv)) * 32767).astype(np.int16)

wavfile.write(r"D:\DEGREE SEM 3\PWP MS\linear_convolution.wav", audio_rate, linear_conv_norm)
wavfile.write(r"D:\DEGREE SEM 3\PWP MS\circular_convolution.wav", audio_rate, circular_conv_norm)


print("Saved output files:")
print("→ linear_convolution.wav")
print("→ circular_convolution.wav")








#2
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# from scipy.signal import convolve
# from numpy.fft import fft, ifft

# # === Read audio and impulse response files ===
# audio_rate, audio = wavfile.read("audio.wav")
# ir_rate, ir = wavfile.read("impulse.wav")

# # === Convert stereo to mono if needed ===
# if audio.ndim > 1:
#     audio = np.mean(audio, axis=1)
# if ir.ndim > 1:
#     ir = np.mean(ir, axis=1)

# # === Normalize signals ===
# audio = audio.astype(float) / np.max(np.abs(audio))
# ir = ir.astype(float) / np.max(np.abs(ir))

# # === Linear convolution ===
# linear_conv = convolve(audio, ir, mode="full")

# # === Circular convolution using FFT ===
# N = len(audio) + len(ir) - 1  # match linear length
# A = fft(audio, N)
# B = fft(ir, N)
# circular_conv = np.real(ifft(A * B))

# # === Plot signals ===
# plt.figure(figsize=(12, 8))

# plt.subplot(3, 1, 1)
# plt.plot(audio, color="blue")
# plt.title("Original Audio Signal – 06 Devansh Karia")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")

# plt.subplot(3, 1, 2)
# plt.plot(linear_conv, color="green")
# plt.title("Linear Convolution (Audio * Impulse Response)")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")

# plt.subplot(3, 1, 3)
# plt.plot(circular_conv, color="red")
# plt.title("Circular Convolution (FFT-based)")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")

# plt.tight_layout()
# plt.show()

# # === Normalize and save results as WAV ===
# linear_conv_norm = (linear_conv / np.max(np.abs(linear_conv)) * 32767).astype(np.int16)
# circular_conv_norm = (circular_conv / np.max(np.abs(circular_conv)) * 32767).astype(np.int16)

# wavfile.write("linear_convolution.wav", audio_rate, linear_conv_norm)
# wavfile.write("circular_convolution.wav", audio_rate, circular_conv_norm)

# print(" Convolution completed successfully!")
# print("→ Saved: linear_convolution.wav")
# print("→ Saved: circular_convolution.wav")
