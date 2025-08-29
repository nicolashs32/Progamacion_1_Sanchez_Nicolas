from gestion_parque.py import parque.py

def main():
    print(" Bienvenido a PythonLand ")
    resumen = parque.registrar_visita()
    parque.mostrar_resumen(resumen)

if __name__ == "__main__":
    main()