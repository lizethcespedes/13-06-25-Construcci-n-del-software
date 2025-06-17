from rich.table import Table
from rich.console import Console

table = Table(title="Librería Favorita")

table.add_column("Nombre", style="cyan", no_wrap=True)
table.add_column("Lenguaje", style="green")
table.add_column("Popularidad", justify="right", style="red")

table.add_row("Rich", "Python", "Media")
table.add_row("Requests", "Python", "Alta")
table.add_row("Seaborn", "Python", "Media")

console = Console()
console.print(table)
