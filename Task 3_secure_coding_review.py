# secure_code_review.py

code = """
password = "admin123"
query = "SELECT * FROM users WHERE username='" + user + "'"
"""

issues = []

if "password =" in code:
    issues.append("Hardcoded password found")

if "SELECT * FROM" in code and "+" in code:
    issues.append("Possible SQL Injection vulnerability")

print("Security Review Report")
print("----------------------")

for issue in issues:
    print("-", issue)
