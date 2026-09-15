from datetime import date

def model_lead(name,company,email,stage):
    return{
        "name": name,
        "company": company,
        "email": email,
        "stage": stage,
        "created": date.today().isoformat()
    }