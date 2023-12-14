from modules.oracleDatabase import OracleDatabase
import os, csv

class PessoaBusiness:

    def importAndSavePessoa(self):

        # Boa pratica usar "with" para o objeto ser liberado do contexto independente do que ocorrer
        with OracleDatabase().open_connection() as connection:
            with connection.cursor() as cursor:
                try:
                    with open(os.getenv("input_file_csv"), mode='r', newline='') as file:
                        
                        reader = csv.reader(file)
                        # Pulando a primeira linha
                        next(reader)
                        
                        query = f"INSERT INTO PESSOA (ID_ARQUIVO, CNPJ_CPFUSUFINALRECBDR_TITLAR, CNPJCREDDRSUB, CNPJFINCDR, CODINSTITDRARRAJPGTO, DTOPTIN, DTINIOPTIN) VALUES (:1, :2, :3, :4, :5, to_date(:6, 'yyyy-mm-dd'), to_date(:7, 'yyyy-mm-dd'))"

                        with connection.cursor() as cursor:
                            for numero, linha in enumerate(reader):
                                dado = linha[0].split(";")
                                dados = (dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6])
                                cursor.execute(query, dados)

                                print(f'Linha {numero}: {linha}')

                            connection.commit()

                except Exception as e:
                    # Em caso de exceção, você pode lidar com o erro aqui
                    print(f"Erro: { str(e) }")
                    connection.rollback()

        