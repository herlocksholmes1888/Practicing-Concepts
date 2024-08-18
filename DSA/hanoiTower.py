# The currently empty towers only accept 1 disk. I do not know how to solve this issue 

def move_disk(from_tower, to_tower):
    disk = from_tower.pop()
    if not to_tower or disk < to_tower[-1]:
        to_tower.append(disk)
    else:
        print("You cannot stack a bigger disk on a smaller one")
        from_tower.append(disk)

def display_towers(towers):
  for i, tower in enumerate(towers):
      print(f"Tower {i}: {tower}")
    
towers = [
          [3, 2, 1], 
          [],    
          []          
      ]

while True:
    display_towers(towers)

    from_tower_index = int(input("Pick a tower to move a disk from (0, 1, 2): "))
    to_tower_index = int(input("Pick a tower to move a disk to (0, 1, 2): "))

    move_disk(towers[from_tower_index], towers[to_tower_index])