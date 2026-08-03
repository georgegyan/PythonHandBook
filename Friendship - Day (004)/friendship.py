from rich.console import Console
from rich.text import Text

console = Console()
# Create the message and color mapping
text = "Happy Friendship Day!"
colors = [
    "red", "yellow", "green", "cyan", "blue", "white", "magenta",
    "red", "yellow", "green", "cyan", "blue", "magenta", "red",
    "yellow", "green", "white", "cyan", "blue", "magenta", "red"
]
# Generate the colorful message
message = Text()
for char, color in zip(text, colors):
    message.append(char, style=color)

console.print(message)