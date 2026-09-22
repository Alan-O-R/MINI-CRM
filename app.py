import json

from model import model_lead
import control 
from random import randint

def add_lead():
    id = randint(100,999)
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Empresa: ")
    stage = input("Estagio de venda: ")

    if not name or not email or "@" not in email:
        print("Nome e/ou e-mail validos são obrigatorios")
        return

    # precisa chamar model para modelar os dados
    # vai printar as informações inseridas
    # print(model_lead(name,company,email,stage))
    
    # depois de modelados...

    # vou precisar chamar control.py para enviar os dados modelados para o banco de dados json
    control.create_lead(model_lead(id, name, company, email, stage ))

def list_leads():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead encontrado")
        return

    print(f"\n {"ID":<5}|{"Nome":<20}|{"Empresa":<20}|{"Email":<10}")
    for i ,lead in enumerate(leads):
        print(f" {lead["id"]:<5}|{lead["name"]:<20}|{lead["company"]:<20}|{lead["email"]:<10}")

def search_leads():
    query = input("Buscar por:").strip().lower()

    if not query:
        print("Consulta vazia")
        return

    #Vamos enviar a busca para o control.py
    # o control.read_leads_busca() vai retornar os leads encontrados
    leads_finded = control.read_leads_busca(query)
    if not leads_finded:
        print("Nada encontrado")
    else:
        print(f"\n {"ID":<5}|{"Nome":<20}|{"Empresa":<20}|{"Email":<10}")
        for i, lead in enumerate(leads_finded):
            print(f" {lead["id"]:<5}|{lead["name"]:<20}|{lead["company"]:<20}|{lead["email"]:<10}")

def export_leads():
    path_csv = control.export_csv()
    print(path_csv)

    if path_csv is None:
        print("Não foi possivel exportar os leads para CSV")
    else: 
        print(f"CSV exportado para {path_csv}")

def delete_lead():
    try:
        id = int(input("Digite o ID do lead que deseja apagar: "))
        if id <= 0:
            print("ID inválido")
            return
        control.delete_lead(id)
    except ValueError:
        print("Informação invalida")
    
def update_lead():
    try:
        id = int(input("Digite o ID do lead que deseja atualizar: "))
        if id <= 0:
            print("ID inválido")
            return
        control.updating(id)
    except ValueError:
        print("Informação invalida")

def  main():
    while True:
        print("\nMini CRM")
        print("[1]- Adicionar lead")
        print("[2]- Listar leads")
        print("[3]- Buscar (nome/e-mail/empresa)")
        print("[4]- Exportar para CSV")
        print("[5]- Apagar lead")
        print("[6]- Mudar informação")
        print("[0]- Sair do programa")

        opt = input("escolha uma opção: ").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "5":
            delete_lead()
        elif opt == "6":
            update_lead()
        elif opt == "0":
            print("Saindo...")
            break
        else:
            print("Opção invalida")

if __name__=="__main__":
    main()