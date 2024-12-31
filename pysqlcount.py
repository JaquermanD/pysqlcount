import re
import argparse
import os

def contar_instrucciones_insert(dump_file):
    """
    Cuenta las instrucciones INSERT INTO en un archivo SQL.
    """
    with open(dump_file, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    
    # Buscar todas las instrucciones INSERT INTO
    inserts = re.findall(r"INSERT INTO `.*?`.*?;", contenido, re.DOTALL)
    return len(inserts)

def guardar_conteo_en_archivo(conteo, archivo_salida):
    """
    Guarda el conteo de instrucciones INSERT INTO en un archivo.
    """
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write(f"Cantidad de instrucciones INSERT INTO encontradas: {conteo}\n")
    print(f"Conteo guardado en {archivo_salida}")

def main():
    # Configuración de los argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Cuenta las instrucciones INSERT INTO en un archivo SQL y guarda el conteo en un archivo de salida.",
        epilog="Ejemplo de uso:\n  python pysqlcount.py --dumpfile dumpAPP_NOTIFICACION_ACUSE.sql --outputfile conteo_inserts.txt \n\n"
        "Creado por Jaquerman con mucho amor para Cindy ita <3",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--dumpfile", required=True, help="Ruta al archivo SQL de entrada (e.g., dumpAPP_NOTIFICACION_ACUSE.sql).")
    parser.add_argument("--outputfile", help="Ruta al archivo de salida para guardar el conteo (e.g., conteo_inserts.txt). Si no se proporciona, se usará el nombre del archivo dump con extensión .txt.")
    args = parser.parse_args()

    # Si no se proporciona el archivo de salida, usar el nombre del dumpfile con extensión .txt
    if not args.outputfile:
        args.outputfile = os.path.splitext(args.dumpfile)[0] + ".txt"

    try:
        conteo = contar_instrucciones_insert(args.dumpfile)
        print(f"Cantidad de instrucciones INSERT INTO encontradas: {conteo}")
        guardar_conteo_en_archivo(conteo, args.outputfile)
    except FileNotFoundError:
        print(f"No se encontró el archivo {args.dumpfile}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
