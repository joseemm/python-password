# Importamos el módulo random para generar números aleatorios
import random

# Definimos una función que genera una contraseña segura y aleatoria
def generar_contraseña(longitud, caracteres_especiales):
  # Creamos una cadena vacía para almacenar la contraseña
  contraseña = ""
  # Creamos una cadena con los posibles caracteres alfanuméricos
  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  # Si el usuario quiere caracteres especiales, los añadimos a la cadena
  if caracteres_especiales:
    caracteres += "!@#$%^&*()-_=+[]{};:,.<>/?"
  # Repetimos el proceso tantas veces como la longitud de la contraseña
  for i in range(longitud):
    # Elegimos un carácter al azar de la cadena y lo añadimos a la contraseña
    contraseña += random.choice(caracteres)
  # Devolvemos la contraseña generada
  return contraseña

# Pedimos al usuario que ingrese la longitud de la contraseña y si quiere caracteres especiales
longitud = int(input("¿De qué longitud quieres la contraseña? "))
caracteres_especiales = input("¿Quieres caracteres especiales? (s/n) ") == "s"

# Llamamos a la función para generar una contraseña y la mostramos por pantalla
contraseña = generar_contraseña(longitud, caracteres_especiales)
print("Tu contraseña es:", contraseña)
