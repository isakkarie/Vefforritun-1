aldur=int(input("Sláðu inn hvað þú ert gamall/gömul: "))

if aldur<12:
    print("Þú er barn.")
elif aldur>11 and aldur<20:
    print("Þú ert unglingur.")
else:
    print("Þú ert fullorðin.")
