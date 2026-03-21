wil={
    "nombre":"Wilfredo",
    "edad": "18 años",
    "ciudad": "Escuintla",
    "lenguaje_favorito": "Español"}
wil.update({"universidad": "San Pablo"})
for clave, valor in wil.items():
    print(clave,":",valor)
