def formula(loopStep):
    """"""
    # sekcja wprowadzająca dane od użytkownika poprzez konsole
    dataName = input("Podaj Imię: ")
    dataSurename = input("Podaj Nazwisko: ")
    dataAge = input("Podaj Wiek: ")
    dataCity = input("Podaj miejsce zamieszkania:")

    Lp = loopStep  # liczba porządkowa wprowadzonej danej

    # Wprowadzenie zmiennych od użytkownika do struktury listy
    dataList = [str(Lp), dataName, dataSurename, dataAge, dataCity]

    # Transformacja listy na string:
    dataTextLine = '||'.join(dataList)

    return dataTextLine

tableOfUsers = []

for x in range (3):
    dataLine = formula(x+1)
    tableOfUsers.append(dataLine)

textTableOfUsers = '\n'.join(tableOfUsers)

print(textTableOfUsers)