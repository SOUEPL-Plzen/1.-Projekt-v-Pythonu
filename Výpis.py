cislo = 1 # Vytvoření proměnné cislo s hodnotou 1 (int)

print(cislo) # Python vypíše proměnnou do terminálu, kde je uložené číslo 1

cislo = 5 # Přepsání původní hodnoty

print(cislo) # Nyní se vypíše 5, protože na řádku 5 bylo změněno na hodnotu 5 (int)
print(cislo + 3) # Pokud se jedná o stejné datové typy, dají se spojovat nebo sčítat pomocá matematických operátorů
# Můžete vyzkoušet přepsat na print(cislo + "3") co se stane, čtěte pozorně terminál
print(cislo ,"3") # Pokud je chceme spojovat dva různé datové typy, musíme hodnoty v printu oddělovat čárkou
print("Kod funguje") # Pokud bychom napsali "print(cislo + "3")", kod se tento nespustí, zkontrolujte chybu v terminálu


# Možnost, jak efektivně pracovat s více datovými typy pomocí takzvaných  f - stringu
# Jiné datový typy nebo proměný píšeme do {} - složene závorky píšeme pomocí levý alt + b/n
print(f"Číslo uložené v proměné cislo je {cislo}")

# ------------------------
#     Zadání z hodiny
# ------------------------

# Vytvořte proměnné pro:
    # Jméno
    # Příjmení
    # Věk
    # Výška v metrech
    # Pohlaví 1 - holka, 0 - kluk

# Vše vypiště do terminálu v takovém to příkladu
    # Pohlavý 1 (True) - Holka, 0 (False) - Kluk
    # Petr Breit
    # Je mu 26 let a měří 1.83 metrů
    # Pohlavý - 0

# Řešení

jmeno = "Petr" # Vytvoření proměnné s datovým typem string
prijmeni = "Breit" # -||-, proměnné si pojmenováváme bez diakritiky (háčky a čárky)
vek = 26 # Vytvoření proměnné s datovým typem int - celé číslo. Nepíšeme do ""
# Při vytvářání větších názvu oddělujeme _, s mezerou nebude fungovat
vyska_v_metrech = 1.83 # Vytváříme proěmnnou pomocí desetiné tečky (desetina čárka zde nefunguje), datový typ - float
pohlavi = False # Vytvoření proměnné s Boolean hodnotou (False - 0, True - 1) 

# Výpis informace pro uživatele co je 1 (True) či 0 (False)
print("Pohlavý 1 (True) - Holka, 0 (False) - Kluk") # V printu dáváme jednoduchý string
print(jmeno, prijmeni) # Voláme proměné pro výpis jména a příjmení v jednom řádku, proměnné oddělujeme čárkou

# Efetkivnější zápis, píšeme string a do něj v {nazev_proměný}, nezapomeňte na f před ""
print(f"Je mu {vek} let a měří {vyska_v_metrech} metrů")

# Jiný způsob zapsání s dvouma proměnnými
print("Pohlavý - ", pohlavi)