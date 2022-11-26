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

    def insert_movie(self, titulo, duracion, calificacion, imagenLink, idioma, genero, resenia, fechaEstreno):
        # print(titulo, duracion, calificacion, imagenLink, idioma, genero, resenia)
        sql = "INSERT INTO peliculas (titulo, duracion, calificacion, imagen_link, idioma, generos_id_generos, resenia, fecha_estreno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (titulo, duracion, calificacion, imagenLink, idioma, genero, resenia, fechaEstreno))
        self.connection.commit()
        print("Se inserto la pelicula")

    def all_movies(self):
        sql = "SELECT id_peliculas, titulo FROM peliculas"
        self.cursor.execute(sql)
        peliculas = self.cursor.fetchall()
        peliculasDiccionario = dict(peliculas)
        return peliculasDiccionario

    def all_rooms(self):
        sql = "SELECT * FROM sala"
        self.cursor.execute(sql)
        salas = self.cursor.fetchall()
        salasDiccionario = dict(salas)
        return salasDiccionario

    def insert_show(self, peliculaId, sala, fechaHora):
        sql = "INSERT INTO funcion (peliculas_id_peliculas, sala_id_sala, horario) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (peliculaId, sala, fechaHora))
        self.connection.commit()
        print("Se inserto la funcion")

    def search_show(self, sala, fechaHora):
        sql = "SELECT * FROM funcion WHERE sala_id_sala = %s AND horario = %s"
        self.cursor.execute(sql, (sala, fechaHora))
        funcion = self.cursor.fetchone()
        return funcion

    def search_show_by_date(self, fecha):
        horario1 = fecha +' 00:00:00'
        horario2 = fecha +' 23:59:00'

        sql = "SELECT * FROM funcion WHERE horario BETWEEN %s AND %s"
        self.cursor.execute(sql, (horario1, horario2))
        funciones = self.cursor.fetchall()
        return funciones

    def search_show_by_date_and_hour(self, fecha, hora):
        horario1 = fecha +' '+ hora

        sql = "SELECT * FROM funcion WHERE horario LIKE %s"
        self.cursor.execute(sql, (horario1))
        funciones = self.cursor.fetchall()
        return funciones

############## USUARIOS
    def login(self, email, password):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        self.cursor.execute(sql, (email, password))
        usuario = self.cursor.fetchone()
        return usuario


    def isAdmin(self, user_id):
        sql = "SELECT * FROM usuarios WHERE id_usuarios = %s"
        self.cursor.execute(sql, (user_id))
        usuario = self.cursor.fetchone()
        if usuario[5] == 1:
            return True
        else:
            return False

    def insert_user(self, usuario, fecha_nacimiento, email, password):
        sql = "INSERT INTO usuarios (usuario, fecha_nacimiento, email, password, admin) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (usuario, fecha_nacimiento, email, password, 0))
        self.connection.commit()
        print("Se inserto el usuario")



db= Database()
db.all_genres()
