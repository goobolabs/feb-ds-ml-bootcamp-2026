import os
import re
import csv
from datetime import datetime

def get_last_modified(path):
    if not os.path.exists(path):
        return None
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')

def track_assignments(base_dir):
    submissions_dir = os.path.join(base_dir, "submissions")
    if not os.path.exists(submissions_dir):
        print(f"Error: Submissions directory not found at {submissions_dir}")
        return

    # Configuration for assignments and projects
    assignment_configs = [
        {"id": "A1", "regex": re.compile(r"(a1|research|lesson[-_ ]*one)|(assig[n]*m[er]*nt|asig[n]*ment)([-_ ]*(1|one))?$", re.IGNORECASE)},
        {"id": "A2", "regex": re.compile(r"(a2|project|lesson[-_ ]*two)|(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(2|two)", re.IGNORECASE)},
        {"id": "A3", "regex": re.compile(r"(a3|lesson[-_ ]*three)|(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(3|three)", re.IGNORECASE)},
        {"id": "A4", "regex": re.compile(r"(a4|lesson[-_ ]*four)|(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(4|four)", re.IGNORECASE)},
        {"id": "A5", "regex": re.compile(r"(a5|lesson[-_ ]*five)|(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(5|five)", re.IGNORECASE)},
        {"id": "A6", "regex": re.compile(r"(a6|lesson[-_ ]*six)|(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(6|six)", re.IGNORECASE)},
        {"id": "Final", "regex": re.compile(r"(final[-_ ]*project|capstone|final[-_ ]*assignment)", re.IGNORECASE)},
    ]

    students = {}
    exclude_folders = {"000.example", ".git", "assignment-1", "assignment-2", "assignment-3"}

    # Get all possible students (all folders in submissions excluding noise)
    all_folders = [f for f in os.listdir(submissions_dir) if os.path.isdir(os.path.join(submissions_dir, f)) and f.lower() not in exclude_folders]

    for student_name in all_folders:
        item_path = os.path.join(submissions_dir, student_name)
        
        students[student_name] = {cfg["id"]: {"status": False, "evidence": "", "date": "N/A"} for cfg in assignment_configs}
        
        for root, dirs, files in os.walk(item_path):
            depth = root[len(item_path):].count(os.sep)
            if depth > 2:
                continue
            
            # Check directory names and filenames
            items_to_check = [(d, os.path.join(root, d)) for d in dirs] + [(f, os.path.join(root, f)) for f in files]
            
            for name, path in items_to_check:
                cleanup_name = name.lower()
                if "readme" in cleanup_name or cleanup_name.startswith("."):
                    continue
                
                for cfg in assignment_configs:
                    if cfg["regex"].search(cleanup_name):
                        if not students[student_name][cfg["id"]]["status"]:
                            students[student_name][cfg["id"]] = {
                                "status": True, 
                                "evidence": name, 
                                "date": get_last_modified(path)
                            }
    
    generate_reports(base_dir, students, assignment_configs)

def generate_reports(base_dir, students, assignment_configs):
    # Valid students have at least one submission
    valid_students = {k: v for k, v in students.items() if any(a["status"] for a in v.values())}
    # Missing students have zero submissions
    missing_students = {k: v for k, v in students.items() if not any(a["status"] for a in v.values())}
    
    total_valid = len(valid_students)
    ids = [cfg["id"] for cfg in assignment_configs]
    
    stats = {id: sum(1 for s in valid_students.values() if s[id]["status"]) for id in ids}
    
    # 1. Generate Markdown Report
    md_path = os.path.join(base_dir, "TRACKER.md")
    with open(md_path, "w") as f:
        f.write("# Student Assignment Tracker Report\n\n")
        f.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Overview\n")
        f.write(f"- **Total Students Found:** {len(students)}\n")
        f.write(f"- **Students with Submissions:** {total_valid} ({total_valid/len(students)*100:.1f}%)\n")
        f.write(f"- **Students with Zero Submissions:** {len(missing_students)}\n\n")
        
        f.write("### Assignment Statistics\n")
        f.write("| Assignment | Submissions | Percentage |\n")
        f.write("| --- | --- | --- |\n")
        for id in ids:
            perc = (stats[id] / total_valid * 100) if total_valid > 0 else 0
            f.write(f"| {id} | {stats[id]} | {perc:.1f}% |\n")
        f.write("\n")
        
        f.write("## Detailed Submission List\n\n")
        header = "| Student Name | " + " | ".join(ids) + " |\n"
        separator = "| --- | " + " | ".join(["---"] * len(ids)) + " |\n"
        f.write(header)
        f.write(separator)
        
        for student in sorted(valid_students.keys()):
            s = valid_students[student]
            row = f"| {student} | "
            statuses = []
            for id in ids:
                if s[id]["status"]:
                    statuses.append(f"✅")
                else:
                    statuses.append("❌")
            row += " | ".join(statuses) + " |\n"
            f.write(row)
            
        if missing_students:
            f.write("\n## Students with zero submissions\n\n")
            for student in sorted(missing_students.keys()):
                f.write(f"- {student}\n")

    # 2. Generate CSV Report
    csv_path = os.path.join(base_dir, "TRACKER.csv")
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        csv_header = ["Student Name"]
        for id in ids:
            csv_header.extend([f"{id} Status", f"{id} Evidence", f"{id} Date"])
        writer.writerow(csv_header)
        
        for student in sorted(students.keys()):
            s = students[student]
            row = [student]
            for id in ids:
                status = "Submitted" if s[id]["status"] else "Missing"
                row.extend([status, s[id]["evidence"], s[id]["date"]])
            writer.writerow(row)
            
    print(f"Reports generated: {md_path} and {csv_path}")

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    track_assignments(current_dir)
