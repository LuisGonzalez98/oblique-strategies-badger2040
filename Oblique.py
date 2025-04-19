from badger2040 import Badger2040, BUTTON_A, BUTTON_B, BUTTON_C
import random
import time

# Estrategias Oblicuas en español

estrategias = [
    "ELIMINA ESPECÍFICOS Y HAZLOS AMBIGUOS",
    "NO TENGAS MIEDO A LOS CLICHÉS",
    "¿CUÁL ES LA REALIDAD DE LA SITUACIÓN?",
    "¿HAY SECCIONES? CONSIDERA TRANSICIONES",
    "DALE LA VUELTA",
    "PERMITE UNA EXCEPCIÓN",
    "SUSTRACCIÓN SIMPLE",
    "DALE LA VUELTA AL EXTERIOR",
    "ESTRATEGIAS OBLICUAS ©",
    "UNA LÍNEA TIENE DOS LADOS",
    "GRADACIONES INFINITESIMALES",
    "HAZ UNA LISTA EXHAUSTIVA Y HAZ LO ÚLTIMO",
    "HACIA LO IMPOSIBLE",
    "PIDE QUE TRABAJEN CONTRA SU JUICIO",
    "QUITA ELEMENTOS POR NO IMPORTANCIA",
    "CAMBIA LOS ROLES DE LOS INSTRUMENTOS",
    "ACRECIÓN",
    "DESCONECTA DEL DESEO",
    "ENFATIZA REPETICIONES",
    "NO TENGAS MIEDO POR SER FÁCIL",
    "¿FALTA ALGO?",
    "NO TEMAS MOSTRAR TU TALENTO",
    "RESPIRA PROFUNDO",
    "HONRA EL ERROR COMO INTENCIÓN OCULTA",
    "SOLO UN ELEMENTO DE CADA TIPO",
    "USA GENTE NO CALIFICADA",
    "¿CÓMO LO HABRÍAS HECHO?",
    "ENFATIZA DIFERENCIAS",
    "NO HAGAS NADA EL MÁXIMO TIEMPO POSIBLE",
    "PUENTES: CONSTRUYE/QUEMA",
    "AGUA",
    "NO TE AVERGÜENCES DE TUS IDEAS",
    "ORDENA",
    "¿CAMBIAR PALABRAS?",
    "PREGUNTA A TU CUERPO",
    "ACCIÓN DESTRUCTIVA IMPREDECIBLE",
    "CONSULTA OTRAS FUENTES",
    "USA UN COLOR INACEPTABLE",
    "HUMANIZA ALGO PERFECTO",
    "USA FILTROS",
    "LLENA CADA COMPÁS",
    "DESCARTA UN AXIOMA",
    "¿QUÉ NO HARÍAS?",
    "DECORA, DECORA",
    "NO HAGAS NADA EL MÁXIMO TIEMPO",
    "ESCUCHA LA VOZ SILENCIOSA",
    "¿ESTÁ TERMINADO?",
    "PONTE TAPONES",
    "DA EL JUEGO",
    "REVERSO",
    "ABANDONA INSTRUMENTOS NORMALES",
    "USA MENOS NOTAS",
    "LA REPETICIÓN ES CAMBIO",
    "CÉDE A TU PEOR IMPULSO",
    "CONFÍA EN TU YO ACTUAL",
    "¿QUÉ HARÍA TU AMIGO?",
    "DISTORSIONA EL TIEMPO",
    "ENCUADRA LO VACÍO",
    "PRINCIPIO DE INCONSISTENCIA",
    "ECO FANTASMA",
    "SOLO UN PUNTO A LA VEZ",
    "SIGUE ADELANTE",
    "MAQUINARIA ORGÁNICA",
    "NO ROMPAS EL SILENCIO",
    "DESCUBRE Y ABANDONA RECETAS",
    "CASCADAS",
    "VALOR",
    "¿QUÉ ERRORES COMETISTE?",
    "CONSIDERA FADES DIFERENTES",
    "MUTE Y CONTINÚA",
    "ES POSIBLE",
    "NO SOBREVALORES NADA",
    "AMBIGÜEDADES A ESPECÍFICOS",
    "OBSERVA EL ORDEN",
    "SAL, CIERRA PUERTA",
    "¿NECESITAMOS AGUJEROS?",
    "ANÁLISIS DE CLÚSTER",
    "TRABAJA A OTRA VELOCIDAD",
    "HAZ ALGO ABURRIDO",
    "DEFINE UN ÁREA SEGURA",
    "RESISTE EL CAMBIO",
    "ACEPTA CONSEJOS",
    "AMPLIFICA LO EMBARAZOSO",
    "MECANIZA LO IDIOSINCRÁTICO",
    "ENFATIZA DEFECTOS",
    "RECUERDA VELADAS TRANQUILAS",
    "TÓMATE UN DESCANSO",
    "LA CINTA ES LA MÚSICA",
    "CORTOCIRCUITO",
    "USA UNA IDEA VIEJA",
    "DESTRUYE NADA / LO MÁS IMPORTANTE",
    "NO CAMBIES NADA",
    "IMAGINA CADENA MÓVIL",
    "IMAGINA EVENTOS DESCONECTADOS",
    "¿EN QUÉ PIENSAS AHORA?",
    "VOCES INFANTILES",
    "AGRUPA INSTRUMENTOS",
    "CIERRA PUERTA Y ESCUCHA",
    "¿AFINA CORRECTAMENTE?",
    "MIRA UN OBJETO PEQUEÑO",
    "FEEDBACK ACÚSTICO",
    "HACIA LO INSIGNIFICANTE",
    "SIMPLEMENTE TRABAJO",
    "NO CONSTRUYAS MURO, HAZ LADRILLO",
    "REVALUACIÓN",
    "AUTOINDULGENCIA DISCIPLINADA",
    "LO MÁS OLVIDADO",
    "GOZO IDIOTA",
    "SÉ EXTRAVAGANTE",
    "DEFINE PROBLEMA CLARAMENTE",
    "SIEMPRE PRIMEROS PASOS",
    "CUESTIONA LO HEROICO",
    "DATE CRÉDITO",
    "FRENTE A DOS, HAZ AMBOS",
    "CIERRA BOCA",
    "TORCE LA ESPINA",
    "MASAJE DE CUELLO",
    "LAVA LOS PLATOS",
    "RITMO DE MELODÍA",
    "ANÁLISIS DE ESPECTRO",
    "CHEQUEO DE MÍNIMO COMÚN",
    "ESCUCHA EN OSCURIDAD",
    "¿LO QUERRÍAN?",
    "RECUERDA PASOS",
    "EXTREMO Y VUELVE",
    "BUSCA HASTA ENCONTRAR",
    "SOLO PARTE, NO TODO",
    "DE NADA A MÁS QUE NADA",
    "CRÍTICA REDUCIDA",
    "TARJETAS EN BLANCO"
]

SCREEN_W = 298
SCREEN_H = 128
badger = Badger2040()
display = badger.display

def mostrar_texto_lineas(lineas, scale=2, spacing=4, y_offset=0, ajuste_x=0, fondo=15, texto=0):
    display.set_pen(fondo)
    display.clear()
    display.set_pen(texto)
    char_width = 6.5
    line_height = 8 * scale
    total_height = len(lineas) * line_height + (len(lineas) - 1) * spacing
    y = ((SCREEN_H - total_height) // 2) + y_offset
    for linea in lineas:
        width = int(len(linea) * char_width * scale)
        x = (SCREEN_W - width) // 2 + ajuste_x
        display.text(linea, x, y, scale=scale)
        y += line_height + spacing
    badger.update()

def dividir_en_lineas(frase, max_chars=16, max_lineas=3):
    palabras = frase.split()
    lineas = []
    actual = ""
    for palabra in palabras:
        if len(actual) + len(palabra) + (1 if actual else 0) <= max_chars:
            actual += " " + palabra if actual else palabra
        else:
            lineas.append(actual)
            actual = palabra
            if len(lineas) == max_lineas - 1:
                break
    if actual and len(lineas) < max_lineas:
        lineas.append(actual)
    return lineas

def mostrar_bienvenida():
    mostrar_texto_lineas(
        ["Oblique Strategies", "Brian Eno / Peter Schmidt"],
        scale=2,
        spacing=4,
        y_offset=0,
        ajuste_x=32,
        fondo=0,
        texto=15
    )
    time.sleep(5)

def mostrar_instrucciones():
    mostrar_texto_lineas(
        [
            "INSTRUCCIONES",
            "Solo en caso de bloqueo absoluto.",
            "Toma una carta.",
            "Solo una.",
            "Acéptala sin cuestionar.",
            "y continúa",
            "",
            "(si aceptas apreta el botón)"
        ],
        scale=1,
        spacing=4,
        fondo=0,
        texto=15
    )
    time.sleep(5)

def mostrar_frase(frase):
    lineas = dividir_en_lineas(frase)
    mostrar_texto_lineas(
        lineas,
        scale=3,
        spacing=0,
        fondo=15,
        texto=0,
        ajuste_x=20
    )

def mostrar_despedida():
    mostrar_texto_lineas(["Adiós", "Genio"], scale=4, fondo=0, texto=15)
    inicio = time.time()
    while time.time() - inicio < 10:
        badger.keepalive()
        if badger.pressed(BUTTON_B):
            main()
            return
        time.sleep(0.1)

def esperar_o_despedir():
    tiempo_inicio = time.time()
    while True:
        badger.keepalive()
        if badger.pressed(BUTTON_C):
            return
        if time.time() - tiempo_inicio >= 300:
            return
        time.sleep(0.1)

def run_oraculo():
    while True:
        badger.keepalive()
        if badger.pressed(BUTTON_A) or badger.pressed(BUTTON_B):
            frase_random = random.choice(estrategias)
            mostrar_frase(frase_random)
            esperar_o_despedir()
            mostrar_despedida()
            break
        elif badger.pressed(BUTTON_C):
            mostrar_despedida()
            break
        time.sleep(0.1)

def main():
    random.seed(time.ticks_ms())
    mostrar_bienvenida()
    mostrar_instrucciones()
    run_oraculo()
    
main()

