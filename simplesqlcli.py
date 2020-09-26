import json, webbrowser

# Inicializando

Cbegin = "\33[37m"
Cend = "\33[0m"

set_names = []
set_files = []
selected_set = []

# Tokens

tk_help = ["help", "ayuda"]
tk_close = ["close", "exit", "cerrar", "salir"]

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
tk_guion = ["-"]
tk_comilla = ['"', "'"]

tk_letra = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚÀÈÌÒÙÄËÏÖÜÂÊÎÔÛáéíóúàèìòùäëïöüâêîôû^~|¡!#$%&/¿?-_"
tk_digito = "1234567890.-"
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
)

# Comandos


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
        print("\33[45m" + "=================================================" + Cend)
        print("No se reconoció el comando " + word)
        print("\33[45m" + "=================================================" + Cend)


def Create(nombre):
    set_names.append(nombre)
    set_names.append([])


def Load(nombre, archivos):

    selected_set = set_files[set_names.index(nombre)]

    for archivo in archivos:

        try:
            archivo.strip()
            temp = open(archivo, "r")
            selected_set.append(temp.read())

            print(Cbegin + "Se cargó '" + archivo + "'." + Cend)

        except:
            print(Cbegin + "No se encontró '" + archivo + "'." + Cend)


def Use(nombre):
    global selected_set

    i = 0
    for set_name in set_names:
        if set_name == nombre:
            selected_set = set_files[i]

        i += 1


def Select(lista):

    words = " ".join(lista)
    seleccionar_todo = False

    if (
        "donde" in words and lista[-1].strip() != "donde"
    ):  # Separa si se usa una condición o no

        list = words.split("donde ")  # Separando la seleccion de la condición

        # PARAMETROS

        parametros = list[0]
        if parametros.strip() == "*":
            seleccionar_todo = True
        else:
            if "," in parametros:
                txt = "".join(parametros)
                parametros = txt.split(",")
            else:
                parametros = [parametros.strip()]

        # CONDICION
        condicion = list[1].split("=")
        try:
            key = condicion[0].strip()
            value = condicion[1].strip()

            if (value[0] == '"' and value[-1] == '"') or (
                value[0] == "'" and value[-1] == "'"
            ):
                value = value[1:-1]
            else:
                if "." in value:
                    value = float(value)
                else:
                    if ("True" in value or "False" in value) or (
                        "true" in value or "false" in value
                    ):
                        value = bool(value)
                    else:
                        value = int(value)

        except:
            print("Sintaxis errónea. [ parametro = condicion ]")

        # SELECCION

        try:
            num_registro = 0
            for registro in registros:  # Iterando sobre todos los archivos cargados

                num_diccionario = 0
                for (
                    diccionario
                ) in registro:  # Iterando sobre cada diccionario de cada registro

                    if (
                        key in diccionario and diccionario[key] == value
                    ):  # Validando que la condicion se cumpla

                        if seleccionar_todo == True:

                            for key1 in diccionario:

                                selec = [num_registro, num_diccionario, key1]
                                if selec not in seleccion:
                                    seleccion.append(selec)

                        else:
                            for parametro in parametros:

                                if parametro in diccionario:

                                    # registro     #diccionario  parametro guardado
                                    selec = [num_registro, num_diccionario, parametro]
                                    if selec not in seleccion:
                                        seleccion.append(selec)

                    num_diccionario += 1
                num_registro += 1

            if len(seleccion) == 0:
                print("No se seleccionó ninguna llave.")
            else:
                print("Hay " + str(len(seleccion)) + " llaves seleccionadas.")
            seleccionar_todo = False

        except:
            if len(registros) == 0:
                print("No se han cargado archivos")
            else:
                print(
                    "Sintaxis erronea para 'seleccionar'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

    elif "donde" not in words:

        # PARAMETROS

        parametros = "".join(lista)

        if parametros.strip() == "*":
            seleccionar_todo = True
        else:
            if "," in parametros:
                txt = "".join(parametros)
                parametros = txt.split(",")
            else:
                parametros = [parametros.strip()]

        # SELECCION

        try:
            num_registro = 0
            for registro in registros:  # Iterando sobre todos los archivos cargados

                num_diccionario = 0
                for (
                    diccionario
                ) in registro:  # Iterando sobre cada diccionario de cada registro

                    if seleccionar_todo == True:

                        for key1 in diccionario:
                            selec = [num_registro, num_diccionario, key1]
                            if selec not in seleccion:
                                seleccion.append(selec)

                    else:

                        for parametro in parametros:

                            if parametro in diccionario:

                                # registro     #diccionario  parametro guardado
                                selec = [num_registro, num_diccionario, parametro]
                                if selec not in seleccion:
                                    seleccion.append(selec)

                    num_diccionario += 1
                num_registro += 1

            if len(seleccion) == 0:
                print("No se seleccionó ninguna llave.")
            else:
                print("Hay " + str(len(seleccion)) + " llaves seleccionadas.")
            seleccionar_todo = False

        except:
            if len(registros) == 0:
                print("No se han cargado archivos")
            else:
                print(
                    "Sintaxis erronea para 'seleccionar'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

    else:
        print(
            "Sintaxis errónea para 'seleccionar'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
        )


def List():
    print("el")


def Print(color):
    global Cbegin

    if color == "blue" or color == "azul":
        Cbegin = "\33[34m"

    elif color == "red" or color == "rojo":
        Cbegin = "\33[31m"

    elif color == "green" or color == "verde":
        Cbegin = "\33[32m"

    elif color == "yellow" or color == "amarillo":
        Cbegin = "\33[33m"

    elif color == "orange" or color == "naranja":
        Cbegin = "\033[33m"

    elif color == "pink" or color == "rosa":
        Cbegin = "\033[95m"


def Max(key):

    if len(registros) > 0:
        try:
            if registros[0][0][key] == True or registros[0][0][key] == False:
                err += 1

            if "." in str(registros[0][0][key]):
                valor_maximo = float(registros[0][0][key])
            else:
                valor_maximo = int(registros[0][0][key])

            for registro in registros:
                for diccionario in registro:
                    if key in diccionario:
                        if diccionario[key] > valor_maximo:
                            valor_maximo = diccionario[key]

            print(valor_maximo)
        except:
            print("'" + key + "' no es una variable numérica")

    else:
        print("No se han cargado archivos")


def Min(key):

    if len(registros) > 0:
        try:
            if registros[0][0][key] == True or registros[0][0][key] == False:
                err += 1

            if "." in str(registros[0][0][key]):
                valor_minimo = float(registros[0][0][key])
            else:
                valor_minimo = int(registros[0][0][key])

            for registro in registros:
                for diccionario in registro:
                    if key in diccionario:
                        if diccionario[key] < valor_minimo:
                            valor_minimo = diccionario[key]

            print(valor_minimo)
        except:
            print("'" + key + "' no es una variable numérica")

    else:
        print("No se han cargado archivos")


def Sum(key):

    if len(registros) > 0:
        try:
            if registros[0][0][key] == True or registros[0][0][key] == False:
                err += 1

            suma_total = 0

            for registro in registros:
                for diccionario in registro:
                    suma_total += diccionario[key]

            print(suma_total)
        except:
            print("'" + key + "' no es una variable numérica")

    else:
        print("No se han cargado archivos")


def Count():

    if len(registros) > 0:
        print("Se han cargado " + str(len(registros)) + " archivos")
    else:
        print("No se han cargado archivos")


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


def Script():
    print("el")


# ================> AFD <====================


#        ~~> SimpleSQL CLI <~~


def SimpleSQL():
    exit = False
    estado = 0
    error_msg = ""

    while exit == False:
        query = input(">>")
        query = query.lower().split(" ") + [";"]
        print(query)

        try:
            for word in query:
                print(word, estado)

                if word != "" and word != "\n":

                    if estado == 0:  # INICIO

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
                            exit = True

                        else:

                            if word != ";":
                                error_msg = ""
                                error_msg = "No se reconoció la palabra " + word
                                estado = -1

                    # ------> CREATE <--------

                    elif estado == 1:

                        if word in tk_set:
                            estado = 2

                        else:

                            if word == ";":
                                error_msg = "Se esperaba 'set'"

                            else:
                                error_msg = "No se reconoció la palabra " + word

                            estado = -1

                    elif estado == 2:

                        if Palabra(word):
                            Create(word)
                            estado = 150

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un nombre para el set"

                            else:
                                error_msg = "Nombre de set no válido"

                            estado = -1

                    # ------> LOAD <--------

                    elif estado == 11:

                        if word in tk_into:
                            estado = 12

                        else:

                            if word == ";":
                                error_msg = "Se esperaba 'into'"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'into'"
                                )

                            estado = -1

                    elif estado == 12:

                        if word in set_names:
                            nombre_set = word
                            archivos_set = []

                            estado = 13

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un set"

                            else:
                                error_msg = "No existe el set " + word

                            estado = -1

                    elif estado == 13:

                        if word in tk_files:
                            estado = 14

                        else:

                            if word == ";":
                                error_msg = "Se esperaba 'files'"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'files'"
                                )

                            estado = -1

                    elif estado == 14:

                        if ArchivoAON(word):
                            archivos_set.append(word)
                            estado = 15

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un archivo AON"

                            else:
                                error_msg = word + " no es un archivo AON"

                            estado = -1

                    elif estado == 15:

                        if word == ",":
                            estado = 14

                        else:

                            if word == ";":
                                # load()
                                print("el")

                            else:
                                error_msg = "No se reconoció la palabra " + word + ""

                            estado = -1

                    # ------> USE <--------

                    elif estado == 21:

                        if word in tk_set:
                            estado = 22

                        else:

                            if word == ";":
                                error_msg = "Se esperaba 'set'"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'set'"
                                )

                            estado = -1

                    elif estado == 22:

                        if word in sets:
                            # use()
                            estado = 150

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un set"

                            else:
                                error_msg = "No existe el set " + word

                            estado = -1

                    # ------> SELECT <--------

                    elif estado == 31:

                        print(Palabra(word))
                        if word == "*":
                            estado = 32

                        elif Palabra(word):
                            estado = 33

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = "No se reconoció la palabra " + word + "."

                                estado = -1

                    elif estado == 32:

                        if word in tk_where:
                            estado = 35

                        else:

                            if word == ";":
                                # select()
                                print("el")

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'where'"
                                )

                                estado = -1

                    elif estado == 33:

                        if word == ",":
                            estado = 34

                        elif word in tk_where:
                            estado = 35

                        else:

                            if word == ";":
                                # select()
                                print("el")

                            else:
                                error_msg = "No se reconoció la palabra " + word

                            estado = -1

                    elif estado == 34:

                        if Palabra(word):
                            estado = 33

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            estado = -1

                    elif estado == 35:

                        if Palabra(word):
                            estado = 33

                        else:
                            if word == ";":
                                error_msg = "Se esperaba una condición"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba una condición"
                                )

                            estado = -1

                    elif estado == 36:

                        if Palabra(word):
                            estado = 33

                        else:
                            if word == ";":
                                error_msg = "Se esperaba una condición"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba una condición"
                                )

                            estado = -1

                    # ------> LIST <--------

                    elif estado == 41:

                        if word in tk_atributes:
                            # list()
                            estado = 150

                        else:

                            if word == ";":
                                error_msg = "Se esperaba 'atributes'"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'atributes'"
                                )

                            estado = -1

                    # ------> PRINT <--------

                    elif estado == 51:

                        if word in tk_in:
                            estado = 52

                        else:
                            if word == ";":
                                error_msg = "Se esperaba 'in'"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba 'in'"
                                )

                            estado = -1

                    elif estado == 52:

                        if word in tk_color:
                            Print(word)
                            estado = 150

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un color"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un color"
                                )

                            estado = -1

                    # ------> MAX <--------

                    elif estado == 61:

                        if Palabra(word):
                            # max()
                            estado = 150

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            estado = -1

                    # ------> MIN <--------

                    elif estado == 71:

                        if Palabra(word):
                            # min()
                            estado = 150

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            estado = -1

                    # ------> SUM <--------

                    elif estado == 81:

                        if Palabra(word):
                            estado = 82

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            estado = -1

                    elif estado == 82:

                        if word == ",":
                            estado = 81

                        else:

                            if word == ";":
                                # sum()
                                print("el")

                            else:
                                error_msg = "No se reconoció la palabra " + word

                                estado = -1

                    # ------> COUNT <--------

                    elif estado == 91:

                        if word == "*":
                            estado = 92

                        elif Palabra(word):
                            estado = 93

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un atributo"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            estado = -1

                    elif estado == 92:

                        if word == ";":
                            estado = 92

                        else:
                            error_msg = "No se reconoció la palabra "
                            estado = -1

                    elif estado == 93:

                        if word == ",":
                            estado = 94

                        else:
                            if word == ";":
                                # count()
                                print("el")

                            else:
                                error_msg = "No se reconoció la palabra " + word

                                estado = -1

                    elif estado == 94:

                        if Palabra(word):
                            estado = 93

                        else:

                            if word == ";":
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un atributo"
                                )

                            else:
                                error_msg = "No se reconoció la palabra " + word

                            estado = -1

                    # ------> REPORTE <--------

                    elif estado == 101:

                        if word in tk_to:
                            estado = 102

                        elif word in tk_tokens:
                            estado = 150
                            # report_tokens()

                        else:
                            if word == ";":
                                error_msg = "Se esperaba to|tokens"

                            else:

                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba to|tokens"
                                )

                            estado = -1

                    elif estado == 102:

                        if Palabra(word):
                            estado = 103

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un nombre"

                            else:
                                error_msg = word + " no es un nombre válido"

                            estado = -1

                    elif estado == 103:

                        if word:  # is comando
                            # report_comando()
                            estado = 150

                        else:

                            if word == ";":
                                error_msg = "Se esperaba un comando"

                            else:
                                error_msg = word + " no es comando válido"

                            estado = -1

                    # ------> SCRIPT <--------

                    elif estado == 111:

                        if ArchivoSIQL(word):
                            estado = 112

                        else:
                            if word == ";":
                                error_msg = "Se esperaba un archivo SIQL"

                            else:
                                error_msg = (
                                    "No se reconoció la palabra "
                                    + word
                                    + ". Se esperaba un archivo SIQL"
                                )

                            estado = -1

                    elif estado == 112:

                        if word == ",":
                            estado = 111

                        else:

                            if word == ";":
                                # script()
                                print("el")

                            else:

                                error_msg = "No se reconoció la palabra "

                            estado = -1

                    # ------> AYUDA <--------

                    elif estado == 121:

                        if word == ";":
                            Ayuda("")

                        else:
                            Ayuda(word)

                        estado = 150

                    # -----------------------

                    elif estado == 150:

                        if word == ";":
                            print("LA CADENA ES VÁLIDA")
                        else:
                            error_msg = "No se esperaba " + word
                            estado = -1

                    if estado == -1:  # ERROR

                        print(
                            "\33[45m"
                            + "================================================="
                            + Cend
                        )
                        print(Cbegin+error_msg+Cend)
                        print(
                            "\33[45m"
                            + "================================================="
                            + Cend
                        )

                        estado = 0
                        err += 1

        except:
            print("error :(")

        estado = 0


#        ~~> AON <~~


def AON(word):  # PARSER, ARCHIVOS .AON
    estado = 0
    palabra = ""

    try:
        for char in word:

            if char != " " and char != "\n":

                if estado == 0:

                    if char in tk_parA:
                        estado = 1

                    else:
                        estado = -1

                elif estado == 1:

                    if char in tk_menorQ:
                        estado = 2

                    else:
                        estado = -1

                elif estado == 2:

                    if char in tk_corchA:
                        estado = 3

                    else:
                        estado = -1

                elif estado == 3:

                    if char in tk_letra:
                        estado = 4

                        palabra = palabra + char
                    else:
                        estado = -1

                elif estado == 4:

                    if char in tk_letra:
                        estado = 4
                        palabra = palabra + char

                    elif char in tk_corchB:
                        palabra = ""
                        estado = 5

                    else:
                        estado = -1

                elif estado == 5:

                    if char in tk_igual:
                        estado = 6

                    else:
                        estado = -1

                elif estado == 6:

                    if char in tk_digito:
                        estado = 7
                        palabra = palabra + char

                    elif char in tk_comilla:
                        estado = 8

                    elif char in tk_letra:
                        estado = 11
                        palabra = palabra + char

                    else:
                        estado = -1

                elif estado == 7:

                    if char in tk_digito:
                        estado = 7
                        palabra = palabra + char

                    elif char in tk_coma:
                        palabra = ""

                        estado = 10
                    elif char in tk_mayorQ:
                        palabra = ""

                        estado = 12
                    else:
                        estado = -1

                elif estado == 8:

                    if char in tk_texto:
                        estado = 8
                        palabra = palabra + char

                    elif char in tk_comilla:
                        palabra = ""

                        estado = 9
                    else:
                        estado = -1

                elif estado == 9:

                    if char in tk_coma:
                        estado = 10

                    elif char in tk_mayorQ:
                        estado = 12

                    else:
                        estado = -1

                elif estado == 10:

                    if char in tk_corchA:
                        estado = 3

                    else:
                        estado = -1

                elif estado == 11:

                    if char in tk_letra:
                        estado = 11
                        palabra = palabra + char

                    elif char in tk_coma:

                        if palabra.lower() != "true" and palabra.lower() != "false":
                            print(
                                Cbegin
                                + "'"
                                + palabra
                                + "' no es un atributo boolean"
                                + Cend
                            )
                            estado = -1

                        else:
                            palabra = ""

                        estado = 10

                    elif char in tk_mayorQ:

                        if palabra.lower() != "true" and palabra.lower() != "false":
                            print(
                                Cbegin
                                + "'"
                                + palabra
                                + "' no es un atributo boolean"
                                + Cend
                            )
                            estado = -1

                        else:
                            palabra = ""

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

                elif estado == 13:
                    print("el")

                if estado == -1:
                    print(Cbegin + "La cadena no es válida. '" + char + "'" + Cend)
                    err += 1

    except:
        print(
            Cbegin
            + """
        La cadena:

            """
            + word
            + """

        es INVALIDA"""
            + Cend
        )


#        ~~> Archivo AON <~~


def ArchivoAON(word):
    estado, count = 0, 0

    for char in word:
        count += 1

        if estado == 0:

            if char in tk_letra:
                estado = 1

        elif estado == 1:

            if char in tk_letra:
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

            if char == "n " and count == len(word):
                return True

            else:
                return False


#        ~~> Numero <~~


def Numero(word):
    estado = 0

    for char in word:

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


#        ~~> Palabra <~~


def Palabra(word):

    if word in reserved:
        print(Cbegin + "'" + word + "' es una palabra reservada" + Cend)
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


#        ~~> Archivo SIQL <~~


def ArchivoSIQL(word):
    estado, count = 0, 0

    for char in word:
        count += 1

        if estado == 0:

            if char in tk_letra:
                estado = 1

        elif estado == 1:

            if char in tk_letra:
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

SimpleSQL()
