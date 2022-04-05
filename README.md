# FMC Skeleton Finder
This repository is an algorithm for training a neural network to find FMC skeletons.

## What is FMC?

FMC stands for Fewest Moves Challenge. The goal is to solve a Rubik's Cube in the fewest number of moves possible. 

## What is a Skeleton?

In the context of FMC a skeleton is a list of moves from which the rest of the cube is solved. Most methods for doing FMC can be broken down into two main steps: finding 
a skeleton and solving the rest by backtracking through the skeleton. A good skeleton should solve as many pieces as possible in as fewer moves as possible. This can be 
done systematically (i.e. by block building) but generally this step involves a large amount of intutition on the part of the solver.

## Basic Idea Behind The Algorithm

When finding a skeleton there are too many possibilities for a computer to exhaustively search through in a reasonable amount of time. So to speed up the search this 
algorithm trains the neural network to assign a number between 0 and 1 to every move depending how likely it thinks that move will lead to a good skeleton. This way the 
search tree explores the most promising paths first.

## Inspiration

The ideas behind the algorithm are not unique to me. This works very similarly to the policy neural network in AlphaGo which like my algorithm assigned numbers to a 
search tree depending on how likely it thought it was going to win from that position. The main difference is that the environment I am using can be interpreted as a
one player game whereas Go is a two player game.
