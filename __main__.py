""" Replace background with the official of the company.
"""

import clr
import sys
from System import Console
from System.IO.Path import Combine
import System.Runtime.InteropServices as SRI

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")
# from SolidEdgeFileProperties import Properties
from scale import echelle

__project__ = "ScaleDraftRemover"
__author__ = "recs"
__version__ = "0.0.2"
__update__ = "2021-05-27"


def prompt_exit():
    raw_input("\nPress any key to exit...")
    sys.exit()


def raw_input(message):
    Console.WriteLine(message)
    return Console.ReadLine()


def main():
    """User can choose to update one draft or many in same time"""
    try:
        application = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        response = raw_input(
            """Would you like to delete the scale indication, (Press y/[Y] to proceed.):\n"(Option: Press '*' for processing documents in batch)"""
        )

        if response.lower() in ["y", "yes"]:
            doc = application.ActiveDocument
            echelle(doc)

        elif response.lower() in ["*"]:
            documents = application.Documents
            for doc in documents:
                echelle(doc)
        else:
            pass

    finally:
        prompt_exit()


if __name__ == "__main__":
    print(
        "%s\n--author: %s --version: %s --last-update : %s \n"
        % (__project__, __author__, __version__, __update__)
    )
    main()
