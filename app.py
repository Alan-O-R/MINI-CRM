from model import model_lead
import control 

def add_lead():
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
    control.create_lead(model_lead(name, company, email, stage ))

def list_leads():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead encontrado")
        return

    print("\n #| Nome                | Empresa             | Email")
    for i ,lead in enumerate(leads):
        print(f"{i:2d}| {lead["name"]:<20}| {lead["company"]:<20}| {lead["email"]:<20}")

def search_leads():
    query = input("Buscar por:").strip().lower()

    if not query:
        print("Consulta vazia")
        return

    #Vamos enviar a busca para o control.py
    # o control.read_leads_busca() vai retornar os leads encontrados
    leads_finded = control.read_leads_busca(query)
    # if not i in control.read_leads_busca(query):
    #     print("aaaa") 
    # else:
    print(f"\n #| {"Nome":<10}| {"Empresa":<10}| {"Email":<10}")
    for i ,lead in enumerate(leads_finded):
        print(f"{i:2d}| {lead["name"]:<10}| {lead["company"]:<10}| {lead["email"]:<10}")

    

def export_leads():
    path_csv = control.export_csv()
    print(path_csv)

    if path_csv is None:
        print("Não foi possivel exportar os leads para CSV")
    else: 
        print(f"CSV exportado para {path_csv}")


def  main():
    while True:
        print("\nMini CRM - 1 - (Adicionar/listar)")
        print("[1]- Adicionar lead")
        print("[2]- Listar leads")
        print("[3]- Buscar (nome/e-mail/empresa)")
        print("[4]- Exportar para CSV")
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
        elif opt == "0":
            print("Saindo...")
            break
        else:
            print("Opção invalida")




if __name__=="__main__":
    main()