#
#  FilteringArrayController.py
#  FilteringController
#
#  Converted by u.fiedler on 05.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Cocoa import NSArrayController
from objc import super


class FilteringArrayController(NSArrayController):
    _k_searchString = ""

    def search_(self, sender):
        self.setSearchString_(sender.stringValue())
        self.rearrangeObjects()

    def newObject(self):
        """
        Creates and returns a new object of the class specified by objectClass.
        Set default values, and keep reference to new object -- see arrangeObjects_
        """
        self.newObj = super().newObject()
        self.newObj.setValue_forKey_("First", "firstName")
        self.newObj.setValue_forKey_("Last", "lastName")
        return self.newObj

    def arrangeObjects_(self, objects):
        if self._k_searchString is None or self._k_searchString == "":
            self.newObj = None
            return super().arrangeObjects_(objects)

        # Create array of objects that match search string.
        # Also add any newly-created object unconditionally:
        # (a) You'll get an error if a newly-added object isn't added to
        # arrangedObjects.
        # (b) The user will see newly-added objects even if they don't
        # match the search term.

        matchedObjects = []
        lowerSearch = self._k_searchString.lower()
        for item in objects:
            if item == self.newObj:
                # if the item has just been created, add it unconditionally
                matchedObjects.append(item)
                self.newObj = None
            else:
                lowerName = item.valueForKeyPath_("firstName").lower()
                if lowerSearch in lowerName:
                    matchedObjects.append(item)
                else:
                    lowerName = item.valueForKeyPath_("lastName").lower()
                    if lowerSearch in lowerName:
                        matchedObjects.append(item)
        return super().arrangeObjects_(matchedObjects)

    def searchString(self):
        return self._k_searchString

    def setSearchString_(self, newStr):
        self._k_searchString = newStr
