path = 'C:\\Users\\marti\\OneDrive\\Documenten\\HU Leerjaar 1 BLOK 3\\Structured Programming\\Opdracht 8 tekstbestand.txt'

def export(i):
    clear = open(path, "w")
    clear.close()
    export = open(path, "a")
    export.write(i)
    export.close()


def new():
    f = open(path, "r")
    file = f.read()
    compressed = "".join(file.split())
    export(compressed)

new()
