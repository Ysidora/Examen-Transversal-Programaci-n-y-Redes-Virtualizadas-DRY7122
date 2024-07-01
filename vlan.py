# vlan.py
vlan_id = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_id <= 1005:
    print("La VLAN está en el rango normal.")
elif 1006 <= vlan_id <= 4094:
    print("La VLAN está en el rango extendido.")
else:
    print("Número de VLAN no válido.")
