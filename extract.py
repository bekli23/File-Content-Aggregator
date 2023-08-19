import os

def citeste_fisier(cale):
    codificari = ['utf-8', 'cp1252', 'latin1', 'ISO-8859-1']
    for codificare in codificari:
        try:
            with open(cale, 'r', encoding=codificare) as f:
                return f.read()
        except UnicodeDecodeError:
            pass
    print(f"ATENȚIE: Nu s-a putut deschide fișierul {cale} folosind codificările {', '.join(codificari)}.")
    return ""

def gaseste_si_copiaza_fisiere(director_start, nume_fisiere, fisier_iesire):
    with open(fisier_iesire, 'w', encoding='utf-8') as out:
        for radacina, directoare, fisiere in os.walk(director_start):
            for fisier in fisiere:
                if fisier in nume_fisiere:
                    cale_completa = os.path.join(radacina, fisier)
                    continut = citeste_fisier(cale_completa)
                    out.write(continut)
                    out.write('\n\n')  # Adaugă două linii noi între conținutul fiecărui fișier pentru claritate

# Exemplu de utilizare:
director_start = '.'  # Acesta este directorul curent. Modifică după nevoie.
nume_fisiere = ['All Passwords.txt', 'passwords.txt']
fisier_iesire = 'out.txt'

gaseste_si_copiaza_fisiere(director_start, nume_fisiere, fisier_iesire)
