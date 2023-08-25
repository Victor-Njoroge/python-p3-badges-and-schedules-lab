def badge_maker(name):
    return f"Hello, my name is {name}."
badge_maker("Arel")
def batch_badge_creator(names):
    for name in names:
        return f"Hello, my name is {name}"
batch_badge_creator(["Arel","Carol"])
def assign_rooms(names, rooms):
    for name, room in zip(names, rooms):
        print(f"Hello, my name is {name} ,"+f" your room is room {room}")
assign_rooms(["Arel","Carol"],[1,2])
def printer(names,rooms):
     for name in names:
        return f"Hello, my name is {name}"
     for name, room in zip(names, rooms):
        print(f"Hello, my name is {name} ,"+f" your room is room {room}")
printer(["Arel","Carol"],[1,2])