from datetime import date

def model_lead(id,name,company,email,stage):
    return{
        "id": id,
        "name": name,
        "company": company,
        "email": email,
        "stage": stage,
        "created": date.today().isoformat()
    }