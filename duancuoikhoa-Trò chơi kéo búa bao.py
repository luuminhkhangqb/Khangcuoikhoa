import random
print("Chào mừng bạn đến với trò chơi kéo búa bao!!")
nguoi=input("Mời bạn nhập, bạn chọn búa kéo hay bao: ")
may2 = ["keo", "bua", "bao"]
may = random.choice(may2)
print("Máy chọn: ", may)
if nguoi == "kéo" and may == "búa": 
    print("Bạn đã thua")
elif nguoi == "búa" and may == "kéo": 
    print("Bạn đã thắng")
elif nguoi == "bao" and may == "kéo": 
    print("Bạn đã thua")
elif nguoi == "kéo" and may == "bao": 
    print("Bạn đã thắng")
elif nguoi == "bao" and may == "búa": 
    print("Bạn đã thắng")
elif nguoi == "búa" and may == "bao": 
    print("Bạn đã thua")
elif nguoi == "búa" and may == "búa": 
    print("Hòa")
elif nguoi == "kéo" and may == "kéo": 
    print("Hòa")
elif nguoi == "bao" and may == "bao": 
    print("Hòa")
choilai=input("Bạn có muốn chơi lại không (Có hay Không) : ")
if (choilai == "Có"):
    nguoi=input("Mời bạn nhập, bạn chọn búa kéo hay bao: ")
    may2 = ["keo", "bua", "bao"]
    may = random.choice(may2)
    print("Máy chọn: ", may)
    if nguoi == "kéo" and may == "búa": 
      print("Bạn đã thua")
    elif nguoi == "búa" and may == "kéo": 
      print("Bạn đã thắng")
    elif nguoi == "bao" and may == "kéo": 
      print("Bạn đã thua")
    elif nguoi == "kéo" and may == "bao": 
      print("Bạn đã thắng")
    elif nguoi == "bao" and may == "búa": 
      print("Bạn đã thắng")
    elif nguoi == "búa" and may == "bao": 
      print("Bạn đã thua")
    elif nguoi == "búa" and may == "búa": 
      print("Hòa")
    elif nguoi == "kéo" and may == "kéo": 
      print("Hòa")
    elif nguoi == "bao" and may == "bao": 
      print("Hòa")
elif (choilai == "Không"):
    print("Vậy thì tạm biệt và hẹn gặp lại. Chúc bạn một ngày tốt lành. ")