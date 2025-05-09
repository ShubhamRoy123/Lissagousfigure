import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
initial_amplitude_x = 1.0
initial_amplitude_y = 1.0
initial_frequency1 = 1
initial_frequency2 = 1
initial_phase = np.pi / 2
t = np.linspace(0, 1, 1000)

#figure
fig, (ax_lissajous, ax_x, ax_y) = plt.subplots(3, 1, figsize=(1, 8))
plt.subplots_adjust(left=0.1, bottom=0.4)

# Initial sine waves
x = initial_amplitude_x * np.sin(2 * np.pi * initial_frequency1 * t)
y = initial_amplitude_y * np.sin(2 * np.pi * initial_frequency2 * t + initial_phase)

#Lissajous curve
line_lissajous, = ax_lissajous.plot(x, y, color="orange")
ax_lissajous.set_title("Lissajous Curve")
ax_lissajous.grid(True)

# Plot x-axis graph
line_x, = ax_x.plot(t, x, color="blue")
ax_x.set_title("Sine Wave X (Time vs Amplitude)")
ax_x.set_xlabel("Time (s)")
ax_x.set_ylabel("Amplitude")
ax_x.grid(True)

# Plot y-axis graph
line_y, = ax_y.plot(t, y, color="green")
ax_y.set_title("Sine Wave Y (Time vs Amplitude)")
ax_y.set_xlabel("Time (s)")
ax_y.set_ylabel("Amplitude")
ax_y.grid(True)

# Add sliders for amplitudes and frequencies
amp_x_slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
freq1_slider_ax = plt.axes([0.1, 0.25, 0.8, 0.03])
amp_y_slider_ax = plt.axes([0.1, 0.15, 0.8, 0.03])
freq2_slider_ax = plt.axes([0.1, 0.3, 0.8, 0.03])

amp_x_slider = Slider(amp_x_slider_ax, "Amplitude Sine X", 0.1, 2.0, valinit=initial_amplitude_x)
freq1_slider = Slider(freq1_slider_ax, "Frequency Sine X", 1, 10, valinit=initial_frequency1)
amp_y_slider = Slider(amp_y_slider_ax, "Amplitude Sine Y", 0.1, 2.0, valinit=initial_amplitude_y)
freq2_slider = Slider(freq2_slider_ax, "Frequency Sine Y", 1, 10, valinit=initial_frequency2)

# Update function
def update(val):
    amp_x = amp_x_slider.val
    amp_y = amp_y_slider.val
    freq1 = freq1_slider.val
    freq2 = freq2_slider.val
    x = amp_x * np.sin(2 * np.pi * freq1 * t)
    y = amp_y * np.sin(2 * np.pi * freq2 * t + initial_phase)
    line_lissajous.set_xdata(x)
    line_lissajous.set_ydata(y)
    line_x.set_ydata(x)
    line_y.set_ydata(y)
    ax_x.set_ylim(-1.5 * amp_x, 1.5 * amp_x)
    ax_y.set_ylim(-1.5 * amp_y, 1.5 * amp_y)
    fig.canvas.draw_idle()

# Connect sliders to the update function
amp_x_slider.on_changed(update)
freq1_slider.on_changed(update)
amp_y_slider.on_changed(update)
freq2_slider.on_changed(update)

plt.show()