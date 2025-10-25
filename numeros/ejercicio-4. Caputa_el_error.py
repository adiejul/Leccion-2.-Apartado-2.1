try:
    año =  int(input("¿En que año naciste?"))
    edad = (2025-año)
    print("Tienes ", edad, "años.")
except ValueError:
    print("Introduce un año válido")