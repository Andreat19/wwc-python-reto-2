# This is a sample Python script.
import pandas
import re
import string


def generar_dataframe_palabras(text):
    # Escribe el codigo para generar el diccionario con las ocurrencias de cada palabra.
         
    dic_empy = {}
    texto = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    list_text = texto.lower().split()
    for i in list_text:
        if i not in dic_empy:
            dic_empy[i] = 1
        else:
            dic_empy[i] += 1
    # Convertir el diccionario de ocurrencias en un Dataframe usando panda
    
    return pandas.DataFrame([[key, dic_empy[key]] for key in dic_empy.keys()], columns=['Palabra', 'Repeticiones'])


neruda = """Puedo escribir los versos más tristes esta noche.
            Yo la quise, y a veces ella también me quiso.

            En las noches como ésta la tuve entre mis brazos.
            La besé tantas veces bajo el cielo infinito.
            
            Ella me quiso, a veces yo también la quería.
            Cómo no haber amado sus grandes ojos fijos.""".lower()  # lower hace que todas las letras sean minúsculas.

if __name__ == '__main__':
    d = generar_dataframe_palabras(neruda)
    assert isinstance(d, pandas.DataFrame), "Aun no generas un Dataframe, verifica tu algoritmo!"
    print("Excelente, has convertido un poema en un Dataframe para trabajar con el!")
