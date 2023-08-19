import os

def citeste_fisier(cale):
    codificari = ['utf-8', 'cp1252', 'latin1', 'ISO-8859-1']
    for codificare in codificari:
        try:
            with open(cale, 'r', encoding=codificare) as f:
                return f.readlines()
        except UnicodeDecodeError:
            pass
    print(f"ATENȚIE: Nu s-a putut deschide fișierul {cale} folosind codificările {', '.join(codificari)}.")
    return []

def extrage_passwords(linii):
    cuvinte_cheie = ["Password:", "pass:", "PASS:"]
    linii_extrase = set()

    for linie in linii:
        for cuvant in cuvinte_cheie:
            if cuvant in linie:
                linie_curata = linie.replace(cuvant, '').strip()
                linii_extrase.add(linie_curata)
                break

    return linii_extrase

def gaseste_si_copiaza_passwords(director_start, fisier_iesire):
    linii_unic = set()

    for radacina, directoare, fisiere in os.walk(director_start):
        for fisier in fisiere:
            cale_completa = os.path.join(radacina, fisier)
            linii = citeste_fisier(cale_completa)
            linii_unic.update(extrage_passwords(linii))
            print(f"Procesat: {cale_completa}. Total linii unice până acum: {len(linii_unic)}")

    # Asigură-te că directoarele pentru fișierul de ieșire există
    director_iesire = os.path.dirname(fisier_iesire)
    if director_iesire and not os.path.exists(director_iesire):
        os.makedirs(director_iesire)

    with open(fisier_iesire, 'w', encoding='utf-8') as out:
        if linii_unic:
            for linie in linii_unic:
                out.write(linie)
                out.write('\n')
            print(f"Finalizat! Total linii unice găsite: {len(linii_unic)}")
        else:
            print("Nicio linie unică găsită pentru a fi salvată.")

# Exemplu de utilizare:
director_start = '.'  # Acesta este directorul curent. Modifică după nevoie.
fisier_iesire = 'passout.txt'

gaseste_si_copiaza_passwords(director_start, fisier_iesire)
