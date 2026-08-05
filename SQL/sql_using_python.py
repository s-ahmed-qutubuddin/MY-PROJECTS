
person = [
    {"id":1,"email":"a"},
    {"id":2,"email":"b"},
    {"id":3,"email":"a"},
]

new_person = []
empty_set=set()

for a in person:
    for b in person:
        if a["email"]==b["email"] and a["id"]>b["id"]:
            empty_set.add(a["id"])
            for p in person:
                if p["id"] not in empty_set:
                    new_person.append(p)

print(new_person)
