import traceback
import webbrowser


# ================> INICIALIZANDO <====================

Cbegin = "\x1b[0;37;40m"
Cend = "\x1b[0m"
Hcolor = "\x1b[1;30;47m"
reporte, nombre_reporte = False, ""


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

dict_tokens = {
    'tk_reservado': ["Se trata de palabras reservadas por SimpleSQL CLI", []],
    'tk_operador': ["Se trata de operadores lógicos usados para la conjunción de comparaciones", []],
    'tk_archivo': ["Se trata de palabras reconocidas como archivos", []],
    'tk_parA': ["Se trata de la apertura de un paréntesis", []],
    'tk_parB': ["Se trata del cierre de un paréntesis", []],
    'tk_menorQ': ["Se trata de un signo 'menor', usado en la apertura de archivos AON", []],
    'tk_mayorQ': ["Se trata de un signo 'mayor', usado en el cierre de archivos AON", []],
    'tk_corchA': ["Se trata de la apertura de un corchete", []],
    'tk_corchB': ["Se trata del cierre de un corchete", []],
    'tk_igual': ["Se trata del signo 'igual', usado en la igualación de valores", []],
    'tk_coma': ["Se trata del signo 'coma', usado en la selección de múltiples objetivos", []],
    'tk_punto': ["Se trata del signo 'punto', usado en la representación de números con decimal", []],
    'tk_scolon': ["Se trata del signo 'punto y coma' usado en la finalización de un comando", []],
    'tk_guion': ["Se trata del signo 'guion' usado en la representación de números negativos", []],
    'tk_asterisco': ["Se trata del signo 'asterisco' usado en la selección de todos los objetivos", []],
    'tk_comilla': ["Se trata del signo 'comilla' usado en la representación de variables string", []],
    'tk_numero': ["Se trata de cualquier número", []],
    'tk_cadena': ["Se trata de cualquier variable string", []],
    'tk_booleano': ["Se trata de una variable que acoge valores booleanos", []],
    'tk_color': ["Se trata de una palabra que representa un color", []]
}


# ================> AFD AUXILIARES <====================


def AON(string):  # PARSER, ARCHIVOS .AON
    word, palabras, llave = "", "", ""
    archivo, diccionario = [], {}
    accum = False

    estado, count = 0, 0

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
                        dict_tokens["tk_parA"][1].append(char)
                        estado = 1

                    else:
                        estado = -1

                elif estado == 1:

                    if char in tk_menorQ:
                        dict_tokens["tk_menorQ"][1].append(char)
                        diccionario = {}
                        estado = 2

                    else:
                        estado = -1

                elif estado == 2:

                    if char in tk_corchA:
                        dict_tokens["tk_corchA"][1].append(char)
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
                        dict_tokens["tk_corchB"][1].append(char)
                        estado = 5

                    else:
                        estado = -1

                elif estado == 5:

                    if char in tk_igual:
                        dict_tokens["tk_igual"][1].append(char)
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
                        dict_tokens["tk_comilla"][1].append(char)

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
                        dict_tokens["tk_coma"][1].append(char)
                        estado = 2

                    elif char in tk_mayorQ:
                        dict_tokens["tk_mayorQ"][1].append(char)
                        archivo.append(diccionario)
                        estado = 12

                    else:
                        estado = -1

                elif estado == 8:

                    if char in tk_coma:
                        dict_tokens["tk_coma"][1].append(char)
                        estado = 2

                    elif char in tk_mayorQ:
                        dict_tokens["tk_mayorQ"][1].append(char)
                        archivo.append(diccionario)
                        estado = 12

                    else:
                        estado = -1

                elif estado == 9:

                    if Palabra(word):
                        dict_tokens["tk_cadena"][1].append(char)
                        palabras = word
                        word = ""
                        accum = True
                        estado = 10

                    else:
                        estado = -1

                elif estado == 10:

                    if char in tk_comilla:
                        dict_tokens["tk_comilla"][1].append(char)
                        valor = palabras
                        diccionario[llave] = valor
                        word, palabras = "", ""
                        estado = 11

                    elif Palabra(word) or word in tk_blank:
                        dict_tokens["tk_cadena"][1].append(char)
                        palabras = palabras + word
                        word = ""
                        accum = True
                        estado = 10

                    else:
                        estado = -1

                elif estado == 11:

                    if char in tk_coma:
                        dict_tokens["tk_coma"][1].append(char)
                        estado = 2

                    elif char in tk_mayorQ:
                        dict_tokens["tk_mayorQ"][1].append(char)
                        archivo.append(diccionario)
                        estado = 12

                    else:
                        estado = -1

                elif estado == 12:

                    if char in tk_coma:
                        dict_tokens["tk_coma"][1].append(char)
                        estado = 1

                    elif char in tk_parB:
                        dict_tokens["tk_parB"][1].append(char)
                        estado = 13

                    else:
                        estado = -1

                if estado == 13:
                    return archivo

                if estado == -1:
                    Mensaje("El archivo no es un archivo AON válido")
                    estado = -2


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


def Numero(word):
    estado = 0

    for char in str(word):

        if estado == 0:

            if char in tk_guion:
                dict_tokens["tk_guion"][1].append(char)
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

            else:
                return False

    dict_tokens["tk_numero"][1].append(word)
    return True


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
                dict_tokens["tk_booleano"][1].append(word)
                return False

            else:
                return None


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


# ================> COMANDOS <====================


def Mensaje(texto):

    if texto:
        print(
            "\n\x1b[0;30;41m"
            + " >>>>>>>>>>>> "
            + Cend
            + "  "
            + Cbegin
            + texto
            + Cend
            + "  \x1b[0;30;41m"
            + " <<<<<<<<<<<< "
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
    selected_set = set_files[set_names.index(nombre)]


def Select(lista_llaves, condicion, conjuncion):
    
    global selected_set
    lista_tuplas, lista_final = [], []
    diccionario_prueba = {}
    condicion_llave, condicion_operador, condicion_valor = "", "", ""

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

                elif condicion_valor != None:
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

                        if reporte:

                            tupla = []
                            for llave in lista_llaves:
                                tupla.append(diccionario[llave])

                        else:

                            tupla = "    ||  "
                            for llave in lista_llaves:

                                tupla = tupla + \
                                    str(diccionario[llave]) + "  ||  "

                        tuplas.append(tupla)

            lista_tuplas.append(tuplas)

        if len(lista_tuplas) >= 2:

            if conjuncion in tk_and:
                dict_tokens["tk_operador"][1].append(conjuncion)

                for tupla in lista_tuplas[0]:

                    if tupla in lista_tuplas[1]:
                        lista_final.append(tupla)

            elif conjuncion in tk_or:
                dict_tokens["tk_operador"][1].append(conjuncion)

                lista_final = lista_tuplas[0]
                for tupla in lista_tuplas[1]:

                    if tupla not in lista_final:
                        lista_final.append(tupla)

            elif conjuncion in tk_xor:
                dict_tokens["tk_operador"][1].append(conjuncion)

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

        if reporte:
            Report(lista_llaves, lista_final)

        else:

            header = "    ||    "  # ENCABEZADO
            for llave in lista_llaves:
                header = header + llave + "    ||    "
            print("\n"+Hcolor + header + "\n" + "=" * len(header) + Cend+"\n")

            if lista_final:  # CUERPO
                for tupla in lista_final:
                    print(Cbegin + tupla + Cend)
                print("\n"+Hcolor + "=" * len(header) + Cend+"\n")

            else:
                print(Cbegin+" ~ " * (len(header)//3) + Cend)
                print("\n"+Hcolor + "=" * len(header) + Cend+"\n")

    except:
        pass


def List():

    if selected_set:
        diccionario_muestra = selected_set[0][0]

        if reporte:
            Report("Atributos", diccionario_muestra.keys())

        else:
            print("\n"+Hcolor + "   Atributos   \n" + "=" * 15 + Cend+"\n")

            if diccionario_muestra:
                for atributo in diccionario_muestra:
                    print(Cbegin+"  || "+atributo+"  ||  "+Cend)

            else:
                print(Cbegin+" ~ " * 5+Cend)

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

        if reporte:
            Report(llave, [str(valor_maximo)])

        else:
            print("\n", Cbegin + str(valor_maximo) + Cend, "\n")

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

        if reporte:
            Report(llave, [str(valor_minimo)])

        else:
            print("\n", Cbegin + str(valor_minimo) + Cend, "\n")

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

                lista_sumas.append(str(suma))

            else:
                lista_sumas.append("NO_NUM")

        if reporte:
            Report(lista_llaves, [lista_sumas])

        else:
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

        lista_cuentas.append(str(cuenta))

    if reporte:
        Report(lista_llaves, [lista_cuentas])

    else:

        header = "  ||  "  # ENCABEZADO
        for llave in lista_llaves:
            header = header + llave + "  ||  "
        print("\n"+Hcolor + header + "\n" + "=" * len(header) + Cend+"\n")

        fila = Cbegin+"    ||  "  # SUMAS
        for cuenta in lista_cuentas:
            fila = fila + \
                str(cuenta) + "  ||  "

        print(fila+Cend+"\n\n"+Hcolor + "=" * len(header) + Cend+"\n")


def Report(lista_llaves, lista_tuplas):

    html_file = open(nombre_reporte+".html", "w")

    html_file.write(  # ENCABEZADO
        "<!DOCTYPE html>\n"
        + "<html>\n"
        + "    <head>\n"
        + "        <title>Reporte</title>\n"

        + "    <link rel='stylesheet' type='text/css' href='style.css'/>\n"
        + "    </head>\n"
        + "    <body>\n"
    )

    html_file.write("        <table class='container'>\n")  # TABLA
    html_file.write("            <thead>\n")  # ENCABEZADO DE LA TABLA

    html_file.write("                <tr>\n")

    if isinstance(lista_llaves, str):
        html_file.write(
            "                    <th><h1>{}</h1></th>\n".format(lista_llaves))

    else:
        for llave in lista_llaves:
            html_file.write(
                "                    <th><h1>{}</h1></th>\n".format(llave))

    html_file.write("                </tr>\n")
    html_file.write("            </thead>\n\n")

    html_file.write("            <tbody>\n")  # CUERPO DE LA TABLA
    for tupla in lista_tuplas:

        html_file.write("                <tr>\n")

        if isinstance(tupla, str):
            html_file.write("                    <td>{}</td>\n".format(tupla))

        else:
            for atributo in tupla:
                html_file.write(
                    "                    <td>{}</td>\n".format(atributo))

        html_file.write("                </tr>\n\n")

    html_file.write("            </tbody>\n        </table>\n" +
                    "    </body>\n" + "</html>")

    webbrowser.open(nombre_reporte+".html")  # Abrir el archivo HTML


def Script(scripts):

    for archivo in scripts:

        try:
            temp = open(archivo, "r")

            for Instruccion in temp:
                SimpleSQL(Instruccion)

            temp.close()

        except Exception:
            Mensaje("No se encontró el archivo " + archivo)
            traceback.print_exc()


# ================> SIMPLESQL CLI <====================


def SimpleSQL(Instruccion):
    global reporte, nombre_reporte, tk_tokens
    exit, late_exit, coma, comilla = False, False, False, False
    estado = 0
    error_msg, nombre_set, conjuncion = "", "", ""
    lista_llaves, archivos_set, condicion, scripts = [], [], [], []

    while exit == False:

        if Instruccion:
            query = Instruccion.strip() + " "

            for char in query:
                if char in tk_comilla:
                    if comilla==True:
                        comilla==False
                    else:
                        comilla==True

                if comilla==False:
                    char.lower()

            print(Hcolor+" >> "+Cend+" "+Cbegin+query+Cend)
            word, Instruccion = "", ""
            late_exit = True

        else:
            query = input(Hcolor+" >> "+Cend+" " +
                          Cbegin).strip().lower() + " ; "+Cend
            word = ""
            

        for char in query:

            if char in tk_comilla:
                dict_tokens["tk_comilla"][1].append(char)
                if comilla:
                    comilla = False

                else:
                    comilla = True

            if char in tk_coma and comilla == False:
                dict_tokens["tk_coma"][1].append(char)
                coma = True

            if char not in tk_blank + tk_coma or comilla == True:

                if comilla != True:
                    char.lower()

                word = word + char

            elif estado == 0:  # INICIO

                if word in tk_create and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 1

                elif word in tk_load and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 11

                elif word in tk_use and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 21

                elif word in tk_select:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 31

                elif word in tk_list:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 41

                elif word in tk_print and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 51

                elif word in tk_max:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 61

                elif word in tk_min:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 71

                elif word in tk_sum:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 81

                elif word in tk_count:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 91

                elif word in tk_report and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 101

                elif word in tk_script and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 111

                elif word in tk_help and reporte == False:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 121

                elif word in tk_close:
                    dict_tokens["tk_reservado"][1].append(word)
                    print(Cbegin+".."+Cend)
                    exit = True

                else:

                    if reporte == True:
                        error_msg = "No se puede reportar el comando '"+word+"'"

                    elif word != ";":
                        error_msg = "No se reconoció la palabra " + word

                    estado = -1

                word = ""

            # ------> CREATE <--------

            elif estado == 1:

                if word in tk_set:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 2

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    Create(word)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un nombre para el set"

                    else:
                        error_msg = "Nombre de set no válido"

                    estado = -1

                word = ""

            # ------> LOAD <--------

            elif estado == 11:

                if word in tk_into:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 12

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    nombre_set = word
                    archivos_set = []

                    estado = 13

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un set"

                    else:
                        error_msg = "No existe el set " + word

                    estado = -1

                word = ""

            elif estado == 13:

                if word in tk_files:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 14

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_archivo"][1].append(word)
                    archivos_set.append(word)
                    estado = 15

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 22

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    Use(word)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un set"

                    else:
                        error_msg = "No existe el set " + word

                    estado = -1

                word = ""

            # ------> SELECT <--------

            elif estado == 31:

                if word in tk_asterisco:
                    dict_tokens["tk_asterisco"][1].append(word)
                    lista_llaves = ["*"]
                    estado = 32

                elif Palabra(word):
                    dict_tokens["tk_cadena"][1].append(word)
                    lista_llaves = [word]
                    estado = 33

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un atributo"

                    else:
                        error_msg = "No se reconoció la palabra " + word + "."

                    estado = -1

                word = ""

            elif estado == 32:

                if word in tk_where:
                    dict_tokens["tk_reserved"][1].append(word)
                    estado = 35

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 35

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    lista_llaves.append(word)
                    estado = 33

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un atributo"

                    else:
                        error_msg = (
                            "No se reconoció la palabra "
                            + word
                            + ". Se esperaba un atributo"
                        )

                    estado = -1

                word = ""

            elif estado == 35:

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
                        dict_tokens["tk_scolon"][1].append(word)
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
                        dict_tokens["tk_scolon"][1].append(word)

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
                    dict_tokens["tk_reservado"][1].append(word)
                    List()
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 52

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_color"][1].append(word)
                    Print(word)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    Max(word)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)
                    Min(word)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_asterisco"][1].append(word)
                    Sum(["*"])
                    estado = 150

                    if late_exit == True:
                        exit = True

                elif Palabra(word):
                    dict_tokens["tk_cadena"][1].append(word)
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
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_asterisco"][1].append(word)
                    Count(["*"])
                    estado = 150

                elif Palabra(word):
                    dict_tokens["tk_cadena"][1].append(word)
                    lista_llaves.append(word)
                    estado = 92

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                        dict_tokens["tk_scolon"][1].append(word)

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
                    dict_tokens["tk_cadena"][1].append(word)
                    lista_llaves.append(word)
                    estado = 92

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un atributo"

                    else:
                        error_msg = "No se reconoció la palabra " + word

                    estado = -1

                word = ""

            # ------> REPORTE <--------

            elif estado == 101:

                if word in tk_to:
                    dict_tokens["tk_reservado"][1].append(word)
                    estado = 102

                elif word in tk_tokens:
                    dict_tokens["tk_reservado"][1].append(word)
                    lista_tokens = []

                    for llave, valor in dict_tokens.items():
                        lista_tokens.append([llave, valor[0], str(valor[1])])

                    nombre_reporte = "Tokens"
                    Report(["Token", "Descripción", "Lexemas"], lista_tokens)
                    estado = 150

                    if late_exit == True:
                        exit = True

                else:
                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                    dict_tokens["tk_cadena"][1].append(word)

                    nombre_reporte = word
                    reporte = True
                    estado = 0

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
                        error_msg = "Se esperaba un nombre"

                    else:
                        error_msg = word + " no es un nombre válido"

                    estado = -1

                word = ""

            # ------> SCRIPT <--------

            elif estado == 111:

                if ArchivoSIQL(word):
                    dict_tokens["tk_archivo"][1].append(word)
                    scripts.append(word)
                    estado = 112

                else:

                    if word in tk_scolon:
                        dict_tokens["tk_scolon"][1].append(word)
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
                        dict_tokens["tk_scolon"][1].append(word)

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
                    dict_tokens["tk_scolon"][1].append(word)
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
                error_msg = ""
                if late_exit == True:
                    exit = True

        estado, lista_llaves, reporte = 0, [], False


# ================> EJECUCIÓN <====================


SimpleSQL("")
