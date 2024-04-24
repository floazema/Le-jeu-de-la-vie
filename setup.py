from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but some modules need help.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None

setup(
    name = "Le jeu de la vie",
    version = "0.1",
    description = "Le jeu de la vie en python avec pygame",
    options = {"build_exe": build_exe_options},
    executables = [Executable("src/main.py", base=base)]
)
