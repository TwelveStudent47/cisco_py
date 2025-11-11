from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',      
    'username': 'admin',
    'password': 'cisco',
}

router_connection = ConnectHandler(**router)

router_connection.enable()

router_conf = router_connection.send_config_from_file("config.txt")

print(router_conf)

router_connection.disconnect()

# 1. parancs letölti a alap confot a fileból
# 2. parancs letölti az aktuális confot lementi fileba, time import (év, hó, nap: óra /perc/másodperc)
# 3. parancs minta kód, felhasználó tetszése szerint, csak a commands listát kell változtatni
# 4. parancs alap dhcp konf net nélkül + 1 nettel
# ++. tesztelni hogy kell-e dhcp az ssh-hoz