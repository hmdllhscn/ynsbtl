not = int(input("Notunuzu girin (0-100): "))

if not < 0 or not_deg > 100:
    print("Hatalı giriş")
elif 90 <= not_deg <= 100:
    print("Pekiyi")
elif 70 <= not_deg <= 89:
    print("İyi")
elif 50 <= not_deg <= 69:
    print("Orta")
else:
    print("Zayıf")
