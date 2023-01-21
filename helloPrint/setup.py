"""A simple setup script to test pandas."""

# test_pandas.py is a very simple script.
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

from __future__ import annotations

from cx_Freeze import Executable, setup, sys

options = {"build_exe": 
{
    #"packages": ["pandas", "numpy", "requests", "datetime", "csv", "sortTwoJoin", "columJoin"]
    "packages": ["pandas", "numpy", "requests", "datetime", "csv",]
    }
}

executables = [
    Executable("sortOne_MAIN.py")
]

setup(
    name="supplier_tables",
    version="0.1",
    description="Supplier Tables to be manipulated for upload",
    executables=executables,
    options=options,
)

# #
# On Windows, you can build a simple installer containing all the files cx_Freeze includes for your application, by running the setup script as:
# # python setup.py bdist_msi

#navigate to directory and execute:
#python setup.py build