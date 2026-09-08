# Amogh Asset Pipeline Toolkit

A beginner Technical Art project built with **Blender + Python**.

The goal is to create a small toolkit that automates repetitive game-asset preparation tasks.

## 🚧 Project Status

Currently in development.

### V0.1 — Asset Renamer ✅

The first prototype of the toolkit.

**What it does:**

* Finds selected Blender objects
* Automatically renames them
* Adds consistent numbering
* Uses Blender's Python API

**Example:**

`Cube` → `Asset_01`
`Cube.001` → `Asset_02`
`Cube.002` → `Asset_03`

---

### V0.2 — Polygon Count Checker ✅

The toolkit can now inspect selected 3D assets and check their polygon count against a predefined limit.

**What it does:**

* Checks selected mesh objects
* Counts their polygons
* Compares them against a polygon limit
* Flags assets that exceed the limit

**Example:**

`Asset_01` → ✓ 6 polygons — GOOD
`Asset_02` → ✓ 6 polygons — GOOD
`Asset_03` → ⚠ 10,000 polygons — TOO HIGH

---

### V0.3 — Material Checker ✅

The toolkit can now check whether selected 3D assets have a material assigned.

**What it does:**

* Checks selected mesh objects
* Counts the materials assigned to each asset
* Flags assets with no material
* Helps identify assets that need attention before entering a game pipeline

**Example:**

`Asset_01` → ✓ Has material — GOOD
`Asset_02` → ✓ Has material — GOOD
`Asset_03` → ✓ Has material — GOOD
`Asset_04` → ⚠ No material — NEEDS ATTENTION
`Asset_05` → ✓ Has material — GOOD

---

### Upcoming

* [ ] V0.4 — Asset Validator
* [ ] V0.5 — Automatic Cleanup
* [ ] V0.6 — Game Engine Exporter
* [ ] V1.0 — Complete Asset Pipeline Toolkit


## 🧰 Technologies

* Blender 4.5
* Python
* Blender Python API

## 🎯 Why I'm Building This

Technical Artists bridge the gap between art and programming.

This project is an experiment in using programming to automate repetitive tasks that artists encounter during game development.

