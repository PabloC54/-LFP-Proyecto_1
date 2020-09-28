import webbrowser

# Inicializando

Cbegin = "\x1b[0;37;40m"
Cend = "\x1b[0m"
Hcolor = "\x1b[1;30;47m"

set_names = []
set_files = []
selected_set = []

# Tokens

tk_help = ["help", "ayuda"]
tk_close = ["close", "exit", "cerrar", "salir"]

tk_blank = [" "]
tk_create = ["create", "crear"]
tk_set = ["set"]
tk_load = ["load", "cargar"]
tk_into = ["into", "en"]
tk_files = ["files", "archivos"]
tk_use = ["use", "usar"]
tk_select = ["select", "seleccionar"]
tk_where = ["where", "donde"]
tk_list = ["list", "listar"]
tk_atributes = ["atributes", "atributos"]
tk_print = ["print"]
tk_in = ["in"]
tk_max = ["max", "maximo"]
tk_min = ["min", "minimo"]
tk_sum = ["sum", "suma"]
tk_count = ["count", "contar"]
tk_report = ["report", "reportar"]
tk_to = ["to"]
tk_tokens = ["tokens"]
tk_script = ["script"]
tk_and = ["and", "y"]
tk_or = ["or", "o"]
tk_xor = ["xor", "nor"]
reserved = (
    tk_help
    + tk_close
    + tk_create
    + tk_set
    + tk_load
    + tk_into
    + tk_files
    + tk_use
    + tk_select
    + tk_where
    + tk_list
    + tk_atributes
    + tk_print
    + tk_in
    + tk_max
    + tk_min
    + tk_sum
    + tk_count
    + tk_report
    + tk_to
    + tk_tokens
    + tk_script
    + tk_and
    + tk_or
    + tk_xor
)

tk_parA = ["("]
tk_parB = [")"]
tk_menorQ = ["<"]
tk_mayorQ = [">"]
tk_corchA = ["["]
tk_corchB = ["]"]
tk_igual = ["="]
tk_coma = [","]
tk_punto = ["."]
tk_scolon = [";"]
tk_guion = ["-"]
tk_asterisco = ["*"]
tk_comilla = ['"', "'"]
tk_letra = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚÀÈÌÒÙÄËÏÖÜÂÊÎÔÛáéíóúàèìòùäëïöüâêîôû^~|¡!#$%&/¿?-_"
tk_digito = "1234567890"
tk_texto = (
    tk_letra
    + tk_digito
    + tk_parA[0]
    + tk_parB[0]
    + tk_menorQ[0]
    + tk_mayorQ[0]
    + tk_corchA[0]
    + tk_corchB[0]
    + tk_coma[0]
    + tk_punto[0]
    + tk_guion[0]
)
tk_color = [
    "blue",
    "red",
    "green",
    "yellow",
    "orange",
    "pink",
    "white",
    "azul",
    "rojo",
    "verde",
    "amarillo",
    "naranja",
    "rosa",
    "blanco"
]
tk_no_igual = ["!="]
tk_mayor_igual = [">="]
tk_menor_igual = ["<="]
tk_operadores = tk_menorQ+tk_mayorQ+tk_igual + \
    tk_menor_igual+tk_mayor_igual+tk_no_igual

# Comandos


def Mensaje(texto):

    if texto:
        print(
            "\n\x1b[0;30;41m"
            + ">>>>>>>>>>>>>"
            + Cend
            + "  "
            + Cbegin
            + texto
            + Cend
            + "  \x1b[0;30;41m"
            + "<<<<<<<<<<<<<"
            + Cend
            + "\n"
        )


def Ayuda(word):

    if word == "":

        print(
            Cbegin
            + """
            Funciones internas de SimpleSQL:

        -CARGAR: carga archivos .json a la memoria del programa.
                    Modo de uso: 'CARGAR archivo1.json, archivo2.json,... '.

        -SELECCIONAR: selecciona llaves de los archivos cargados.
                        Modo de uso: 'SELECCIONAR param1, param2,... (DONDE condicion=valor)'
                        Si se usa una condición string, se debe rodear en comillas "" o ''.

        -MAXIMO: busca el parametro numérico de mayor valor entre los archivos cargados. 
                    Modo de uso: 'MAXIMO param'.

        -MINIMO: busca el parametro numérico de mayor valor entre los archivos cargados.
                    Modo de uso: 'MINIMO param'.

        -SUMA: suma todos los valores del parametro indicado, de los archivos cargados.
                Modo de uso: 'SUMA param'.

        -CUENTA: cuenta el número de archivos guardados.
                    Modo de uso: 'CUENTA'.

        -REPORTAR: exporta un archivo HTML con los registros de los archivos guardados.
                    Modo de uso: 'Reportar num'

        -Usa 'salir', 'exit', 'out', 'close' para finalizar la ejecución de SimpleSQL
        """
            + Cend
        )

    elif word in tk_create:
        print(Cbegin + "" + Cend)

    elif word in tk_load:
        print(Cbegin + "" + Cend)

    elif word in tk_use:
        print(Cbegin + "" + Cend)

    elif word in tk_select:
        print(Cbegin + "" + Cend)

    elif word in tk_list:
        print(Cbegin + "" + Cend)

    elif word in tk_print:
        print(Cbegin + "" + Cend)

    elif word in tk_max:
        print(Cbegin + "" + Cend)

    elif word in tk_min:
        print(Cbegin + "" + Cend)

    elif word in tk_sum:
        print(Cbegin + "" + Cend)

    elif word in tk_count:
        print(Cbegin + "" + Cend)

    elif word in tk_report:
        print(Cbegin + "" + Cend)

    elif word in tk_script:
        print(Cbegin + "" + Cend)

    else:
        Mensaje("No se reconoció el comando " + word)


def Create(nombre):

    if nombre not in set_names:
        set_names.append(nombre)
        set_files.append([])

    else:
        Mensaje("El set '" + nombre + "' ya existe")


def Load(nombre, archivos):

    global selected_set
    temp_set = set_files[set_names.index(nombre)]  # Local

    for archivo in archivos:

        try:

            temp = open(archivo, "r")
            temp = AON(temp.read())
            temp_set.append(temp)

        except:

            Mensaje("No se encontró '" + archivo + "'")

    selected_set = temp_set


def Use(nombre):

    global selected_set
    seleted_set = set_files[set_names.index(nombre)]


def Select(lista_llaves, condicion, conjuncion):

    global selected_set
    lista_tuplas, lista_final = [], []
    diccionario_prueba = {}

    try:

        if selected_set:  # Verificando si se seleccionó un set (Use)
            diccionario_prueba = selected_set[0][0]
        else:
            Mensaje("No se ha seleccionado un set, o no se han cargado archivos")
            err += 1

        if lista_llaves == ["*"]:  # Verificando si se ingresó '*'
            lista_llaves = diccionario_prueba.keys()

        for llave in lista_llaves:  # Removiendo los atributos que no existen
            if llave not in diccionario_prueba:

                lista_llaves.remove(llave)
                Mensaje("Atributo '" + llave + "' no encontrado")

        header = "    ||    "  # ENCABEZADO
        for llave in lista_llaves:
            header = header + llave + "    ||    "
        print("\n"+Hcolor + header + "\n" + "=" * len(header) + Cend+"\n")

        if condicion:
            rango = len(condicion) // 3
        else:
            rango = 1

        for i in range(rango):

            if condicion:

                condicion_llave = condicion[3 * i].strip()
                condicion_operador = condicion[3 * i + 1].strip()
                condicion_valor = condicion[3 * i + 2].strip()

                if Numero(condicion_valor):
                    condicion_valor = float(condicion_valor)

                elif Booleano(condicion_valor) in [True, False]:
                    condicion_valor = Booleano(condicion_valor)

                else:
                    condicion_valor = condicion_valor[1:-1]

            tuplas = []

            for (
                archivo
            ) in selected_set:  # Iterando en el set de archivos seleccionado con 'Use'

                for (
                    diccionario
                ) in archivo:  # Iterando sobre cada diccionario de cada archivo

                    cumple_condicion = True

                    if condicion:

                        if condicion_operador in tk_igual:

                            if diccionario[condicion_llave] == condicion_valor:
                                pass
                            else:
                                cumple_condicion = False

                        elif condicion_operador in tk_mayorQ:

                            if diccionario[condicion_llave] > condicion_valor:
                                pass
                            else:
                                cumple_condicion = False

                        elif condicion_operador in tk_menorQ:

                            if diccionario[condicion_llave] < condicion_valor:
                                pass
                            else:
                                cumple_condicion = False

                        elif condicion_operador in tk_no_igual:

                            if diccionario[condicion_llave] != condicion_valor:
                                pass
                            else:
                                cumple_condicion = False

                        elif condicion_operador in tk_mayor_igual:

                            if diccionario[condicion_llave] != None:
                                if diccionario[condicion_llave] >= condicion_valor:
                                    pass
                                else:
                                    cumple_condicion = False

                        elif condicion_operador in tk_menor_igual:

                            if diccionario[condicion_llave] != None:
                                if diccionario[condicion_llave] <= condicion_valor:
                                    pass
                                else:
                                    cumple_condicion = False

                    if cumple_condicion:

                        tupla = "    ||  "
                        for llave in lista_llaves:

                            tupla = tupla + \
                                str(diccionario[llave]) + "  ||  "

                        tuplas.append(tupla)

            lista_tuplas.append(tuplas)

        if len(lista_tuplas) > 1:

            if conjuncion in tk_and:

                for tupla in lista_tuplas[0]:

                    if tupla in lista_tuplas[1]:
                        lista_final.append(tupla)

            elif conjuncion in tk_or:

                lista_final = lista_tuplas[0]
                for tupla in lista_tuplas[1]:

                    if tupla not in lista_final:
                        lista_final.append(tupla)

            elif conjuncion in tk_xor:

                lista_final = lista_tuplas[0]
                for tupla in lista_tuplas[1]:

                    if tupla not in lista_final:
                        lista_final.append(tupla)

                for tupla in lista_final:
                    if tupla in lista_tuplas[0] and tupla in lista_tuplas[1]:
                        lista_final.remove(tupla)

            else:
                lista_final = lista_tuplas[0]

        else:

            lista_final = lista_tuplas[0]

        if lista_final:
            for tupla in lista_final:
                print(Cbegin + tupla + Cend)
            print("\n"+Hcolor + "=" * len(header) + Cend+"\n")

        else:
            print(Cbegin+" ~ " * (len(header)//3) + Cend)
            print("\n"+Hcolor + "=" * len(header) + Cend+"\n")

    except:
        pass


def List():

    print("\n"+Hcolor + "   Atributos   \n" + "=" * 15 + Cend+"\n")

    if selected_set:
        diccionario_muestra = selected_set[0][0]

        for atributo in diccionario_muestra:
            print("   "+atributo)

    else:
        print(Cbegin+" ~ " * 5)

    print("\n"+Hcolor + "=" * 15 + Cend+"\n")


def Print(color):
    global Cbegin, Hcolor

    if color in ["blue", "azul"]:
        Cbegin = "\x1b[0;34;40m"
        Hcolor = "\x1b[0;30;44m"

    if color in ["red", "rojo"]:
        Cbegin = "\x1b[0;31;40m"
        Hcolor = "\x1b[0;30;41m"

    if color in ["green", "verde"]:
        Cbegin = "\x1b[0;32;40m"
        Hcolor = "\x1b[0;30;42m"

    if color in ["yellow", "amarillo"]:
        Cbegin = "\x1b[0;33;40m"
        Hcolor = "\x1b[5;30;43m"

    if color in ["orange", "naranja"]:
        Cbegin = "\x1b[1;33;40m"
        Hcolor = "\x1b[0;30;43m"

    if color in ["pink", "rosa"]:
        Cbegin = "\x1b[0;35;40m"
        Hcolor = "\x1b[6;30;41m"

    if color in ["white", "blanco"]:
        Cbegin = "\x1b[0;37;40m"
        Hcolor = "\x1b[1;30;47m"


def Max(llave):

    if selected_set:

        valor_maximo = selected_set[0][0][llave]

        for archivo in selected_set:

            for diccionario in archivo:
                
                if diccionario[llave] != None:

                    if diccionario[llave] > valor_maximo:
                        valor_maximo = diccionario[llave]

        print("\n",Cbegin + valor_maximo + Cend, "\n")

    else:
        Mensaje("No se ha seleccionado un set")


def Min(llave):

    if selected_set:

        valor_minimo = selected_set[0][0][llave]

        for archivo in selected_set:

            for diccionario in archivo:
                
                if diccionario[llave] != None:

                    if diccionario[llave] < valor_minimo:
                        valor_minimo = diccionario[llave]

        print("\n",Cbegin + valor_minimo + Cend, "\n")

    else:
        Mensaje("No se ha seleccionado un set")


def Sum(lista_llaves):

    if lista_llaves == ["*"]:  # Verificando si se ingresó '*'
        lista_llaves = selected_set[0][0].keys()

    if selected_set:

        lista_sumas = []
        for llave in lista_llaves:

            if Numero(selected_set[0][0][llave]):

                suma = 0

                for archivo in selected_set:

                    for diccionario in archivo:

                        suma += diccionario[llave]

                lista_sumas.append(suma)

            else:
                lista_sumas.append("NO_NUM")

        header = "    ||    "  # ENCABEZADO
        for llave in lista_llaves:
            header = header + llave + "    ||    "
        print("\n"+Hcolor + header + "\n" + "=" * len(header) + Cend+"\n")

        fila = Cbegin+"    ||  "  # SUMAS
        for suma in lista_sumas:
            fila = fila + \
                str(suma) + "  ||  "
        fila = fila+Cend+"\n"

        print(fila)

    else:
        Mensaje("No se ha seleccionado un set")


def Count(lista_llaves):
    
    if lista_llaves == ["*"]:  # Verificando si se ingresó '*'
        lista_llaves = selected_set[0][0].keys()

    lista_cuentas = []

    for llave in lista_llaves:

        cuenta = 0
        for archivo in selected_set:

            for diccionario in archivo:

                if llave in diccionario and diccionario[llave] not in ["null", None]:
                    cuenta += 1

        lista_cuentas.append(cuenta)

    header = "  ||  "  # ENCABEZADO
    for llave in lista_llaves:
        header = header + llave + "  ||  "
    print("\n"+Hcolor + header + "\n" + "=" * len(header) + Cend+"\n")

    fila = Cbegin+"    ||  "  # SUMAS
    for cuenta in lista_cuentas:
        fila = fila + \
            str(cuenta) + "  ||  "
            
    print(fila+Cend+"\n\n"+Hcolor + "=" * len(header) + Cend+"\n")


def Report(num):

    if len(registros) > 0:

        diccionarios_totales = 0
        for registro in registros:
            for diccionario in registro:
                diccionarios_totales += 1

        if num <= diccionarios_totales:

            html_file = open("reporte.html", "w")

            html_file.write(
                "<!DOCTYPE html>\n"
                + "<html>\n"
                + "    <head>\n"
                + "        <title>Reporte de registros</title>\n"
                + "        <style>\n"
                + "            body{\n"
                + "                background-image:url(bg.png);\n"
                + "            }\n"
                + "            .registro{\n"
                + "                background-color:black;\n"
                + "                width: 60%;\n"
                + "                padding: 15px;\n"
                + "                margin: 10px 20%;\n"
                + "            }\n"
                + "            .diccionario{\n"
                + "                background-color:darkslategray;\n"
                + "                padding: 2px 10px;\n"
                + "                margin: 8px;\n"
                + "            }\n"
                + "            h2{\n"
                + "                color:white;\n"
                + "                text-decoration: underline;\n"
                + "            }\n"
                + "            h3{\n"
                + "                color:aquamarine;\n"
                + "            }\n"
                + "            p{\n"
                + "                color:lightblue;\n"
                + "            }\n"
                + "        </style>\n"
                + "    <head>\n\n"
                + "    <body>\n"
            )

            num_registro, num_diccionario = 0, 0

            try:
                for registro in registros:  # BODY
                    html_file.write(
                        "        <div class='registro'>\n"
                        + "            <h2>Nombre: REGISTRO "
                        + str(num_registro + 1)
                        + "</h2>\n\n"
                    )

                    for diccionario in registro:
                        html_file.write(
                            "            <div class='diccionario'>\n"
                            + "                <h3>Diccionario "
                            + str(num_diccionario + 1)
                            + "</h3>\n"
                        )

                        for key, value in diccionario.items():
                            html_file.write(
                                "                <p><b>"
                                + str(key)
                                + ":</b>  "
                                + str(value)
                                + "</p>\n"
                            )

                        html_file.write("            </div>\n\n")
                        num_diccionario += 1
                        if num_diccionario == num:
                            err += 1

                    html_file.write("        </div>\n\n")
                    num_registro += 1

            except:
                html_file.write("        </div>\n")
                print("COMPLETO ")

                # Abrir el archivo HTML
                webbrowser.open("reporte.html")

            html_file.write("    </body>\n" + "</html>")

        else:
            print("'" + str(num) + "' excede el número total de registros cargados")

    else:
        print("No se han cargado archivos")


def Script(scripts):

    for archivo in scripts:

        try:
            temp = open(archivo, "r")

            for Instruccion in temp:
                SimpleSQL(Instruccion)

            temp.close()

        except:
            Mensaje("No se encontró el archivo " + archivo)


# ================> AFD <====================


#        ~~> SimpleSQL CLI <~~


def SimpleSQL(Instruccion):

    exit, late_exit, coma, comilla = False, False, False, False
    estado = 0
    error_msg, nombre_set, conjuncion = "", "", ""
    lista_llaves, archivos_set, condicion, scripts = [], [], [], []

    while exit == False:

        if Instruccion:
            query = Instruccion.strip().lower() + " "
            print(Hcolor+" >> "+Cend+" "+Cbegin+query+Cend)
            word, Instruccion = "", ""
            late_exit = True

        else:
            query = input(Hcolor+" >> "+Cend+" " +
                          Cbegin).strip().lower() + " ; "+Cend
            word = ""

        try:
            for char in query:

                if char in tk_comilla:

                    if comilla:
                        comilla = False

                    else:
                        comilla = True

                if char in tk_coma and comilla == False:
                    coma = True

                if char not in tk_blank + tk_coma or comilla == True:

                    if estado != 35:
                        char.lower()

                    word = word + char

                elif estado == 0:  # INICIO

                    if word in tk_create:
                        estado = 1

                    elif word in tk_load:
                        estado = 11

                    elif word in tk_use:
                        estado = 21

                    elif word in tk_select:
                        estado = 31

                    elif word in tk_list:
                        estado = 41

                    elif word in tk_print:
                        estado = 51

                    elif word in tk_max:
                        estado = 61

                    elif word in tk_min:
                        estado = 71

                    elif word in tk_sum:
                        estado = 81

                    elif word in tk_count:
                        estado = 91

                    elif word in tk_report:
                        estado = 101

                    elif word in tk_script:
                        estado = 111

                    elif word in tk_help:
                        estado = 121

                    elif word in tk_close:
                        print(Cend)
                        exit = True

                    else:

                        if word != ";":
                            error_msg = ""
                            error_msg = "No se reconoció la palabra " + word
                            estado = -1

                    word = ""

                # ------> CREATE <--------

                elif estado == 1:

                    if word in tk_set:
                        estado = 2

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba 'set'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'set'"
                            )

                        estado = -1

                    word = ""

                elif estado == 2:

                    if Palabra(word):
                        Create(word)
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un nombre para el set"

                        else:
                            error_msg = "Nombre de set no válido"

                        estado = -1

                    word = ""

                # ------> LOAD <--------

                elif estado == 11:

                    if word in tk_into:
                        estado = 12

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba 'into'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'into'"
                            )

                        estado = -1

                    word = ""

                elif estado == 12:

                    if word in set_names:
                        nombre_set = word
                        archivos_set = []

                        estado = 13

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un set"

                        else:
                            error_msg = "No existe el set " + word

                        estado = -1

                    word = ""

                elif estado == 13:

                    if word in tk_files:
                        estado = 14

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba 'files'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'files'"
                            )

                        estado = -1

                    word = ""

                elif estado == 14:

                    if ArchivoAON(word):
                        archivos_set.append(word)
                        estado = 15

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un archivo AON"

                        else:
                            error_msg = word + " no es un archivo AON"

                        estado = -1

                    word = ""

                elif estado == 15:

                    if coma == True:

                        coma = False
                        estado = 14

                    else:

                        if word in tk_scolon:
                            Load(nombre_set, archivos_set)

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Archivos múltiples se separan por comas"
                            )
                            estado = -1

                    word = ""

                # ------> USE <--------

                elif estado == 21:

                    if word in tk_set:
                        estado = 22

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba 'set'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'set'"
                            )

                        estado = -1

                    word = ""

                elif estado == 22:

                    if word in set_names:
                        Use(word)
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un set"

                        else:
                            error_msg = "No existe el set " + word

                        estado = -1

                    word = ""

                # ------> SELECT <--------

                elif estado == 31:

                    if word in tk_asterisco:
                        lista_llaves = ["*"]
                        estado = 32

                    elif Palabra(word):
                        lista_llaves = [word]
                        estado = 33

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = "No se reconoció la palabra " + word + "."

                        estado = -1

                    word = ""

                elif estado == 32:  # *

                    if word in tk_where:
                        estado = 35

                    else:

                        if word in tk_scolon:
                            Select(lista_llaves, condicion, conjuncion)
                            lista_llaves, condicion, conjuncion = [], [], ""
                            estado = 150

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'where'"
                            )

                            estado = -1

                    word = ""

                elif estado == 33:

                    if coma == True:
                        coma = False
                        estado = 34

                    elif word in tk_where:
                        estado = 35

                    else:

                        if word in tk_scolon:
                            Select(lista_llaves, condicion, conjuncion)
                            lista_llaves, condicion, conjuncion = [], [], ""
                            estado = 150

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Múltiples archivos se separan por comas"
                            )

                            estado = -1

                    word = ""

                elif estado == 34:

                    if Palabra(word):
                        lista_llaves.append(word)
                        estado = 33

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un atributo"
                            )

                        estado = -1

                    word = ""

                elif estado == 35:  # where

                    if (Palabra(word) or Numero(word) or Booleano(word) in [True, False, None] or word in tk_operadores) and comilla == False:
                        condicion.append(word)

                        if len(condicion) % 3 == 0 and comilla == False:  # validar condicion
                            estado = 36
                        else:
                            estado = 35
                    elif comilla == True:
                        word = word+" "

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba una condición"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba una condición"
                            )

                        estado = -1

                    if comilla == False:
                        word = ""

                elif estado == 36:

                    if word in tk_and + tk_or + tk_xor:
                        conjuncion = word
                        estado = 35

                    else:

                        if word in tk_scolon:

                            Select(lista_llaves, condicion, conjuncion)
                            lista_llaves, condicion, conjuncion = [], [], ""
                            estado = 150

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba una condición"
                            )

                        estado = -1

                    word = ""

                # ------> LIST <--------

                elif estado == 41:

                    if word in tk_atributes:
                        List()
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba 'atributes'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'atributes'"
                            )

                        estado = -1

                    word = ""

                # ------> PRINT <--------

                elif estado == 51:

                    if word in tk_in:
                        estado = 52

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba 'in'"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba 'in'"
                            )

                        estado = -1

                    word = ""

                elif estado == 52:

                    if word in tk_color:
                        Print(word)
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba un color"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un color"
                            )

                        estado = -1

                    word = ""

                # ------> MAX <--------

                elif estado == 61:

                    if Palabra(word):
                        Max(word)
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un atributo"
                            )

                        estado = -1

                    word = ""

                # ------> MIN <--------

                elif estado == 71:

                    if Palabra(word):
                        Min(word)
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un atributo"
                            )

                        estado = -1

                    word = ""

                # ------> SUM <--------

                elif estado == 81:

                    if word in tk_asterisco:
                        Sum(["*"])
                        estado = 150

                        if late_exit == True:
                            exit = True

                    elif Palabra(word):
                        lista_llaves.append(word)
                        estado = 82

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un atributo"
                            )

                        estado = -1

                    word = ""

                elif estado == 82:

                    if coma == True:
                        coma = False
                        estado = 81

                    else:

                        if word in tk_scolon:
                            Sum(lista_llaves)
                            lista_llaves = []
                            estado = 150

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = "No se reconoció la palabra " + word

                            estado = -1

                    word = ""

                # ------> COUNT <--------

                elif estado == 91:

                    if word in tk_asterisco:
                        Count(["*"])
                        estado = 150

                    elif Palabra(word):
                        lista_llaves.append(word)
                        estado = 92

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un atributo"
                            )

                        estado = -1

                    word = ""

                elif estado == 92:

                    if coma == True:
                        coma = False
                        estado = 93

                    else:
                        if word in tk_scolon:
                            
                            Count(lista_llaves)
                            lista_llaves = []
                            estado = 150

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = "No se reconoció la palabra " + word

                            estado = -1

                    word = ""

                elif estado == 93:

                    if Palabra(word):
                        lista_llaves.append(word)
                        estado = 92

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un atributo"

                        else:
                            error_msg = "No se reconoció la palabra " + word

                        estado = -1

                    word = ""

                # ------> REPORTE <--------

                elif estado == 101:

                    if word in tk_to:
                        estado = 102

                    elif word in tk_tokens:
                        Report()
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:
                        if word in tk_scolon:
                            error_msg = "Se esperaba to|tokens"

                        else:

                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba to|tokens"
                            )

                        estado = -1

                    word = ""

                elif estado == 102:

                    if Palabra(word):
                        estado = 103

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un nombre"

                        else:
                            error_msg = word + " no es un nombre válido"

                        estado = -1

                    word = ""

                elif estado == 103:

                    if word:  # is comando
                        Report("comando")
                        estado = 150

                        if late_exit == True:
                            exit = True

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un comando"

                        else:
                            error_msg = word + " no es comando válido"

                        estado = -1

                    word = ""

                # ------> SCRIPT <--------

                elif estado == 111:

                    if ArchivoSIQL(word):
                        scripts.append(word)
                        estado = 112

                    else:

                        if word in tk_scolon:
                            error_msg = "Se esperaba un archivo SIQL"

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Se esperaba un archivo SIQL"
                            )

                        estado = -1

                    word = ""

                elif estado == 112:

                    if coma == True:
                        coma = False
                        estado = 111

                    else:

                        if word in tk_scolon:

                            Script(scripts)

                            if late_exit == True:
                                exit = True

                        else:
                            error_msg = (
                                "No se reconoció la palabra "
                                + word
                                + ". Archivos múltiples se separan por comas"
                            )
                            estado = -1

                    word = ""

                # ------> AYUDA <--------

                elif estado == 121:

                    if word in tk_scolon:
                        Ayuda("")

                    else:
                        Ayuda(word)

                    word = ""
                    estado = 150

                # -----------------------

                elif estado == 150:

                    if char not in tk_scolon + tk_blank:
                        error_msg = "No se esperaba " + word
                        estado = -1

                    if late_exit == True:
                        exit = True

                if estado == -1:  # ERROR

                    Mensaje(error_msg)

                    if late_exit == True:
                        exit = True

                    err += 1

        except:
            pass

        estado, error_msg, lista_llaves = 0, "", []


#        ~~> AON <~~


def AON(string):  # PARSER, ARCHIVOS .AON
    word, palabras, llave = "", "", ""
    archivo, diccionario = [], {}
    accum = False

    estado, count = 0, 0
    try:
        for char in string:
            count += 1

            if (char not in tk_blank and char != "\n") or accum == True:

                if estado in [3] and accum == True:
                    word = word + char

                    if string[count] in ["]"]:
                        accum = False

                elif estado in [6] and accum == True:
                    if char not in tk_blank + ["\n"]:
                        word = word + char

                    if string[count] in [",", ">", " "] or char in tk_comilla:
                        accum = False

                elif estado in [9, 10] and accum == True:
                    word = word + char
                    if (
                        string[count] in tk_comilla + tk_blank
                        or char in tk_comilla + tk_blank
                    ):
                        accum = False

                if accum == False:

                    if estado == 0:

                        if char in tk_parA:
                            estado = 1

                        else:
                            estado = -1

                    elif estado == 1:

                        if char in tk_menorQ:
                            diccionario = {}
                            estado = 2

                        else:
                            estado = -1

                    elif estado == 2:

                        if char in tk_corchA:
                            accum = True
                            estado = 3

                        else:
                            estado = -1

                    elif estado == 3:

                        if Palabra(word):
                            llave = word.strip()
                            word = ""
                            estado = 4

                        else:
                            estado = -1

                    elif estado == 4:

                        if char in tk_corchB:
                            estado = 5

                        else:
                            estado = -1

                    elif estado == 5:

                        if char in tk_igual:
                            accum = True
                            estado = 6

                        else:
                            estado = -1

                    elif estado == 6:

                        if Numero(word.strip()):

                            valor = float(word)
                            diccionario[llave] = valor
                            word = ""
                            estado = 7

                        elif char in tk_comilla:

                            word = ""
                            accum = True
                            estado = 9

                        elif Booleano(word) in [True, False, None]:

                            valor = Booleano(word)
                            diccionario[llave] = valor
                            word = ""
                            estado = 8

                        else:
                            estado = -1

                    elif estado == 7:

                        if char in tk_coma:
                            estado = 2

                        elif char in tk_mayorQ:
                            archivo.append(diccionario)
                            estado = 12

                        else:
                            estado = -1

                    elif estado == 8:

                        if char in tk_coma:
                            estado = 2

                        elif char in tk_mayorQ:
                            archivo.append(diccionario)
                            estado = 12

                        else:
                            estado = -1

                    elif estado == 9:

                        if Palabra(word):
                            palabras = word
                            word = ""
                            accum = True
                            estado = 10

                        else:
                            estado = -1

                    elif estado == 10:

                        if char in tk_comilla:
                            valor = palabras
                            diccionario[llave] = valor
                            word, palabras = "", ""
                            estado = 11

                        elif Palabra(word) or word in tk_blank:
                            palabras = palabras + word
                            word = ""
                            accum = True
                            estado = 10

                        else:
                            estado = -1

                    elif estado == 11:

                        if char in tk_coma:
                            estado = 2

                        elif char in tk_mayorQ:
                            archivo.append(diccionario)
                            estado = 12

                        else:
                            estado = -1

                    elif estado == 12:

                        if char in tk_coma:
                            estado = 1

                        elif char in tk_parB:
                            estado = 13

                        else:
                            estado = -1

                    if estado == 13:
                        return archivo

                    if estado == -1:
                        err += 1

    except:

        Mensaje("El archivo no es un archivo AON válido")


#        ~~> Archivo AON <~~


def ArchivoAON(word):

    estado, count = 0, 0

    for char in word:
        count += 1

        if estado == 0:

            if char in tk_letra + tk_digito:
                estado = 1

        elif estado == 1:

            if char in tk_letra + tk_digito:
                estado = 1

            elif char in tk_punto:
                estado = 2

            else:
                return False

        elif estado == 2:

            if char == "a":
                estado = 3

            else:
                return False

        elif estado == 3:

            if char == "o":
                estado = 4

            else:
                return False

        elif estado == 4:

            if char == "n" and count == len(word):
                return True

            else:
                return False


#        ~~> Archivo SIQL <~~


def ArchivoSIQL(word):
    estado, count = 0, 0

    for char in word:
        count += 1

        if estado == 0:

            if char in tk_letra + tk_digito:
                estado = 1

        elif estado == 1:

            if char in tk_letra + tk_digito:
                estado = 1

            elif char in tk_punto:
                estado = 2

            else:
                return False

        elif estado == 2:

            if char == "s":
                estado = 3

            else:
                return False

        elif estado == 3:

            if char == "i":
                estado = 4

            else:
                return False

        elif estado == 4:

            if char == "q":
                estado = 5

            else:
                return False

        elif estado == 5:

            if char == "l" and count == len(word):
                estado = 5
                return True

            else:
                return False


#        ~~> Palabra <~~


def Palabra(word):

    if word in reserved:
        Mensaje("'" + word + "' es una palabra reservada")
        return False

    estado = 0

    for char in word:

        if estado == 0:

            if char in tk_texto:
                estado = 1

            else:
                return False

        elif estado == 1:

            if char in tk_texto:
                estado = 1

            else:
                return False

    return True


#        ~~> Numero <~~


def Numero(word):
    estado = 0

    for char in str(word):

        if estado == 0:

            if char in tk_guion:
                estado = 1

            elif char in tk_digito:
                estado = 2

            else:
                return False

        elif estado == 1:

            if char in tk_digito:
                estado = 2

            else:
                return False

        elif estado == 2:

            if char in tk_digito:
                estado = 2

            elif char in tk_punto:
                estado = 3

            else:
                return False

        elif estado == 3:

            if char in tk_digito:
                estado = 4

            else:
                return False

        elif estado == 4:

            if char in tk_digito:
                estado = 4

    return True


#        ~~> Booleano <~~


def Booleano(word):
    estado, count = 0, 0

    for char in word:
        count += 1

        if estado == 0:

            if char == "t":
                estado = 1

            elif char == "f":
                estado = 5

            else:
                return None

        elif estado == 1:

            if char == "r":
                estado = 2

            else:
                return None

        elif estado == 2:

            if char == "u":
                estado = 3

            else:
                return None

        elif estado == 3:

            if char == "e" and count == len(word):
                return True

            else:
                return None

        elif estado == 5:

            if char == "a":
                estado = 6

            else:
                return None

        elif estado == 6:

            if char == "l":
                estado = 7

            else:
                return None

        elif estado == 7:

            if char == "s":
                estado = 8

            else:
                return None

        elif estado == 8:

            if char == "e" and count == len(word):
                return False

            else:
                return None


#        ~~> Condicion <~~


def Condicion(string):
    estado = 0

    for char in string:

        if char != " " and char != "/n":

            if estado == 0:

                if char in tk_letra:
                    estado = 1

                else:
                    return False

            elif estado == 1:

                if char in tk_texto:
                    estado = 1

                elif char in tk_igual:
                    estado = 2

                else:
                    return False

            elif estado == 2:

                if char in tk_comilla:
                    estado = 3

                elif char in tk_digito:
                    estado = 4

                elif char in tk_letra:
                    estado = 9999

            elif estado == 3:

                if char in tk_letra:
                    estado = 3

                elif char in tk_comilla:
                    estado = "gg"

    return True


#        ~~> RegEx <~~


def RegEx(string):
    estado = 0

    for char in string:

        if estado == 0:

            if char in tk_letra:
                estado = 1

        elif estado == 1:

            if char in tk_letra:
                estado = 1

            else:
                return False

    return True


# EJECUCIÓN

SimpleSQL("")
