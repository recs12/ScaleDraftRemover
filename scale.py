import clr

clr.AddReference("Interop.SolidEdge")


def echelle(doc):
    """Replace echelle by "-"."""
    print("---")

    # draft (code 2)
    if doc.Type == 2:
        print("Document name: %s" % doc.Name)
        properties = doc.Properties
        scale = properties("Custom").Item("ECHELLE").value

        if scale != "-":
            properties("Custom").Item("ECHELLE").value = "-"
            print("[Scale changed]: \t%s\t->\t[-]" % scale)
            doc.UpdatePropertyTextDisplay()  # Update the draft with the properties
        else:
            print("Change not necessary.")

    else:
        print("Document not a draft.")

    print("...")
