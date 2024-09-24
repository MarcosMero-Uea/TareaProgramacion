'creamos un Diccionario'

informacion_personal = {'nombre': 'Marcos Mero',
                        'edad': 30 ,
                        'Ciudad' : 'Montecristi',
                        'trabajo':'supervisor'}

print("esta es el diccionario original:")
print(informacion_personal)
#----------------Modificacion del Diccionario--------------------

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal['Ciudad']='Manta'

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Ingeniero en Sistema"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

print("Este es el Diccionario modificamos:")
print(informacion_personal)