# CSCI220: Publishing ESNU Grades to Canvas

*(Originally authored by Joey Lovato Fall 2022)*

This repo contains Python scripts to publish module-based exam grades to Canvas using the ESNU scale for CSCI220 (CS@Mines) Fall 2022. These scripts were also used to publish the final letter grades to canvas

You will need the CanvasAPI for Python: https://canvasapi.readthedocs.io/en/stable/getting-started.html

## Files

- `exam.py` declaration of the `exam` class
- `student.py` declaration of the `student` class
- `main.py` shows an example with CanvasAPI 

## CSV formatting

The expected **grades csv** should be formatted with first name, last name, module scores, and the final score. For example:

`midterm.csv`:
```
first_name,last_name,module-0,module-1,module-2,final
John,Smith,2,3,1,3
Emily,Fields,3,2,3,3
```
These fields can appear in any order. When constructing an `exam` object, you will specify the column names.

The csv expects the ESNU scores as integers where E=3, S=2, N=1, U=0. 

The expected **roster csv** must be strictly formatted with last name, first name, and canvas ID, in that order, with no headers. For example:

`roster.csv`

```
Apadoca,Jesse,42432
Bernard,Robert,34360
Brunvik,Keenan,53487
```
The roster provides a xref of students to their canvas IDs

## Initialize 
Example: 

```
csci220final = exam("roster.csv", "first_name", "last_name", "final", "module-0", "module-1", "module-2")
csci220final.add_scores("midterm.csv")
```

See `main.py` for further example

## Publishing final grades

These scripts can also be used to publish final grades (component grades and letter grades). In Fall 2022, we calculated the final component grades and final letter grade with [esnu-calc](https://github.com/JosephLovato/esnu-calc.git), then uploaded to excel. In excel, the instructors collaborated to adjust the scheme slightly and change a few grades (some F->D, some D->C). Then, the final component grades and letter grades were exported to csv in the same format as the example (`midterm.csv`). The only difference is that the modules were given in ESNU, not 3210; therefore, line 32 in `student.py` was commented out so that the scores were not converted from num to char as they usually are for exam grades.

