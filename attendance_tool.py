# attendance_tool.py
import os, csv, math

HERE = os.path.dirname(__file__)
CSV_PATH = os.path.join(HERE, "attendance.csv")
REQUIRED_PERCENT = 75.0

def read_attendance():
    rows = []
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "subject": r["Subject"].strip(),
                "total": int(r["Total_Classes"]),
                "attended": int(r["Attended_Classes"])
            })
    return rows

def safe_bunks(attended, total, required_percent=REQUIRED_PERCENT):
    R = required_percent / 100.0
    # safe_bunks = floor(A / R - T)
    val = math.floor(attended / R - total)
    return max(0, int(val))

def project_if_bunk(attended, total, bunk_days):
    new_total = total + bunk_days  # classes held increases
    new_attended = attended        # if you bunk you don't increase attended
    if new_total == 0:
        return 0.0
    return (new_attended / new_total) * 100.0

def build_report(subject_filter=None, bunk_days=1):
    data = read_attendance()
    lines = []
    for r in data:
        subj = r["subject"]
        if subject_filter and subject_filter.lower() not in subj.lower():
            continue
        total = r["total"]
        attended = r["attended"]
        pct = (attended / total) * 100.0
        sb = safe_bunks(attended, total)
        proj = project_if_bunk(attended, total, bunk_days)
        lines.append({
            "subject": subj,
            "total": total,
            "attended": attended,
            "percentage": round(pct,2),
            "safe_bunks_left": sb,
            "if_bunk_{}d_pct".format(bunk_days): round(proj,2)
        })
    return lines

if __name__ == "__main__":
    # quick CLI test
    import sys
    subj = sys.argv[1] if len(sys.argv) > 1 else ""
    bunk = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    out = build_report(subject_filter=subj if subj else None, bunk_days=bunk)
    import json
    print(json.dumps(out, indent=2))
