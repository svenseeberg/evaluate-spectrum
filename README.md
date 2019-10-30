# What does it do?

This script reads image files provided as an argument. Then it
calculates the vertical average for the red, green, and blue values.
The average values and the sum of the average values is written to a CSV
file.

# Why does it sum up the RGB values?

This script is about finding absorption lines in spectra. Each color
value is a signal and we want the best signal-to-noise ratio. We do not
care about visual appearance to the observer.

# License

This script is MIT licensed.
