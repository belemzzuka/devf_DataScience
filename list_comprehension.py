students = [ "Pipino", "Sofia", "Warita", "Vaquita", "Chiwita" ];

best_students = [];

for s in students:
    #if s != "Pipino":
    if "Pipino" not in s:
        best_students.append(s);

print(best_students);

list_comprehension = [ s for s in students if s != "Pipino" ]
print("LIST COMPREHENSION: ", list_comprehension);

print("LIST COMPREHENSION: ")
[ print(s) for s in students if s != "Pipino" ]