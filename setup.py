from cx_Freeze import setup, Executable

base = None    

executables = [Executable("passGEN.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Password Generator BY Matheesha",
    options = options,
    version = "0.1",
    description = 'Create Any Type Of Password You Like',
    executables = executables
)