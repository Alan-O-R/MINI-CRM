from datetime import date
# Modelo da estructura de dados do lead
#A linha created: date.today().isoformat() vai pegar a data atual e formatar para o padrão (ano-mês-dia)
def model_lead(id,name,company,email,stage):
    return{
        "id": id,
        "name": name,
        "company": company,
        "email": email,
        "stage": stage,
        "created": date.today().isoformat()
    }