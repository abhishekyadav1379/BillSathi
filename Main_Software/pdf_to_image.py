import sys, fitz  # import the bindings
fname = "invoice.pdf"  # get filename from command line
doc = fitz.open(fname)  # open document
for page in doc:  # iterate through the pages
    print(page)
    pix = page.get_pixmap()  # render page to an image
    zoom_x = 16.0  # horizontal zoom
    zoom_y = 16.0  # vertical zoom
    # dpi = 300
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
    # mat.prescale(dpi / 72.0, dpi / 72.0)  # Adjust matrix for DPI
    pix = page.get_pixmap(matrix=mat)

    pix.save("page-%i.png" % page.number)  # store image as a PNG
    break