blood_type_donor = float(input("Введите группу крови донора (0, A, B, AB): "))
blood_type_patient = float(input("Введите группу крови поциента (0, A, B, AB): "))
if blood_type_donor == blood_type_patient or blood_type_donor == "0":
    print("Донор подходит")
else:
    print("Донор не подходит")