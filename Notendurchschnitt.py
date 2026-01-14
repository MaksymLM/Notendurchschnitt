#print("1. Notendurchschnitt", "2. Mögliche Zeugnis-Note")

#function = input("Die Aufgabe:")

mathe = {}

mathe = input("Mathe: ")
deutsch = input("Deutsch: ")
english = input("English: ")

note_mathe = sum(mathe) / len(mathe)
note_deutsch = sum(deutsch) / len(deutsch)
note_english = sum(english) / len(english)

print(note_mathe, note_deutsch, note_english)
sum_noten = note_mathe + note_deutsch + note_english

notendurchschnitt = sum(sum_noten) / len(sum_noten)

print("Dein Notendurchschnitt ist:", )

