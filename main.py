import netmiko
from functions import save_default_config, save_current_config, run_custom_code

def main():
    user_ip = input("Adj meg a routered IP címét: ")
    print("Melyik feladatot szeretnéd végrehajtani?:")
    print("1. Alap konfiguráció letöltése\n*"
          + "2. Aktuális konfiguráció mentése\n*"
          + "3. Egyedi konfig betöltése az eszközön\n"
          + "4. Egyedi kód futtatása\n*"
          + "5. DHCP konfig beállítása net nélkül\n"
          + "6. DHCP konfig beállítása nettel\n")
    user_choice = input("Feladat száma: ")
    user_choice = user_choice[0]
    match user_choice:
        case "1":
            save_default_config(user_ip)
        case "2":
            save_current_config(user_ip)
        case "3":
            user_config = input("Írd be a futtatni kívánt config nevét: ")
            with open(user_config, "r") as file:
                commands = file.readlines()
            run_custom_code(user_ip, commands)
        case "4":
            commands = [
                "int s0/1/0",
                "ip add 10.0.0.1 255.255.255.0",
                "no sh"
            ]
            run_custom_code(user_ip, commands)
        case "5":
            print("Melyiket szeretnéd betölteni?:")
            print("1. DHCP net nélkül, NAT-ból"
                  + "2. DHCP alapkonfig")
            user_second_choice = input("Feladat száma: ")
            match user_second_choice:
                case "1":
                    with open("dhcp_from_nat_without_internet", "r") as file:
                        commands = file.readlines()
                    run_custom_code(user_ip, commands)
                case "2":
                    with open("dhcp_without_internet.txt", "r") as file:
                        commands = file.readlines()
                    run_custom_code(user_ip, commands)
                case _:
                    print("Nem megfelelő számot adtál meg.")
        case "6":
            with open("dhcp_with_internet.txt", "r") as file:
                commands = file.readlines()
            run_custom_code(user_ip, commands)
        case _:
            print("Nem megfelelő számot adtál meg.")

if __name__ == "__main__":
    main()