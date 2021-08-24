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

Play the videos below to see how the computer solves this problem.

<video controls>
  <source src="{{ site.baseurl }}/assets/rect6x10_solving.mp4" type="video/mp4">
</video>

<video controls>
  <source src="{{ site.baseurl }}/assets/pentomino.mp4" type="video/mp4"> 
</video>

## Code discussion

Looking at the visualisations above it might seem that the computer is abit stupid.
It works tirelessly trying different rotations and positions in one corner of the board
while there is an enclosed gap in another area - meaning there is no chance of finding a solution. 
However, it is worth noting just how quickly the computer finds a solution - on my modern laptop it takes less than 4 tenths of a second to find the second (more difficult) solution (and write all the steps to a file).

This is Java code, with no attempt made to optimize for efficiency - so there is room for improvement.

An important consideration is the simplicity of this algorithm - it is just a depth first search of a graph.
In this context, the graph nodes are the board layouts and the graph vertices are the pendominos.

Those famillar with depth first search may find the following method in the `Solver` class satisfying;

```Java
public class GridNode {
    public char[][] grid;
    private ArrayList<Character> avaliableTypes = new ArrayList<>();

    public GridNode(char[][] grid, ArrayList<Character> avaliableTypes);
    public ArrayList<Character> getPentominoTypes();
    public Coordinate getCoordinateToPlace();
    public GridNode copy();
    public ArrayList<Pentomino> generateEdges();
}

/*******/

 private GridNode aSolution(GridNode firstNode, boolean reusablePentominoes){
    	/*Depth first search for a solution*/
		GridNode node = firstNode;
		Stack<GridNode> stack = new Stack<GridNode>();
		HashSet<String> seen = new HashSet<>();


		stack.add(node);

		while (stack.size()>0){
			node = stack.pop();

			ArrayList<Pentomino> allPermutations = node.generateEdges();

			if (node.getCoordinateToPlace() == null){
				return node;
			}

			for (Pentomino p : allPermutations){

				if (p.canPlaceOn(node)){

					GridNode newNode = node.copy();
					p.placeOn(newNode);

					if (!reusablePentominoes){
						newNode.removePentominoType(p.getType());
					}

					stack.push(newNode);
				}
			}

		}
		return null;
	}
```

