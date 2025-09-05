from gestion_parque.parque import registrar_visita, mostrar_resumen

def main():
    resumen = registrar_visita()
    mostrar_resumen(resumen)
