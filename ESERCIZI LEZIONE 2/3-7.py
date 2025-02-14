#3-7

name_for_invites = ["Joseph Stalin", "Adolf Hitler", "Massimino il Trace"]

for i in name_for_invites:

    print(i, "you are invited to my party!")

print("oh no! Adolf can't attend the party")

name_for_invites.pop(1)

name_for_invites.append("Gesù")

for i in name_for_invites:

    print(i, "you are invited to my party!")

print("Sentite, abbiamo trovato un tavolo più grande. Abbiamo invitato gli amici della Giusi")

name_for_invites.insert(0, "Giustino Pio")

name_for_invites.insert(2, "Gigi Proietti")

name_for_invites.append("Solone di Mileto")

for i in name_for_invites:

    print(i, "you are invited to my party!")



for i in range(len(name_for_invites) - 2):

    persona_non_invitata = name_for_invites.pop()

    print("mi spiace",persona_non_invitata , "non puoi venire alla cena")

print(name_for_invites)

for i in name_for_invites:

    del name_for_invites[-2:]

    print(name_for_invites)
    



