""" Remove the scale for "-".
"""
# for test : PT1512993

import clr
import sys
from System import Console
import System.Runtime.InteropServices as SRI

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")
<<<<<<< HEAD
# from SolidEdgeFileProperties import Properties
from scale import echelle
=======
from SolidEdgeFileProperties import Properties
>>>>>>> 39009afd7b81c12c75fe6b8054ecd73eb93eea28

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


<<<<<<< HEAD
=======
def echelle(doc):
    """
    replace echelle by "-".
    """
    # check if the draft is a draft.
    if doc.Name.lower().endswith(".dft"):
        print("Document name: %s" % doc.Name)
        properties = doc.Properties
        scale = properties("Custom").Item("ECHELLE").value
        if (scale != "-"):
            properties("Custom").Item("ECHELLE").value = "-"
            print("[SCALE CHANGED]: [%s]\t->\t[-]" % scale )
        else:
            print("change not necessary.")
    else:
        print("document not a draft.")
    # Update the draft with the properties 
    doc.UpdatePropertyTextDisplay()


>>>>>>> 39009afd7b81c12c75fe6b8054ecd73eb93eea28
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
