'''water_shape.py...'''

def height_constant(glass_info, speed):
	'''Returns the constant for the height equation.

	The constant for the height equation can be found by integrating
	the height equation of the cross-sectional area of the glass
	and setting that equal to the volume of the water. 

	Args:
		glass_info : dictionary of information about the glass
		speed : rotational speed of plate.
	Returns:
		h_0 : constant of the height equation.
	'''

	m = glass_info['mass_water']
	p = 1000  # density of water, kg/m^3
	a = glass_info['alpha']
	r_0 = glass_info['r_0']
	r_1 = glass_info['r_1']
	g = 9.8  # acceleration of gravity, m/s^2

	first_element = 2 * m / (p * a * (r_1**2 - r_0**2))
	second_element = (r_1**4 - r_0**4) * speed**2 / (4 * g)
	return first_element - second_element


def height(glass_info, r, speed):
	'''Returns the height of the water at a given radius.

	This equation can be derived by assumed the sum of forces on an element
	of water at the surface is perpendicular to the angle of the water surface
	at that point.

	Args:
		glass_info : dictionary of information about the glass
		r : radius in m.
		speed : rotational speed in radians per second.
	Returns:
		h : height in m.
	'''
	h_0 = height_constant(glass_info, speed)

	return h_0 + ((speed * r)**2 / (2 * 9.8))


def main(glass_info, speed):
	'''Calculates the delta center of gravity given the shape of the water
	and whether or not the water reaches the brim of the glass.

	Args:
		glass_info : dictionary of physical properties of glass
		speed : speed of rotation in radians per second.
	Returns:
		results : (brim, delta_water_cg)
				brim : boolean if water reaches brim (1) or not (0)
				delta_water_cg: (delta in m radially, delta in m of height)
	'''

	delta_water_cg = (0, 0)

	max_h = height(glass_info, glass_info['r_1'], speed)
	if max_h > glass_info['height']:
		return (1, delta_water_cg)
	return (0, delta_water_cg)
