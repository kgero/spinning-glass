Spinning Glass Calculation / Sim
=========================

The goal of this project is to create a tool for solving the following problem:

You have a glass of water on revolving tray, such as a lazy Susan. The tray slowly
begins to rotate. As the tray rotates faster and faster, what happens first?

1. The glass slides off the tray
2. The glass tips over
3. The water in the glass is flung out of the glass (without the glass falling over)

(Acceleration is slow. Assume steady state)

## Glass Sliding Calculation

This calculation is fairly simple. The glass begins to slide when the centripetal force of the rotation is greater than the frictional force between the glass and the tray.

centripetal force = mass * rotational speed^2 * distance from center of rotation

frictional force = coefficient of friction * mass * gravity

## Water Shape Calculation

Here we assume that the shape the water takes in the glass is the same as it would be if water 'filled' the entire tray. This means we can figure out the shape of the water as if it were in a giant bucket on the tray, and then just pay attention to the part our glass occupies.

picture to demonstrate what this means!

The height of the water as a function of the radius can be derived given this assumption about the situation: the slope of the surface of the water at a particular point is perpendicular to the angle of the resultant force on the water at this point. If the resultant force were not perpendicular to the slope, the water would move! This (hopefully) makes intuitive sense. When water is in an unmoving container, the slope of the surface is horizontal, because the resultant force (just the force of gravity) is directed vertically. 

picture of this too!

But what we're looking for is the height as a function of the radius -- h(r). If we look at a single point of water on the surface, we can find the force of gravity, the centripetal force of rotation, and the resultant force which is the sum of the two. We can then find the tangent of the angle perpendicular to the resultant force, and set that equal to the slope of h(r). (Remember, tangent = rise over run.) This means we've found the derivative of h(r), and therefore can integrate it to find an equation for h(r). (You can find more information about this if you look up the Bucket Argument.)

picture of force diagram and dh/dr, integrate to get h(r)

But we still don't know what h<sub>0</sub> is! It will determine how "high" the curve is. This must be a function of the volume, because that's what will set our height. To find it, we can integrate h(r) over the area of our glass, set that equal to the volume and solve for h<sub>0</sub>.

Here's the thing: integrating over a circle sounds like a pain in the ass. Maybe we'll implement that eventually, but for now we'll do the tactical engineering thing and pick a simpler problem to solve. Let's integrate over a wedge that looks like this:

wedge shape

This is way easier. We can do a definite integral from r<sub>0</sub> to r<sub>1</sub> of **alpha * r * h(r) * dr**.

## File Structure

- main.py 
  - Description: (will run the simulation, increaseing spinning speed until failture)
  - Args: glass size, amount of water, distance from center, friction
  - Return: what failed, at what speed

- src/glass_slides.py 
  - Description: (calc force on glass, is it enough to slide?)
  - Args: physical variables, speed
  - Return: slide?(0/1)

- src/water_shape.py 
  - Description: (where the water is in the glass, where the CG of the water is, does it reach the brim?)
  - Args: physical variables, speed
  - Return: brim?(0/1), delta_water_CG

- src/glass_tips.py
  - Description: (moment on glass (given water CG), enough to tip?)
  - Args: physical variables, speed, delta_water_CG
  - Return: tips?(0/1)

Physical Variables

- Volume of water
- Height of glass
- Bottom radius of glass
- Top radius of glass
- Thickness of glass
- Glass density
- Cf of friction
- Distance from center of rotating tray
