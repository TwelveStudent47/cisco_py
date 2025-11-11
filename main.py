def main():
    print("Melyik feladatot szeretnéd végrehajtani?:")
    print("1. Alap konfiguráció letöltése\n"
          + "2. Aktuális konfiguráció mentése\n",
          + "3. Egyedi konfig betöltése az eszközön\n"
          + "4. Egyedi kód futtatása\n"
          + "5. DHCP konfig beállítása net nélkül\n"
          + "6. DHCP konfig beállítása nettel\n")
    user_choice = input("Feladat száma: ")
    user_choice = user_choice[0]
    match user_choice:
        case "1":
            print("Alap konfig elmentve...")
        case "2":
            print("Aktuális konfig elmentve...")
        case "3":
            print("Egyedi konfig beállítva...")
        case "4":
            print("Egyedi kód lefuttatva...")
        case "5":
            print("DHCP konfig beállítva net nélkül...")
        case "6":
            print("DHCP konfig beállítva nettel....")
        case _:
            print("Nem megfelelő számot adtál meg.")

if __name__ == "__main__":
    main()