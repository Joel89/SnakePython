import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name ="Slither",
    options ={"build.exe":{"packages":["pygame"],"include_files":["apple.png","snakehead.png", "pacman.png","frog.png"]}},

    description = "Slither Game Tutorial",
    executables = executables
)
