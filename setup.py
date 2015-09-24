import py_compile, os,cx_Freeze,sys,shutil

executables = [cx_Freeze.Executable("pyNote.py")]

cx_Freeze.setup(
    name="pyNote Text Editor",
    author="Adonis Megalos",
    version="0.0.0.1",
    options={"build_exe": {"packages":[],
                           "excludes": [],
                           "include_files":[]} },
    executables = executables

    )

shutil.copyfile("pyNote.py", 'build/exe.win32-3.2/pyNote.py')
