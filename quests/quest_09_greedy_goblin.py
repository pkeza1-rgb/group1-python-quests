#!/usr/bin/env python3
"""Quest 9: The Greedy Goblin"""

gold = 27
friends = 4

each_gets = gold // friends
goblin_keeps = gold % friends

print(f"Each friend gets: {each_gets} gold pieces.")
print(f"The goblin keeps: {goblin_keeps} gold pieces.")
