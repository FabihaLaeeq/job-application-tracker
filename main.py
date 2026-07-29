import csv

applications = []

try:
    with open("applications.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            applications.append(row)
except FileNotFoundError:
    print("No previous applications found.")

def add_application(company, role, status, date_applied):
    application = {
        "company": company,
        "role": role,
        "status": status,
        "date_applied": date_applied
    }
    applications.append(application)

def filter_by_status(status):
    return [app for app in applications if app["status"] == status]

def save_to_csv():
    with open("applications.csv", "w", newline="") as file:
        fieldnames = ["company", "role", "status", "date_applied"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(applications)

def print_summary():
    print("\nJob Applications:\n")
    for app in applications:
        print(
            f"Company: {app['company']} | "
            f"Role: {app['role']} | "
            f"Status: {app['status']} | "
            f"Applied: {app['date_applied']}"
        )

add_application("Google", "Data Analyst", "Applied", "2026-07-29")
add_application("Microsoft", "Data Scientist", "Interview", "2026-07-30")
add_application("Amazon", "BI Analyst", "Rejected", "2026-07-20")

print_summary()

print("\nApplications with status 'Applied':")
for app in filter_by_status("Applied"):
    print(app)

save_to_csv()
