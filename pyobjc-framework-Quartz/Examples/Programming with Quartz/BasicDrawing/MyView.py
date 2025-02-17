import AppDrawing
import Cocoa
import Quartz
import FrameworkTextDrawing
import FrameworkUtilities
import objc
import UIHandling
import PDFHandling
from objc import super

# XXX: Why are these global?
_drawingCommand = UIHandling.kHICommandSimpleRect
_pdfDocument = None


class MyView(Cocoa.NSView):
    currentMenuItem = objc.IBOutlet()

    def initWithFrame_(self, frameRect):
        self = super().initWithFrame_(frameRect)
        if self is None:
            return None

        global _pdfDocument
        _pdfDocument = None
        return self

    if False:

        def isFlipped(self):
            return True

    def drawRect_(self, rect):
        context = Cocoa.NSGraphicsContext.currentContext().graphicsPort()

        if _pdfDocument is None:
            if _drawingCommand in (
                UIHandling.kHICommandDrawNSString,
                UIHandling.kHICommandDrawNSLayoutMgr,
                UIHandling.kHICommandDrawCustomNSLayoutMgr,
            ):

                if _drawingCommand == UIHandling.kHICommandDrawNSString:
                    FrameworkTextDrawing.drawNSStringWithAttributes()

                elif _drawingCommand == UIHandling.kHICommandDrawNSLayoutMgr:
                    FrameworkTextDrawing.drawWithNSLayout()

                else:
                    FrameworkTextDrawing.drawWithCustomNSLayout()
            else:
                AppDrawing.DispatchDrawing(context, _drawingCommand)

        else:
            mediaRect = Quartz.CGPDFDocumentGetMediaBox(_pdfDocument, 1)
            mediaRect.origin.x = mediaRect.origin.y = 0
            Quartz.CGContextDrawPDFDocument(context, mediaRect, _pdfDocument, 1)

    @objc.IBAction
    def setDrawCommand_(self, sender):
        global _drawingCommand, _pdfDocument

        newCommand = sender.tag()
        if _drawingCommand != newCommand:
            _drawingCommand = newCommand
            # The view needs to be redisplayed since there is a new drawing command.
            self.setNeedsDisplay_(True)

            # Disable previous menu item.
            if self.currentMenuItem is not None:
                self.currentMenuItem.setState_(Cocoa.NSOffState)

            # Update the current item.
            self.currentMenuItem = sender

            # Enable new menu item.
            self.currentMenuItem.setState_(Cocoa.NSOnState)

            # If we were showing a pasted document, let's get rid of it.
            if _pdfDocument:
                _pdfDocument = None

    def currentPrintableCommand(self):
        # The best representation for printing or exporting
        # when the current command caches using a bitmap context
        # or a layer is to not do any caching.
        if _drawingCommand in (
            UIHandling.kHICommandDrawOffScreenImage,
            UIHandling.kHICommandDrawWithLayer,
        ):
            return UIHandling.kHICommandDrawNoOffScreenImage

        return _drawingCommand

    def print_(self, sender):
        global _drawingCommand

        savedDrawingCommand = _drawingCommand
        # Set the drawing command to be one that is printable.
        _drawingCommand = self.currentPrintableCommand()
        # Do the printing operation on the view.
        Cocoa.NSPrintOperation.printOperationWithView_(self).runOperation()
        # Restore that before the printing operation.
        _drawingCommand = savedDrawingCommand

    def acceptsFirstResponder(self):
        return True

    @objc.IBAction
    def copy_(self, sender):
        FrameworkUtilities.addPDFDataToPasteBoard(_drawingCommand)

    @objc.IBAction
    def paste_(self, sender):
        global _pdfDocument

        newPDFDocument = PDFHandling.createNewPDFRefFromPasteBoard()
        if newPDFDocument is not None:
            _pdfDocument = newPDFDocument
            # The view needs to be redisplayed since there is
            # a new PDF document.
            self.setNeedsDisplay_(True)

    # Return the number of pages available for printing. For this
    # application it is always 1.
    def knowsPageRange_(self, aRange):
        return True, Cocoa.NSRange(1, 1)

    # Return the drawing rectangle for a particular page number.
    # For this application it is always the page width and height.
    def rectForPage_(self, page):
        pi = Cocoa.NSPrintOperation.currentOperation().printInfo()

        # Calculate the page height in points.
        paperSize = pi.paperSize()
        return Cocoa.NSMakeRect(0, 0, paperSize.width, paperSize.height)

    def validateMenuItem_(self, menuItem):
        if menuItem.tag() == _drawingCommand:
            self.currentMenuItem = menuItem
            menuItem.setState_(True)
        else:
            menuItem.setState_(False)

        return True
