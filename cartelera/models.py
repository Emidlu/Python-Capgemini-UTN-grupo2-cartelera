import pymysql
from datetime import date, time, datetime, timedelta
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

    def movie_by_id(self, movie_id):
        sql = "SELECT * FROM peliculas WHERE id_peliculas = %s"
        self.cursor.execute(sql, (movie_id))
        movie = self.cursor.fetchone()
        return movie

    def delete_movie (self, movie_id):
        sql = "DELETE FROM peliculas WHERE id_peliculas = %s ;"
        self.cursor.execute(sql,(movie_id))
        self.connection.commit()
        print("Se elimino la entrada")

    def update_movie (self, id_peliculas, titulo, resenia, duracion, calificacion, idioma, generos_id_generos, imagen_link, fecha_estreno):
        sql = "UPDATE peliculas SET titulo = %s, resenia = %s, duracion = %s, calificacion = %s, idioma = %s, generos_id_generos = %s, imagen_link = %s, fecha_estreno = %s WHERE id_peliculas = %s ;"
        self.cursor.execute(sql, (titulo, resenia, duracion, calificacion, idioma, generos_id_generos, imagen_link, fecha_estreno, id_peliculas))
        self.connection.commit()
        print("Se edito la pelicula")

    def movie_show_by_id(self, movie_id, dateTime):
        sql = "SELECT * FROM cartelera.peliculas INNER JOIN funcion ON funcion.peliculas_id_peliculas = peliculas.id_peliculas WHERE id_peliculas = %s AND funcion.horario > %s;"
        self.cursor.execute(sql, (movie_id, dateTime))
        movie = self.cursor.fetchall()
        return movie

    def entradas_by_show_id(self, show_id):
        sql = "SELECT * FROM cartelera.entrada INNER JOIN funcion ON funcion.id_funcion = entrada.funcion_id_funcion INNER JOIN asientos ON entrada.asiento_id_asiento = asientos.id_asiento WHERE funcion.id_funcion = %s;"
        self.cursor.execute(sql, (show_id))
        entradas = self.cursor.fetchall()
        return entradas

    # def asiento_numero_salas(self, numero_asiento, sala):
    #     sql = "SELECT * FROM cartelera.asientosINNER JOIN sala ON sala.id_sala=asientos.id_sala WHERE asientos.numero_asiento = %s AND sala.id_sala = %s;"
    #     self.cursor.execute(sql, (numero_asiento, sala))
    #     asiento = self.cursor.fetchone()
    #     return asiento

    def show_by_id(self, show_id):
        sql = "SELECT * FROM funcion WHERE id_funcion = %s"
        self.cursor.execute(sql, (show_id))
        funcion = self.cursor.fetchone()
        return funcion

    def crearEntrada(self, funcion_id, usuario_id, asiento_id, precio):
        sql = "INSERT INTO entrada (`funcion_id_funcion`, `usuarios_id_usuarios`, `asiento_id_asiento`, `precio`) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (funcion_id, usuario_id, asiento_id, precio))
        self.connection.commit()
        print("Se inserto la entrada")


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


    def cartelera(self, dateTime):
        date=datetime.strftime(dateTime, '%Y-%m-%d')

        sql = "SELECT * FROM peliculas  INNER JOIN funcion ON funcion.peliculas_id_peliculas=peliculas.id_peliculas WHERE peliculas.fecha_estreno <= %s AND funcion.horario >= %s"
        self.cursor.execute(sql, (date, dateTime))
        funciones = self.cursor.fetchall()
        return funciones

    def estrenos(self, dateTime):
        date=datetime.strftime(dateTime, '%Y-%m-%d')

        sql = "SELECT * FROM peliculas  INNER JOIN funcion ON funcion.peliculas_id_peliculas=peliculas.id_peliculas WHERE peliculas.fecha_estreno >= %s"
        self.cursor.execute(sql, (date))
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
