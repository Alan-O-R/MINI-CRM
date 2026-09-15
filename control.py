from pathlib import Path
import json , csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "lead.jason"

#CRUD
#CREATE - create_lead()
#READ - read_leads()
#UPDATE
#DELETE

def read_leads():
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(DB_PATH.read_text(encoding = "utf-8"))
    except json.JSONDecodeError:
        # se corromper, começar vazio
        return[]

def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding= "utf-8")

def read_leads_busca(query):
    leads = read_leads()
    results =[]

    for i,lead in enumerate(leads):
       txt_lead = f"{lead["name"]} {lead["company"]} {lead["email"]}".lower()

       if query in txt_lead:
           results.append(lead)
    if not results:
        print("Nada encontrado")
        return []
    else:
        return results

def export_csv():
    # vai exportar os leads para um csv
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w",newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None