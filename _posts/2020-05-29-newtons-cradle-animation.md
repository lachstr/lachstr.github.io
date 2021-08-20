---
layout: post
title: "Newton's Cradle Animation"
categories: misc
---
The purpose of this project is to animate Newton's Cradle from first principles. Newton's Cradle has been animated before however typically via a key-frame method or one reliant on a complicated physics engine. In this post we will animate Newton's Cradle by implementing our own minimalist physics engine. We will use the following guiding statement to develop our simulator;

"Newton's Cradle can be modelled as multiple pendulums confined to swing along a single axis which undergo elastic collisions with one another. The pendulums rest such that there is a small amount of horizontal displacement between their masses.''

Here a pendulum means a mass attached to a massless, rigid, fixed-length <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\ell" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\ell" title="\ell" /></a> with an angle <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\theta" title="\theta" /></a> to the vertical which obeys differential equation 

<a href="https://www.codecogs.com/eqnedit.php?latex=\ddot{\theta}&space;=&space;-\frac{g}{\ell}\sin(\theta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\ddot{\theta}&space;=&space;-\frac{g}{\ell}\sin(\theta)" title="\ddot{\theta} = -\frac{g}{\ell}\sin(\theta)" /></a>

Here "elastic" means the collisions occur conserving energy and momentum.

For a more precise mathematical description please see this [white paper]({{ site.baseurl }}/cradle/cradle_report.pdf).

The [Runge–Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) numerical integration technique was used.

The code used to produce the following animations can be found [here](https://github.com/lachstr/cradle/blob/master/video_out/newtons_cradle_equalmass_simulator.ipynb). However, this pseudocode gives an idea of the general approach;

```python
for t in time_interval:
    cradle.CheckForCollisions()
    
    for pendulum in cradle.pendulums:
        pendulum.IntegrateStep(t)
    
    cradle.plot()
```

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/2_masses_1_raised.mp4" type="video/mp4">
</video> 

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/3_masses_1_raised.mp4" type="video/mp4">
</video> 

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/5_masses_3_raised.mp4" type="video/mp4">
</video> 

<a name="middle_pendulum_motion"></a>
## middle pendulum motion
Watching these animations closely, we notice that the once stationary middle masses begin to move after some time. The same phenomena can be seen in this video of a real cradle. This is a remarkable result.

<iframe width="680" height="428" src="https://www.youtube.com/embed/0LnbyjOyEQ8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The explanation for this originates from what we meant by the separation between pendulums being small.

With our simulated system we can place the pendulums closer together. Observe how this increases the time before the motion of the internal masses becomes obvious. 

Original separation between pendulums
<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/3_masses_1_raised.mp4" type="video/mp4">
</video> 
1/100th of original separation between pendulums
<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/3_masses_1_raised_closer_at_rest.mp4" type="video/mp4">
</video> 

We could continue placing the masses closer and closer together, yet this comes at the cost of computation time. I thought this was an interesting observation.

<a name="non-equal_masses"></a>
## non-equal masses

The code used to produce the following animations can be found [here](https://github.com/lachstr/cradle/blob/master/video_out/newtons_cradle_variable_mass.ipynb).

In this animation we require that each mass has the same density, meaning the larger radii on the right has a larger mass.

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/2_small_1_big.mp4" type="video/mp4">
</video> 

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/4_small_1_big.mp4" type="video/mp4">
</video> 

## extra animations

<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/5_masses_1_raised.mp4" type="video/mp4">
</video> 
<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/5_masses_2_raised_closer_at_rest.mp4" type="video/mp4">
</video> 
<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/5_masses_3_raised_closer_at_rest.mp4" type="video/mp4">
</video> 
<video width="680" height="428" controls>	  <source src="{{ site.baseurl }}/cradle/5_masses_4_raised_closer_at_rest.mp4" type="video/mp4">
</video> 