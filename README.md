# Shipping Box Selection System

A simple terminal-based Python program that recommends the most suitable shipping box for a product, based on the product's shape, dimensions, and weight.

## What it does

Given a product's shape (rectangular, cube, sphere, cylinder, plate, oval, square, or triangle), its measurements, and its weight, the program finds the **tightest-fitting available box** that can safely hold it — not too small, not unnecessarily large.

If no box in the database is big enough or strong enough (weight-wise) for the product, it clearly returns:
```
no available box for the product.
```

## How it works (logic)

1. The product's shape is converted into 3 comparable "bounding box" dimensions (e.g. a sphere becomes `[diameter, diameter, diameter]`, a cylinder becomes `[diameter, diameter, height]`, etc.)
2. Both the product's dimensions and each box's internal dimensions are sorted largest → smallest, so rotation is accounted for.
3. A box is a valid candidate only if every sorted product dimension ≤ the matching sorted box dimension, **and** the product's weight is within the box's max weight capacity.
4. Among all valid candidate boxes, the one with the **smallest volume** is chosen (cheapest as a tiebreaker) — guaranteeing the closest fit.

## Tech used

- Python 3
- SQLite (via Python's built-in `sqlite3` module) — stores the available box catalog in `boxes.db`, created automatically on first run

## Files in this repository

| File | Purpose |
|---|---|
| `box_selector.py` | Main program — run this to select a box for a product |
| `test_cases.py` | Automated tests for the core selection logic |
| `TEST_OUTPUT.md` | Captured output from running the test cases |
| `AI_USAGE.md` | Documentation of AI tool usage during development |
| `README.md` | This file |

## How to run

```bash
python box_selector.py
```

You'll be prompted to enter:
- The product's shape
- Shape-specific measurements (e.g. length/width/height, or diameter, etc.)
- The product's weight

The program will then print the recommended box along with its full specification (dimensions, max weight capacity, cost) — or tell you no suitable box is available.

## How to run tests

```bash
python test_cases.py
```

This runs 8 automated test cases covering normal fits, oversized products, overweight products, rotated dimensions, boundary (exact-fit) cases, and different shapes. See `TEST_OUTPUT.md` for the last captured run.

## Default box catalog (seeded automatically into `boxes.db`)

| Box | L (cm) | W (cm) | H (cm) | Max Weight (kg) | Cost |
|---|---|---|---|---|---|
| XS Box | 10 | 10 | 10 | 1 | 10 |
| S Box | 20 | 15 | 10 | 3 | 15 |
| M Box | 30 | 20 | 20 | 8 | 25 |
| L Box | 40 | 30 | 30 | 15 | 40 |
| XL Box | 60 | 40 | 40 | 25 | 60 |
| XXL Box | 80 | 60 | 60 | 40 | 90 |
