#QUIPUZCOA LOPEZ YULEISY
personas = [("Yule", 18, "87654321"), ("Jean", 22, "12345678"), ("Chris", 18, "14725836"), ("Claudia", 19, "96385214")]
dni = ["12345678", "14725836"]
personascheck = []
for persona in personas:
    if persona[1] >= 18 and persona[2] in dni:
            personascheck.append(persona[0])
print("Las personas que cumplen las condiciones de ser mayor de edad y verificación de DNI son:\n", personascheck)