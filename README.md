# Matplotlib Learning

This repository contains my Matplotlib practice as I learn data visualization with Python.

## Topics covered

- Line plots using `plt.plot()`
- Bar charts using `plt.bar()` and `plt.barh()`
- Adding axis labels, titles, and grid lines
- Customizing line color, markers, line style, bar color, and bar width

## Practice programs

### 1. Weekly study-hours line plot

File: [line_plot_study_hours.py](line_plot_study_hours.py)

**What it shows:** Study hours recorded across Monday to Sunday.

**Data:** Monday to Sunday; study hours are 2, 3, 4, 1, 6, 7, and 8.

**Output:** A yellow dashed line with circular markers. Sunday has the highest study time (8 hours), while Thursday has the lowest (1 hour).

### 2. Vertical product sales bar chart

File: [vertical_bar_chart.py](vertical_bar_chart.py)

**What it shows:** Sales comparison across laptop, mobile, tablet, headphones, and keyboard.

**Output:** Five pink vertical bars. Mobile is highest at 80, and tablet is lowest at 30. The x-axis displays product names and the y-axis displays sales.

### 3. Horizontal product sales bar chart

File: [horizontal_bar_chart.py](horizontal_bar_chart.py)

**What it shows:** The same product sales data displayed horizontally using `plt.barh()`.

**Output:** Five pink horizontal bars. Product names appear on the y-axis and sales values on the x-axis. Mobile is highest at 80, and tablet is lowest at 30.

## How to run

Install Matplotlib if needed:

```bash
pip install matplotlib
```

Run any program, for example:

```bash
python vertical_bar_chart.py
python horizontal_bar_chart.py
```

### 4. Student marks histogram

File: [student_marks_histogram.py](student_marks_histogram.py)

**What it shows:** The distribution of marks for 20 students, grouped into 5 numerical intervals (bins).

**Output:** A pink histogram with black edges. The x-axis shows student marks and the y-axis shows how many marks fall within each interval (frequency). The bars touch because the intervals are adjacent parts of a continuous numerical range.

**Concept learned:** Increasing the number of bins creates more, narrower intervals and gives a more detailed view of the distribution. It does not mean every interval contains the same number of students.

### 5. Study hours vs exam marks scatter plot

File: [study_hours_vs_marks_scatter.py](study_hours_vs_marks_scatter.py)

**What it shows:** The relationship between students' study hours and exam marks.

**Output:** Eight blue circular points. The points generally move upward as study hours increase, showing a positive correlation in this example.

**Concept learned:** Use `plt.scatter(x, y)` to plot the relationship between two numerical variables. The `marker` parameter changes the point shape, `s` controls point size, and `alpha` controls transparency.

### 6. Weekly study time pie chart

File: [weekly_study_time_pie_chart.py](weekly_study_time_pie_chart.py)

**What it shows:** How weekly study time is divided across Python, Maths, Java, DBMS, and English.

**Output:** A pie chart with percentage labels and different slice colors. Python is highlighted using `explode`. Python accounts for 10 of the 24 total study hours (about 41.7%).

**Concept learned:** Use `plt.pie()` for category proportions that make up a whole. The `autopct` parameter displays percentages, `colors` sets slice colors, `explode` separates selected slices, and `startangle` rotates the chart.

### 7. Comparing charts with subplots

File: [subplots_comparison.py](subplots_comparison.py)

**What it shows:** Three charts in one figure using the same subject data: a line plot for study hours, a bar chart for marks, and a pie chart for the share of study time.

**Output:** The charts appear side by side in a 1-row, 3-column layout. Axis labels make the line and bar charts easier to read, and `plt.tight_layout()` helps prevent titles and labels from overlapping.

**Concept learned:** Use `plt.subplot(rows, columns, position)` to choose a chart area in a figure. The position is counted from left to right, then top to bottom. All subplots in the same figure should use a consistent grid layout.


### 8. Customized weekly study-hours chart

File: [weekly_study_analysis_customized.py](weekly_study_analysis_customized.py)

**What it shows:** Daily study hours from Monday to Sunday, with the highest value highlighted.

**Output:** A blue line chart with circular markers, an 8 × 5 inch figure, dashed grid lines, and an annotation marking Saturday's 7 study hours.

**Concept learned:** Customize a figure with `figsize`, set line color and markers, style grid lines, and use `plt.annotate()` to call attention to an important data point.
