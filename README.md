# Smart Expense Tracker with Insights

## Description
This project is a Python-based Smart Expense Tracker that allows users to record, categorize, and analyze their daily expenses. It provides monthly summaries, category-wise analysis, and visual insights using charts. The system stores all expense data in a JSON file for persistence.

## Features
- Add daily expenses with date, category, amount, and description
- Store data using JSON file
- Generate monthly expense summary
- Category-wise expense breakdown
- Identify highest spending category
- Visualize expenses using pie chart (matplotlib)
- Simple CLI-based interaction

## Project Structure
python_use_case/<br>
│<br>
├── main.py → User interface (CLI)<br>
├── expense.py → Expense class definition<br>
├── storage.py → Load and save JSON data<br>
├── analysis.py → Expense analysis and insights<br>
└── data.json → Stores expense records<br>

## Data Description
data.json → Contains all user expense entries
Each record includes date, category, amount, and description

## Summary Chart
<img width="1122" height="936" alt="image" src="https://github.com/user-attachments/assets/a63e983c-726d-439f-a777-1900b6d5e9a9" />

## Technologies Used
Python
JSON
Matplotlib
File Handling
Collections (defaultdict)
