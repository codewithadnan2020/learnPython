# Make students stand according to there houses

def check_houses():
    name = input("Enter Your Name:");
    records = {"adnan":"safa", "fazil": "hira"};

    if name in records:
        print("You are from",records[name],"house.");
    else:
        print("You are not registaered.");
        check_houses();

check_houses();
