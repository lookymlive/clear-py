import os
import shutil

def limpiar_temporales():
    ruta_temp = os.environ.get("TEMP")
    if ruta_temp:
        for archivo in os.listdir(ruta_temp):
            ruta_completa = os.path.join(ruta_temp, archivo)
            try:
                if os.path.isfile(ruta_completa):
                    os.remove(ruta_completa)
                elif os.path.isdir(ruta_completa):
                    shutil.rmtree(ruta_completa)
            except Exception as e:
                print(f"Error al eliminar {ruta_completa}: {e}")

def vaciar_papelera():
    # Esta función depende de la librería 'winshell' que no está incluida en Python
    # Puedes instalarla con: pip install pywin32
    try:
        import winshell
        winshell.empty_recycle_bin()
    except ImportError:
        print("La librería 'winshell' no está instalada. No se puede vaciar la papelera.")
    except Exception as e:
        print(f"Error al vaciar la papelera: {e}")

def main():
    print("Limpiando archivos temporales...")
    limpiar_temporales()
    print("Archivos temporales eliminados.")

    print("Vaciando la papelera de reciclaje...")
    vaciar_papelera()
    print("Papelera de reciclaje vaciada.")

if __name__ == "__main__":
    main()