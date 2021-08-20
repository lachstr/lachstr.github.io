---
layout: post
title: "Bessel Function Animation"
categories: misc
---

Bessel’s differential equation is given by:

<img src="https://latex.codecogs.com/svg.latex?x^2&space;\frac{d^2y}{dx^2}&space;&plus;&space;x&space;\frac{dy}{dx}&space;&plus;&space;(x^2&space;-&space;n^2)y&space;=&space;0" title="x^2 \frac{d^2y}{dx^2} + x \frac{dy}{dx} + (x^2 - n^2)y = 0" />

It is a 2-dimensional wave equation, having many applications in physics including the notable examples: 

- describing electromagnetic waves in a cylindrical wave-guide
- solving the radial Schrodinger Equation for a free particle
- modes of vibration on a circular drum. 

For integer <img src="https://latex.codecogs.com/svg.latex?\inline&space;n" title="n" /> it has the series solution:

<img src="https://latex.codecogs.com/svg.latex?J_n(x)&space;=&space;\sum_{l=0}^{N}&space;\frac{(-1)^l}{2^{2l&plus;n}&space;l!&space;(n&plus;l)!}&space;x^{2l&plus;n}" title="J_n(x) = \sum_{l=0}^{N} \frac{(-1)^l}{2^{2l+n} l! (n+l)!} x^{2l+n}" />

as <img src="https://latex.codecogs.com/svg.latex?\inline&space;N&space;\rightarrow&space;\infty" title="N \rightarrow \infty" />

We can use python to approximate <img src="https://latex.codecogs.com/svg.latex?\inline&space;J_n(x)" title="J_n(x)" /> using increasingly large <img src="https://latex.codecogs.com/svg.latex?\inline&space;N" title="N" />. 

The function could look something like this;

```python
def bessj(n, x, N):
    partial_sum = 0
    
    from math import factorial 
    for l in range(N+1):
        partial_sum += (-1)**l/(2**(2*l+n)*factorial(l)*factorial(n+l))*x**(2*l+n)
    
    return partial_sum
``` 

We could then plot the bessel function approximation for larger values of <img src="https://latex.codecogs.com/svg.latex?\inline&space;N" title="N" />. We'll also plot <img src="https://latex.codecogs.com/svg.latex?\inline&space;J_1(x),&space;J_2(x),&space;J_3(x),&space;J_4(x),&space;J_5(x),&space;J_6(x)" title="J_1(x), J_2(x), J_3(x), J_4(x), J_5(x), J_6(x)" />.

```python
import numpy as np
import matplotlib.pyplot as plt

def bessel_plotter(N):
    plt.xlabel("x")
    plt.ylabel("J_n(x)")
    plt.title(f"Bessel Function Types (Order {N})")
    x_domain = np.linspace(0, 15, 1000)
    
    for kind in [1, 2, 3, 4, 5, 6]:
        plt.plot(x_domain, bessj(kind, x_domain, N), label = f'n = {kind}')

    return plt.legend()
```

With abit of matplotlib magic we can animate this process:

<video width="800" height="428" controls>
	  <source src="{{ site.baseurl }}/jupyter/bessel.mp4" type="video/mp4">
</video> 

Beautiful!