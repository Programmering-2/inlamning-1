def get_name():
    """Fråga efter namn och returnera svaret."""
    while True:
        name = input("Ange ditt namn: ").strip()
        if name:
            return name
        print("Namnet får inte vara tomt. Försök igen.")


def get_age():
    """Fråga efter ålder och returnera ett heltal."""
    while True:
        answer = input("Ange din ålder: ").strip()
        try:
            age = int(answer)
        except ValueError:
            print("Ogiltig ålder. Skriv ett heltal, till exempel 25.")
            continue

        if 0 <= age <= 120:
            return age
        print(f"Är du {age} år gammal?! Det tror jag inte på. Försök igen.")


def calculate_year_100(age):
    """Beräkna och returnera året då personen fyller 100."""
    current_year = 2026
    return current_year + (100 - age)


def main():
    name = ""
    age = 0

    while True:
        print("\n1. Ange namn och ålder")
        print("2. Visa vilket år du fyller 100")
        print("3. Avsluta")

        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            name = get_name()
            age = get_age()
            print(f"Tack, {name}! Du är {age} år gammal.")
        elif choice == "2":
            if not name:
                print("Du måste först ange namn och ålder (alternativ 1).")
            else:
                year = calculate_year_100(age)
                if year < 2026:
                    print(f"{name}, du fyllde 100 år {year}.")
                elif year == 2026:
                    print(f"{name}, du fyller 100 år i år ({year})!")
                else:
                    print(f"{name}, du fyller 100 år {year}.")
        elif choice == "3":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val. Välj 1, 2 eller 3.")


if __name__ == "__main__":
    main()