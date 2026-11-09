# Matplotlib Learning

This repository contains my Matplotlib practice as I learn data visualization with Python.

## Topics covered

- Line plots using `plt.plot()`
- Adding axis labels and a title
- Grid lines
- Customizing line color, markers, and line style

## Practice programs

### 1. Weekly study-hours line plot

File: [line_plot_study_hours.py](line_plot_study_hours.py)

**What it shows:** Study hours recorded across Monday to Sunday.

**Data used:**
- Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
- Study hours: 2, 3, 4, 1, 6, 7, 8

**Output:**
A line chart with a yellow dashed line and circular markers. The x-axis shows the days of the week, the y-axis shows study hours, and the chart includes the title "Study Analysis" and grid lines.

**Observation:** Sunday has the highest study time (8 hours), while Thursday has the lowest (1 hour).

## How to run

Install Matplotlib if needed:

```bash
pip install matplotlib
```

Run the program:

```bash
python line_plot_study_hours.py
```
