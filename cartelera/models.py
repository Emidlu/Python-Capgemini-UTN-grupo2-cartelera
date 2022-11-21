import pymysql
# definimos un objetos Base de datos
class Database():
    #creamos el constructor con la bbdd elegida a través de pymysql
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='cartelera'
    )
    #chequeo que la bbdd este en funcionamiento, sino no se conecta
    #y lanza un error (no llega al print)
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa")
    
    #METODOS
    def all_genres (self):
        sql='SELECT * FROM generos'

        self.cursor.execute(sql)
        generos=self.cursor.fetchall()

        diccionarioGeneros = dict(generos)
        # for genero in generos:
        #     print("id:",genero[0] )
        #     print("Nombre:",genero[1] )

        return diccionarioGeneros

    def insert_movie(self, titulo, duracion, calificacion, imagenLink, idioma, genero, resenia):
        # print(titulo, duracion, calificacion, imagenLink, idioma, genero, resenia)
        sql = "INSERT INTO peliculas (titulo, duracion, calificacion, imagen_link, idioma, generos_id_generos, resenia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (titulo, duracion, calificacion, imagenLink, idioma, genero, resenia))
        self.connection.commit()
        print("Se inserto la pelicula")


db= Database()
db.all_genres()
