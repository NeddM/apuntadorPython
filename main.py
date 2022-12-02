import os
import pyaudio
import speech_recognition as sr


def nombreArchivo():
    # de qué clase que era el audio
    materia = input("¿De qué asignatura era el audio?: ")

    # fecha de la clase
    fecha = input("¿Cuando se realizó esa clase? (dd.mm.aaaa): ")

    # mostrar nombre final del archivo
    nombreFinal = f"{materia} - {fecha}"
    print(f"El nombre del archivo final será {nombreFinal}.txt")
    confirmacion = input("¿Estás de acuerdo? S/N: ")
    confirmacion = confirmacion.upper()
    if confirmacion == "S":
        return nombreFinal


def cargarArchivo():
    nombreArchivoBruto = input("Introduce la ruta del archivo de audio: ")
    return nombreArchivoBruto


def transformarAudioEnTexto(rutaArchivo):
    r = sr.Recognizer()

    archivo = sr.AudioFile(rutaArchivo)
    with archivo as origen:
        audio = r.record(origen)
        texto = r.recognize_google(audio, language='es')
        return texto


def crearArchivoTexto(nombreFinal, texto):
    print(nombreFinal)
    archivo = open(f"{nombreFinal}.txt", "w")
    archivo.write(str(texto))
    archivo.close()


def main():
    rutaArchivo = cargarArchivo()
    nombreFinal = nombreArchivo()
    texto = transformarAudioEnTexto(rutaArchivo)
    crearArchivoTexto(nombreFinal, texto)


if __name__ == "__main__":
    main()