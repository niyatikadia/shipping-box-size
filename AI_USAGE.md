# AI Usage Documentation

## 1. Which AI tool(s) I used
- Claude (Anthropic) — via the Claude.ai chat interface

## 2. The prompts I gave

Below is a summary of the key prompts used during development, in order:

1. Asked Claude to explain, conceptually, how to select a suitable shipping box for a product based on matching product dimensions/weight against box dimensions/capacity.
2. Asked how to handle a product that is circular/round in shape (sphere, cylinder), since it doesn't have straight length/width/height like a box.
3. Asked for the complete box-selection logic covering all possible product shapes (rectangular, cube, sphere, cylinder, plate, oval, square, triangle, irregular).
4. Asked Claude to strip the explanation down to pure logic only (no code), and then asked for the steps to be numbered in strict execution order (step 1, step 2, etc.).
5. Asked Claude to build this as a single Python file — no Django, no frontend, no login system — that runs purely in the terminal: takes product details as input, and prints the recommended box (or "no available box for the product." if nothing fits).
6. Asked Claude to add a database so the available boxes are stored outside the code instead of being hardcoded in a list.
7. Asked Claude to help prepare the final submission files: README.md, AI_USAGE.md, test cases, and test run output.

## 3. What output I accepted
- The full shape-normalization logic (converting every product shape into 3 comparable bounding dimensions) — accepted as-is, it matched my understanding of the problem.
- The sort-and-compare fitting algorithm (handling rotation by comparing sorted dimensions) — accepted, since it correctly avoids rejecting a product that would fit if rotated.
- The final `box_selector.py` script structure (input → normalize → fit-check → select best box → print result) — accepted.
- The SQLite database integration (`init_db()`, `get_all_boxes()`) for storing box data outside the code — accepted.
- The automated test cases covering normal fits, oversized products, overweight products, rotated dimensions, and boundary cases — accepted after reviewing that all 8 passed.

## 4. What output I rejected or modified
- Initially, Claude's example code outputs were in a multi-file / Django-style structure (models, views, admin) matching the original assignment brief. I rejected this structure and asked Claude to simplify to a single-file, terminal-only Python script instead, since that is what I wanted to build and understand first.
- I rejected the idea of keeping box data hardcoded in the Python file long-term and asked for it to be moved into a real database (SQLite) instead.

## 5. Any mistakes the AI made
- No functional/logic bugs were found in the generated code after testing.
- One thing I had to manage myself: making sure I understood *why* the sorting/rotation logic works (comparing sorted dimensions instead of raw length-width-height) rather than just copying it blindly — I asked Claude to re-explain this step-by-step until it was clear to me.

## 6. How I verified the final code
- Ran `box_selector.py` manually multiple times with different shapes (rectangular, sphere) and checked the recommended box and its specification were logically correct against the box catalog.
- Ran `test_cases.py`, which contains 8 automated test cases (normal fits, oversized product with no match, overweight product with no match, cylinder shape, rotated dimensions producing the same result, exact-boundary fit, and largest-size product). All 8 passed — output captured in `TEST_OUTPUT.md`.
- Manually cross-checked the box catalog values seeded into the database against the expected results for each test case.
