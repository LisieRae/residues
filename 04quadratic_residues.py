# Quadratic residues

import pylab as pyl

# Try different sizes for MAX
# bigger gives a higher resolution image, but > 175 gets slow
MAX = 120 

SCALE_FACTOR = 512 # for color scaling

def plot_point(x, y, color_base):
	""" Given coordinates and a color base value,
		format the color value and plot the point
	"""
    color_formatted = '#' + hex((SCALE_FACTOR/MAX) * color_base)[2:].rjust(4, '0') + 'FF'
    pyl.plot(MAX/2. - y/2. + x, y, marker = 's', color = color_formatted)

def main():
    pyl.figure(figsize = (11.5, 10))
    pyl.gca().invert_yaxis()
    for k in range(1, MAX):
        for n in range(1, k):
            # interesting math is here
            # each point (n, k) colored by the value of its quadratic residue
			# n^2 (mod k)
            plot_point(n, k, n**2 % k)
    pyl.show()


if __name__ == '__main__':
    main()