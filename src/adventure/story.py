from adventure.utils import read_events_from_file
from rich.console import Console
from rich.theme import Theme
import random

adventure_theme = Theme({
    "head":"bold #407b7c",
    "question": "bold magenta underline",
    "left_choice": "cyan",
    "right_choice": "yellow",
    "exit_choice": "red",
    "left": "green",
    "right": "blue"
})

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "[left]You walk left. " + event+"[/left]"

def right_path(event):
    return "[right]You walk right. " + event+"[/right]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')
    console = Console(theme=adventure_theme)
    console.print("[head]You wake up in a dark forest. You can go left or right.[/head]")
    while True:
        choice = console.input("[question]Which direction do you choose?[/question] ([left_choice]left[/left_choice]/[right_choice]right[/right_choice]/[exit_choice]exit[/exit_choice]): ")

        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        console.print(step(choice, events))
