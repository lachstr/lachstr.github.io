---
layout: post
title: "Pendulum Approximation Qualitative Analysis"
categories: misc
---

Let's see how we can use matplotlib to model pendulum motion.

![Pendulum]({{ site.baseurl }}/jupyter/pendulum-gif.gif)

Here we will examine qualitatively the applicabiltiy of the theta based model in modelling pendulum motion. Let's first consider releasing from an angle of &pi;/3. Can you tell the difference?

<video width="550" height="350" controls>
	  <source src="{{ site.baseurl }}/jupyter/quantitative-assesment.mp4" type="video/mp4">
</video> 

<video width="550" height="350" controls>
	  <source src="{{ site.baseurl }}/jupyter/quantitative-assesment-real.mp4" type="video/mp4">
</video> 

No? Let's have a look at releasing from 2&pi;/3.

<video width="550" height="350" controls>
	  <source src="{{ site.baseurl }}/jupyter/quantitative-assesment-large-angle.mp4" type="video/mp4">
</video> 
<video width="550" height="350" controls>
	  <source src="{{ site.baseurl }}/jupyter/quantitative-assesment-real-large-angle.mp4" type="video/mp4">
</video>

Qualitatively, we deduce that the theta model does not match our intuition for how real pendulums behave at large angles.

{% highlight python %}
def real_pendulum_ode(conditions, t, ℓ=0.2, g=9.8):
    ##current state of θ and ω is in the conditions list
    θ, ω = conditions
    
    dydt = [ω, -g/ℓ*sin(θ)]
{% endhighlight %}

Solving the real system is as simple as
{% highlight python %}
from scipy.integrate import odeint
solutions = odeint(real_pendulum_ode, init_conditions, t_interval)
{% endhighlight %}
Imagine doing such a calculation with pencil and paper! Newton would be proud.
