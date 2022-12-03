
from os import remove
import math
from operator import contains
import speech_recognition as sr
from pydub import AudioSegment


def nombreArchivo():
    materia = input("¿De qué asignatura era el audio?: ")
    fecha = input("¿Cuando se realizó esa clase? (dd.mm.aaaa): ")
    nombreFinal = f"{materia} - {fecha}"
    print(f"El nombre del archivo final será {nombreFinal}.txt")
    confirmacion = input("¿Estás de acuerdo? S/N: ")
    confirmacion = confirmacion.upper()
    if confirmacion == "S":
        return nombreFinal


def cargarArchivo():
    nombreArchivoBruto = input("Introduce la ruta del archivo de audio: ")
    return nombreArchivoBruto


def transformarAudioEnTexto(rutaArchivo, nombreFinal):
    seg = 50

    speech = AudioSegment.from_wav(rutaArchivo)

    batch_size = seg * 1000
    duracion = speech.duration_seconds
    batches = math.ceil(duracion / seg)

    inicio = 0
    for i in range(batches):
        trozo = speech[inicio: inicio + batch_size]
        trozo.export(f'trozo_{i}.wav', format='wav')
        inicio += batch_size

        r = sr.Recognizer()

        archivo = sr.AudioFile(f"trozo_{i}.wav")
        with archivo as origen:
            audio = r.record(origen)
            texto = r.recognize_google(audio, language='es')
            archivo = open(f"{nombreFinal}.txt", "a")
            archivo.write(str(texto))
            archivo.close()

        remove(f"trozo_{i}.wav")


def crearArchivoTexto(nombreFinal, texto):
    archivo = open(f"{nombreFinal}.txt", "a")
    archivo.write(str(texto))
    archivo.close()


def main():
    rutaArchivo = cargarArchivo()
    nombreFinal = nombreArchivo()
    transformarAudioEnTexto(rutaArchivo, nombreFinal)


if __name__ == "__main__":
    main()
