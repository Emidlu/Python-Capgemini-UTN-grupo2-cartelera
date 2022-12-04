import cv2
from django.shortcuts import render, redirect
from .models import Database


def contarEspectadores(request):
    db=Database()
    if request.method == "POST": #Si entra por POST
        cantidad_entradas=request.POST.get("cantidad_entradas")
        

        net = cv2.dnn.readNet("cartelera\static\dnn_model\yolov4-tiny.weights", "cartelera\static\dnn_model\yolov4-tiny.cfg")
        model=cv2.dnn_DetectionModel(net)

        model.setInputParams(size=(320,320), scale=1/255)


        captura_video = cv2.VideoCapture(0)

        espectadores = 0

        clase_buffer = ["","","","",""]
        while captura_video.isOpened():
            bol, frame = captura_video.read()

            (id_clase, puntaje, caja) = model.detect(frame)

            id_clase_string = str(id_clase)
            if "0" in id_clase_string and "0" not in clase_buffer[0] and "0" not in clase_buffer[1] and "0" not in clase_buffer[2] and "0" not in clase_buffer[3] and "0" not in clase_buffer[4]:
                print("Entro una persona")
                espectadores += 1


            if int(cantidad_entradas) == 0:
                break
            elif espectadores == int(cantidad_entradas):
                print("Se alcanzo la cantidad de espectadores")
                break

            clase_buffer[4] = str(clase_buffer[3])
            clase_buffer[3] = str(clase_buffer[2])
            clase_buffer[2] = str(clase_buffer[1])
            clase_buffer[1] = str(clase_buffer[0])
            clase_buffer[0] = id_clase_string


            for id_clase, puntaje, caja in zip(id_clase, puntaje, caja):
                (x, y, w, h) = caja 
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)


            if bol:
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        captura_video.release()
        cv2.destroyAllWindows()



        return render(request, "molinete.html", {"cantidad_entradas":cantidad_entradas, "user_id":True, "formClass":"d-none","msg":""})
    