m_10 = int(input("Ingrese el total de monedas de $10 con las que cuenta: "))
m_5 = int(input("Ingrese el total de monedas de $5 con las que cuenta: "))
m_2 = int(input("Ingrese el total de monedas de $2 con las que cuenta: "))
m_1 = int(input("Ingrese el total de monedas de $1 con las que cuenta: "))
m_05 = float(input("Ingrese el total de monedas de $0.5 con las que cuenta: "))
m_02 = float(input("Ingrese el total de monedas de $0.20 con las que cuenta: "))
m_01 = float(input("Ingrese el total de monedas de $0.10 con las que cuenta: "))

pesos_total = (m_10 * 10) + (m_5 * 5) + (m_2 * 2) + (m_1 * 1) + \
    (m_05 * 0.5) + (m_02 * 0.20) + (m_01 * 0.10)

print("Usted tiene un total de $ ", pesos_total, "pesos.")

input()