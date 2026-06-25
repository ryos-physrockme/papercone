# Cycle 4: semantic layout

Goal: make the x-y plane represent semantic similarity rather than arbitrary fixture coordinates.

## Desired experience

Papers about nearby ideas appear close together in the x-y plane, while publication time remains the z-axis.

## First implementation plan

1. Build an embedding interface over paper text.
2. Use title and abstract as the initial text source.
3. Project embeddings to 2D with PCA.
4. Export x, y, z coordinates for visualization.

## Why PCA first

UMAP or force-directed layouts may look more dramatic, but PCA is easier to debug and tends to be more stable during early development.

## Later options

- UMAP
- PaCMAP
- citation-aware layout
- hybrid semantic and graph-force layout
- local neighborhood stabilization so maps do not jump too much between runs
