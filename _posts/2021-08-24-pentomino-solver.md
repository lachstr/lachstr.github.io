---
layout: post
title: "Pentomino Solver Animation"
categories: cs
---

In this post we will explore pentomino puzzle solving. But first, what is a pentomino?
A pentomino is a special case (n=5) of an n-omino with 5 equal sized squares connected edge-to-edge.
Without considering rotations or reflections, there are 12 distinct pentominos.

![All 18 Pentominos](https://en.wikipedia.org/wiki/Pentomino#/media/File:All_18_Pentominoes.svg)

In this project we will attempt to fill a rectangular grid full of pentominos without any gaps.
This is a harder problem than one might initially think. Anecdotetally, I have heard it might take
humans around an hour to find a solution to a 60 square board - I'm yet to try this though.

The first few pentominos are easy to place, but the final few are much more difficult!

<video controls>
  <source src="{{ site.baseurl }}/assets/rect6x10_solving.mp4" type="video/mp4">
</video>

<video controls>
  <source src="{{ site.baseurl }}/assets/pentomino.mp4" type="video/mp4"> 
</video>
