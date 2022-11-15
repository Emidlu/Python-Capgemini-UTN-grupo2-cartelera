import pymysql
#definimos un objetos Base de datos
# class Database():
#     #creamos el constructor con la bbdd elegida a través de pymysql
#     def __init__(self):
#         self.connection = pymysql.connect(
#         host='localhost',
#         user='',
#         password='',
#         db=''
#     )
#     #chequeo que la bbdd este en funcionamiento, sino no se conecta
#     #y lanza un error (no llega al print)
#         self.cursor = self.connection.cursor()
#         print("La conexion fue exitosa")
    
#     #METODOS
#     #METODOS de ejemplo
#     # def all_users (self):
#     #     sql='SELECT * FROM medicos'

#     #     self.cursor.execute(sql)
#     #     users=self.cursor.fetchall()

#     #     for user in users:
#     #         print("Matricula:",user[0] )
#     #         print("Nombre:",user[1] )
#     #         print("Apellido:", user[2])
#     #         print("Telefono:", user[3])

# db= Database()
# db.all_users()
