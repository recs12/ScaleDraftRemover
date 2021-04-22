""" Replace background with the official of the company.
"""
# for test : PT1512993

import sys
import clr
import System
from System import Console
from System.IO.Path import Combine
import System.Runtime.InteropServices as SRI

clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")
from SolidEdgeFileProperties import Properties

__project__ = "ScaleDraftRemover"
__author__ = "recs"
__version__ = "0.0.1"
__update__ = "2021-04-12"


def prompt_exit():
    raw_input("\nPress any key to exit...")
    sys.exit()


def raw_input(message):
    Console.WriteLine(message)
    return Console.ReadLine()



def echelle(doc):
    """
    replace echelle by "-".
    """
    # check if the draft is a draft.
    if doc.Name.lower().endswith(".dft"):
        print("Document name: %s" % doc.Name)
        properties = doc.Properties
        scale = properties('Custom').Item('ECHELLE').value
        print("Current scale: %s" %scale)
        properties('Custom').Item('ECHELLE').value = "-"
    else:
        print("document not a draft.")



def main():
    """User can choose to update one draft or many in same time"""
    try:
        # Connection to the application, only one session should be opened here.
        application = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        response = raw_input(
            """Would you like to delete the scale indication, (Press y/[Y] to proceed.):\n"(Option: Press '*' for processing documents in batch)""")

        if response.lower() in ["y", "yes"]:
            doc = application.ActiveDocument
            echelle(doc)

        elif response.lower() in ["*"]:
            # loop through all the drafts
            documents = application.Documents
            for doc in documents:
                echelle(doc)
        else:
            pass

    finally:
        prompt_exit()


if __name__ == "__main__":
    print("%s\n--author: %s --version: %s --last-update : %s \n" %
          (__project__, __author__, __version__, __update__))
    main()
