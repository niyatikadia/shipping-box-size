"""
Test cases for box_selector.py

Run with: python test_cases.py

These tests check the core logic (normalize_product, fits, select_best_box)
directly, without needing terminal input, by building product dictionaries
manually and comparing against the box database.
"""

from box_selector import init_db, get_all_boxes, normalize_product, fits, select_best_box

init_db()
boxes = get_all_boxes()

passed = 0
failed = 0


def check(test_name, condition):
    global passed, failed
    if condition:
        print(f"[PASS] {test_name}")
        passed += 1
    else:
        print(f"[FAIL] {test_name}")
        failed += 1


# ---------------------------------------------------------
# Test 1: Small rectangular product -> should fit a small box
# ---------------------------------------------------------
product1 = {"shape": "rectangular", "dims": {"length": 8, "width": 8, "height": 8}, "weight": 0.5}
result1 = select_best_box(product1, boxes)
check("Small rectangular product gets a box (XS Box expected)", result1 is not None and result1["name"] == "XS Box")


# ---------------------------------------------------------
# Test 2: Medium rectangular product -> should fit M Box
# ---------------------------------------------------------
product2 = {"shape": "rectangular", "dims": {"length": 25, "width": 18, "height": 15}, "weight": 4}
result2 = select_best_box(product2, boxes)
check("Medium rectangular product gets M Box", result2 is not None and result2["name"] == "M Box")


# ---------------------------------------------------------
# Test 3: Oversized sphere -> should return None (no box fits)
# ---------------------------------------------------------
product3 = {"shape": "sphere", "dims": {"length": 100, "width": 100, "height": 100}, "weight": 50}
result3 = select_best_box(product3, boxes)
check("Oversized sphere returns no available box", result3 is None)


# ---------------------------------------------------------
# Test 4: Product fits dimensionally but exceeds weight limit -> no box
# ---------------------------------------------------------
product4 = {"shape": "rectangular", "dims": {"length": 5, "width": 5, "height": 5}, "weight": 999}
result4 = select_best_box(product4, boxes)
check("Overweight (but small) product returns no available box", result4 is None)


# ---------------------------------------------------------
# Test 5: Cylinder product -> correctly normalized and fits a box
# ---------------------------------------------------------
product5 = {"shape": "cylinder", "dims": {"length": 12, "width": 12, "height": 25}, "weight": 2}
result5 = select_best_box(product5, boxes)
check("Cylinder product gets a valid box", result5 is not None)


# ---------------------------------------------------------
# Test 6: Rotated product -> dims in different order should still fit
# (10x30x5 should fit the same box as 30x10x5, since rotation is allowed)
# ---------------------------------------------------------
product6a = {"shape": "rectangular", "dims": {"length": 10, "width": 30, "height": 5}, "weight": 2}
product6b = {"shape": "rectangular", "dims": {"length": 30, "width": 5, "height": 10}, "weight": 2}
result6a = select_best_box(product6a, boxes)
result6b = select_best_box(product6b, boxes)
check("Rotated dimensions select the same box", result6a is not None and result6b is not None and result6a["name"] == result6b["name"])


# ---------------------------------------------------------
# Test 7: Exact boundary fit -> product dims exactly equal to box dims should pass
# ---------------------------------------------------------
m_box = next(b for b in boxes if b["name"] == "M Box")
product7 = {"shape": "rectangular", "dims": {"length": m_box["length"], "width": m_box["width"], "height": m_box["height"]}, "weight": m_box["max_weight"]}
check("Product dims exactly equal to box dims still fits (boundary case)", fits(product7, m_box) is True)


# ---------------------------------------------------------
# Test 8: Largest product -> should select XXL Box
# ---------------------------------------------------------
product8 = {"shape": "rectangular", "dims": {"length": 75, "width": 55, "height": 55}, "weight": 35}
result8 = select_best_box(product8, boxes)
check("Very large product gets XXL Box", result8 is not None and result8["name"] == "XXL Box")


print(f"\n{passed} passed, {failed} failed out of {passed + failed} tests.")
