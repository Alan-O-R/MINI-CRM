from pathlib import Path
import json , csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "lead.json"

#CRUD
#CREATE - create_lead()
#READ - read_leads()
#UPDATE
#DELETE

def read_db():
    return DB_PATH.read_text(encoding = "utf-8")

def read_leads():
    if not DB_PATH.exists():
        return[]

    try:
        return json.loads(read_db())
    except json.JSONDecodeError:
        # se corromper, começar vazio
        return[]

def create_lead(lead_dict):
    if not DB_PATH.exists():
        DB_PATH.write_text(json.dumps([lead_dict], ensure_ascii=False, indent=2), encoding= "utf-8")
    else:   
        try:
            removerFinal = open(DB_PATH, "rb+", encoding = "utf-8")
            removerFinal.seek(-1, 2)
            removerFinal.truncate()
            removerFinal.seek(-2, 2)
            removerFinal.truncate()

            adicionarNovo = open(DB_PATH, "a", encoding = "utf-8")
            adicionarNovo.write(f",\n\t{json.dumps(lead_dict, ensure_ascii=False, indent=2)}\n]")
        except Exception as e: 
            ...
    # DB_PATH.write_text(, encoding= "utf-8")

def read_leads_busca(query):
    leads = read_leads()
    results =[]

    for i,lead in enumerate(leads):
       txt_lead = f"{lead["id"]} {lead["name"]} {lead["company"]} {lead["email"]}".lower()

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