# Make students stand according to there houses

def check_houses():
    name = input("Enter Your Name:");
    records = [["adnan", "safa"], ["fazil", "hira"]];

    for record in records:
        if record[0] == name:
            print("You are from "+record[1]+" house.");
            break;
        else:
            print("You are not registered.");
            check_houses();
            break;

check_houses();
