"""
mode="r" is read only
mode="w" is write only (will overwrite files or create new!)
mode="a" is append only (will add on to files)
mode="r+" is reading and writing
mode="w+" is writing and reading (Overwrites existing files or creates a new file!)
"""

file = open("import.txt", mode="w")
file.write("Import this")
file.close()