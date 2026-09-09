# Amogh Asset Pipeline Toolkit

A Technical Art project built with **Blender + Python**.

The goal of this project is to create a small toolkit that automates repetitive game-asset preparation tasks, from naming and validation to cleanup and engine-ready export.

## 🚀 Project Status

**V0.6 Complete — Full Prototype Finished ✅**

The toolkit currently contains six progressively developed tools covering common asset preparation steps in a basic game-art pipeline.

---

### V0.1 — Asset Renamer ✅

The first prototype of the toolkit.

**What it does:**

* Finds selected Blender objects
* Automatically renames them
* Adds consistent numbering
* Uses Blender's Python API

**Example:**

```text
Cube        → Asset_01
Cube.001    → Asset_02
Cube.002    → Asset_03
```

---

### V0.2 — Polygon Count Checker ✅

The toolkit can inspect selected 3D assets and check their polygon count against a predefined limit.

**What it does:**

* Checks selected mesh objects
* Counts their polygons
* Compares them against a polygon limit
* Flags assets that exceed the limit

**Example:**

```text
Asset_01 → ✓ 6 polygons — GOOD
Asset_02 → ✓ 6 polygons — GOOD
Asset_03 → ⚠ 10,000 polygons — TOO HIGH
```

---

### V0.3 — Material Checker ✅

The toolkit can check whether selected 3D assets have a material assigned.

**What it does:**

* Checks selected mesh objects
* Counts the materials assigned to each asset
* Flags assets with no material
* Helps identify assets that need attention before entering a game pipeline

**Example:**

```text
Asset_01 → ✓ Has material — GOOD
Asset_02 → ✓ Has material — GOOD
Asset_03 → ✓ Has material — GOOD
Asset_04 → ⚠ No material — NEEDS ATTENTION
Asset_05 → ✓ Has material — GOOD
```

---

### V0.4 — Asset Validator ✅

The toolkit can combine multiple validation checks into a single asset validation process.

**What it does:**

* Checks selected mesh objects
* Checks polygon count against a predefined limit
* Checks whether materials are assigned
* Reports whether each asset is ready
* Lists specific issues that need attention

**Example:**

```text
Asset_01 → ✓ READY
Asset_02 → ✓ READY
Asset_03 → ⚠ NEEDS ATTENTION
    → Too many polygons (10000)
Asset_04 → ⚠ NEEDS ATTENTION
    → No material
Asset_05 → ✓ READY
```

---

### V0.5 — Automatic Cleanup ✅

The toolkit can automatically fix common asset preparation issues instead of only reporting them.

**What it does:**

* Removes empty material slots
* Applies object transforms
* Standardizes asset names
* Reports the changes made during cleanup

**Example:**

```text
Chair_Final_FINAL2 → Asset_01
Cube.001          → Asset_02
RandomObject      → Asset_03
```

The cleanup process also applies transforms and removes unused material slots where applicable.

---

### V0.6 — Game Engine Exporter ✅

The toolkit can now export prepared Blender assets into **FBX files** for use in external game-engine workflows.

**What it does:**

* Exports selected assets
* Creates FBX files automatically
* Uses consistent export settings
* Organizes exported assets into an `exports` folder
* Provides a bridge between Blender asset preparation and a game-engine pipeline

**Example:**

```text
Blender Asset
      ↓
Asset Preparation
      ↓
Validation
      ↓
Cleanup
      ↓
FBX Export
      ↓
exports/
├── Asset_01.fbx
├── Asset_02.fbx
└── Asset_03.fbx
```

This completes the first prototype of the toolkit by connecting asset preparation with the final export stage.

---

## 🏁 V1.0 — Complete Asset Pipeline Toolkit

The six V0.x versions form the completed prototype.

The next step toward **V1.0** would be combining these individual tools into a more unified pipeline rather than treating them as separate scripts.

Potential future improvements could include:

* A unified Blender interface
* Configurable validation settings
* Batch processing
* More advanced asset checks
* Improved error handling
* Expanded game-engine export options
* Pipeline automation and usability improvements

---

## 🧰 Technologies

* **Blender 4.5**
* **Python**
* **Blender Python API**
* **FBX**

---

## 🎯 Why I'm Building This

Technical Artists bridge the gap between **art and programming**.

This project is an experiment in using programming to automate repetitive tasks that artists encounter during game development.

Rather than building a single complex system immediately, the toolkit was developed incrementally — starting with simple automation and gradually progressing toward validation, cleanup, and game-engine export.

The project is intended to demonstrate how **Python scripting can turn repetitive artist workflows into a more consistent and automated pipeline.**
