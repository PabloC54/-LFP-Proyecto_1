import json
import webbrowser


# Inicializando

exit = False
registros = []
seleccion = []


# Diccionario

salir = ["salir", "out", "exit", "close"]

reservado = [
    "ayuda",
    "cargar",
    "seleccionar",
    "maximo",
    "minimo",
    "suma",
    "cuenta",
    "reportar",
    "donde",
]


# Definición de los comandos


def ayuda():
    print(
        """
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
    )


def cargar(archivos):
    txt = "".join(archivos)
    archivos = txt.split(",")

    for archivo in archivos:
        try:
            archivo.strip()

            reg = open(archivo, "r")
            reg = json.load(reg)
            registros.append(reg)

            print("Se cargó '" + archivo + "'.")

        except:
            print("No se encontró '" + archivo + "'.")


def seleccionar(lista):

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


def maximo(key):

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


def minimo(key):

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


def suma(key):

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


def cuenta():

    if len(registros) > 0:
        print("Se han cargado " + str(len(registros)) + " archivos")
    else:
        print("No se han cargado archivos")


def reportar(num):

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


# SimpleSQL
while exit == False:
    query = input("=>")
    query = query.lower()
    words = query.split(" ")

    if words[0] in reservado:  # Verificando el comando
        comando = words[0]

        if comando == "ayuda":
            ayuda()

        if comando == "cargar":
            cargar(words[1:])

        if comando == "seleccionar":
            seleccionar(words[1:])

        if comando == "maximo":
            if len(words) == 2:
                maximo(words[1].strip())
            else:
                print(
                    "Sintaxis errónea para 'maximo'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

        if comando == "minimo":
            if len(words) == 2:
                minimo(words[1].strip())
            else:
                print(
                    "Sintaxis errónea para 'minimo'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

        if comando == "suma":
            if len(words) == 2:
                suma(words[1].strip())
            else:
                print(
                    "Sintaxis errónea para 'suma'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

        if comando == "cuenta":
            if len(words) == 1:
                cuenta()
            else:
                print(
                    "Sintaxis errónea para 'cuenta'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

        if comando == "reportar":
            if len(words) == 2:
                if int(words[1]) > 0:
                    reportar(int(words[1]))
                else:
                    print("'" + words[1] + "' no es un número válido")

            else:
                print(
                    "Sintaxis errónea para 'reportar'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
                )

    elif words[0].lower() in salir:  # Salir del programa
        print("Saliendo.. ")
        exit = True
    elif words[0] == "":  # Sentencia vacía
        pass
    else:  # Sentencia errónea
        print(
            "No se reconoció el comando: '"
            + words[0]
            + "'. Consulte 'ayuda' para ver los comandos de SimpleSQL"
        )
