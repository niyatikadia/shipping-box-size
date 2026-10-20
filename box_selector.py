"""
Box Selection System
---------------------
Takes product details as terminal input and recommends the most
suitable shipping box (closest fit, not oversized, not undersized).

Run with:  python box_selector.py
"""

# -----------------------------
# STEP 1: Box catalog (hardcoded)
# Each box: name, length, width, height (internal, in cm), max_weight (kg), cost
# -----------------------------
BOXES = [
    {"name": "XS Box", "length": 10, "width": 10, "height": 10, "max_weight": 1,  "cost": 10},
    {"name": "S Box",  "length": 20, "width": 15, "height": 10, "max_weight": 3,  "cost": 15},
    {"name": "M Box",  "length": 30, "width": 20, "height": 20, "max_weight": 8,  "cost": 25},
    {"name": "L Box",  "length": 40, "width": 30, "height": 30, "max_weight": 15, "cost": 40},
    {"name": "XL Box", "length": 60, "width": 40, "height": 40, "max_weight": 25, "cost": 60},
    {"name": "XXL Box","length": 80, "width": 60, "height": 60, "max_weight": 40, "cost": 90},
]


# -----------------------------
# STEP 2: Collect product input from the user
# -----------------------------
def get_product_input():
    print("\nEnter product details:")
    shape = input("Shape (rectangular / cube / sphere / cylinder / plate / oval / square / triangle): ").strip().lower()

    dims = {}

    if shape in ("rectangular",):
        dims["length"] = float(input("Length (cm): "))
        dims["width"]  = float(input("Width (cm): "))
        dims["height"] = float(input("Height (cm): "))

    elif shape == "cube":
        side = float(input("Side (cm): "))
        dims["length"] = dims["width"] = dims["height"] = side

    elif shape == "sphere":
        diameter = float(input("Diameter (cm): "))
        dims["length"] = dims["width"] = dims["height"] = diameter

    elif shape == "cylinder":
        diameter = float(input("Diameter (cm): "))
        height = float(input("Height (cm): "))
        dims["length"] = dims["width"] = diameter
        dims["height"] = height

    elif shape == "plate":
        diameter = float(input("Diameter (cm): "))
        thickness = float(input("Thickness (cm): "))
        dims["length"] = dims["width"] = diameter
        dims["height"] = thickness

    elif shape == "oval":
        major = float(input("Major axis / longer length (cm): "))
        minor = float(input("Minor axis / shorter length (cm): "))
        thickness = float(input("Thickness (cm): "))
        dims["length"] = major
        dims["width"] = minor
        dims["height"] = thickness

    elif shape == "square":
        side = float(input("Side (cm): "))
        thickness = float(input("Thickness (cm): "))
        dims["length"] = dims["width"] = side
        dims["height"] = thickness

    elif shape == "triangle":
        base = float(input("Base (cm): "))
        height = float(input("Height (cm): "))
        thickness = float(input("Thickness (cm): "))
        dims["length"] = base
        dims["width"] = height
        dims["height"] = thickness

    else:
        print("Unknown shape entered. Please use one of the listed shapes.")
        return get_product_input()

    weight = float(input("Weight (kg): "))

    return {"shape": shape, "dims": dims, "weight": weight}


# -----------------------------
# STEP 3: Normalize product into 3 bounding dimensions
# -----------------------------
def normalize_product(product):
    d = product["dims"]
    return [d["length"], d["width"], d["height"]]


# -----------------------------
# STEP 4: Check if a product fits a given box
# -----------------------------
def fits(product, box):
    product_dims = sorted(normalize_product(product), reverse=True)
    box_dims = sorted([box["length"], box["width"], box["height"]], reverse=True)

    dimension_ok = all(product_dims[i] <= box_dims[i] for i in range(3))
    weight_ok = product["weight"] <= box["max_weight"]

    return dimension_ok and weight_ok


# -----------------------------
# STEP 5: Select the best (tightest, cheapest) valid box
# -----------------------------
def select_best_box(product, boxes):
    candidates = [b for b in boxes if fits(product, b)]

    if not candidates:
        return None

    def volume(b):
        return b["length"] * b["width"] * b["height"]

    best = min(candidates, key=lambda b: (volume(b), b["cost"]))
    return best


# -----------------------------
# STEP 6: Main program flow
# -----------------------------
def main():
    product = get_product_input()
    best_box = select_best_box(product, BOXES)

    print("\n--- Result ---")
    if best_box is None:
        print("no available box for the product.")
    else:
        print(f"Recommended Box: {best_box['name']}")
        print(f"  Internal Length : {best_box['length']} cm")
        print(f"  Internal Width  : {best_box['width']} cm")
        print(f"  Internal Height : {best_box['height']} cm")
        print(f"  Max Weight Cap  : {best_box['max_weight']} kg")
        print(f"  Cost            : {best_box['cost']}")


# -----------------------------
# STEP 7: Entry point
# -----------------------------
if __name__ == "__main__":
    main()
