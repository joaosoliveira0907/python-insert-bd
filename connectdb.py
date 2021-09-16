import mysql.connector
from credentials import usr, pswd

def insert_db(value1):
    try:  
        mydb = mysql.connector.connect(
            host = "localhost",
            user = usr,
            password = pswd,
            database = "safelog_analytics"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor()

            sql_query = f"INSERT INTO analytics(cpu_percent, ram, disco, data_medicao) VALUES ({value1[0]}, {value1[1]}, {value1[2]}, now())"
            val = [value1]
            print(val, value1)
            mycursor.execute(sql_query)

            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")