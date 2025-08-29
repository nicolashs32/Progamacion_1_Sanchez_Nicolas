from gestion_del_parque import parque.py

def main():
    resumen = parque.registrar_visita()
    parque.mostrar_resumen(resumen)
