# minor-2-
Convert any image into ASCII Art using Python. A fun project that transforms images into text-based artwork.
# ASCII Face Generator – Greta Thunberg (Python Project)

This project generates a detailed ASCII-style human face using Python.  
It has been developed as part of the AI/ML Minor Project at **Rungta College of Engineering & Technology**.

The program prints an ASCII art representation inspired by **Greta Thunberg**, the globally renowned young climate activist.  
The entire artwork is generated only through Python code — using loops, conditions, and logical character placement.

---
Greta Thunberg is one of the most influential youth leaders in the world.  
She inspires millions by raising awareness about climate change, sustainability, and environmental protection.  
Creating her ASCII face symbolizes:
- Strength and determination
- Youth leadership
- Courage to speak the truth
- Hope for a better planet

---

##  Project Purpose
The primary objective of this project is to:
- Strengthen Python programming fundamentals  
- Improve logical thinking and structured problem-solving  
- Practice coordinate mapping (row-column logic)  
- Creatively use characters like `*`, `#`, `%`, `+`, `-`, `=`, `:` and `@` to form an ASCII face  
- Represent a real personality through coding instead of graphical tools

This is a programming + creativity + patience-based project.

---

##  How ASCII Art Works
ASCII Art means creating visual designs using **characters instead of images**.  
Where normal images use pixels, ASCII art uses carefully placed characters.

In this project:
- **Rows** = Vertical positioning  
- **Columns** = Horizontal positioning  
- **Characters** = Shape, shading, and structure of the face  

By controlling which character prints at which coordinate, a face is formed.

---

##  Python Concepts Used
This project is built completely using core Python, including:

- `for` loops  
- Nested loops  
- Conditional statements (`if – elif – else`)  
- Coordinate-based logic  
- Character printing  
- Structured program design  

These concepts decide **what to print, where to print, and why to print**.

---

##  How the Code Works

### 1️ Grid Setup
A fixed 2D grid structure is created:
```python
height = 33
width = 45

 2 . Nested Loops

Two loops are used:

Outer loop → Travels through rows

Inner loop → Travels through columns

So every (row, column) position is checked.


3 . Default Character

Initially, every position is blank " " and later replaced with appropriate characters wherever needed.

4️ Conditional Logic for Structure

For each row, logical conditions are used

if row == 0:
   # print top structure

if row == 1:
   # next row details

.
.
if row == 32:
   # bottom structure


Inside every row, columns are checked using:

Exact column values

Column ranges

Multiple character conditions

Characters like: *  #  %  +  -  =  :  @

Challenges Faced

While building this project, I faced challenges like:

Maintaining exact alignment

Handling many conditions without confusion

Understanding coordinates properly

This project helped me gain:

Stronger understanding of loops

Better control over conditional logic

Coordinate-based thinking ability


