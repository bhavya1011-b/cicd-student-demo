from student_result import calculate_result

# Sample student data
students = [
    {"name": "Alice", "mark": 85},
    {"name": "Bob", "mark": 35},
    {"name": "Charlie", "mark": 65},
    {"name": "David", "mark": 40},
]

# Generate HTML Content
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Student Results - CD Pipeline</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 50%; margin-top: 20px; background: white; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #007bff; color: white; }
        .Pass { color: green; font-weight: bold; }
        .Fail { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Student Results Summary</h1>
    <table>
        <tr>
            <th>Student Name</th>
            <th>Mark</th>
            <th>Result</th>
        </tr>
"""

for student in students:
    result = calculate_result(student["mark"])
    html_content += f"""
        <tr>
            <td>{student['name']}</td>
            <td>{student['mark']}</td>
            <td class="{result}">{result}</td>
        </tr>
"""

html_content += """
    </table>
</body>
</html>
"""

# Save to public directory
import os
os.makedirs("public", exist_ok=True)
with open("public/index.html", "w") as f:
    f.write(html_content)

print("Website successfully generated in public/index.html")
