
from .models import Database
from datetime import date, time, datetime, timedelta



def chequeoDeFuncionesFechaHora(funcion, fecha, horario):
    funcionFechaHora = funcion(fecha, horario)
    if funcionFechaHora:
        return True
    else:
        return False

def funcionPorDia(fecha):
    db=Database()
    matrizDia = [[False,False ,False],[False,False ,False],[False,False ,False]]
    date=datetime.strftime(fecha, '%Y-%m-%d')
    horarios=['10:00:00', '14:00:00', '21:00:00']
    for i in range(3):
        if chequeoDeFuncionesFechaHora(db.search_show_by_date_and_hour, date, horarios[i]):
            funcionesPorHorario = db.search_show_by_date_and_hour(date, horarios[i])
            for funcion in funcionesPorHorario:
                if funcion[2] == 1:
                    matrizDia[0][i] = True
                elif funcion[2] == 2:
                    matrizDia[1][i] = True
                elif funcion[2] == 3:
                    matrizDia[2][i] = True
        else:
            pass
    return matrizDia
    
def matriz_shows_semana(date):
    db=Database()

    matrizSemana = []
    for i in range(7):
        fecha = date + timedelta(days=i)
        fechaString=datetime.strftime(fecha, '%Y-%m-%d')
        if len(db.search_show_by_date(fechaString)) > 0:
            matrizSemana.append(funcionPorDia(fecha))
        else:
            matrizSemana.append([[False,False ,False],[False,False ,False],[False,False ,False]])
            pass


    return matrizSemana


def primerLunesAnterior(fecha):
    while fecha.weekday() != 0:
        fecha = fecha - timedelta(days=1)
    return fecha



def proximosDias(primerDia, cantidadDias):
    dias = []
    for i in range(cantidadDias):
        diaAGuardar = primerDia + timedelta(days=i)
        dias.append(int(diaAGuardar.strftime("%d")))
    return dias



