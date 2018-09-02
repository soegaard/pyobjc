from PyObjCTools.TestSupport import *

import CoreServices

class TestMDImport (TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(CoreServices.MDItemRef)

    def test_functions(self):
        self.assertIsInstance(CoreServices.MDItemGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CoreServices.MDItemCreate)
        self.assertResultIsCFRetained(CoreServices.MDItemCreateWithURL)
        self.assertResultIsCFRetained(CoreServices.MDItemsCreateWithURLs)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttribute)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributes)


        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributeNames)
        self.assertResultIsCFRetained(CoreServices.MDItemsCopyAttributes)

    @expectedFailure
    def test_functions_missing(self):
        # Link error on 10.13
        self.assertIsNullTerminated(CoreServices.MDItemCopyAttributeList)
        self.assertResultIsCFRetained(CoreServices.MDItemCopyAttributeList)

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDItemAttributeChangeDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemContentType, unicode)
        self.assertIsInstance(CoreServices.kMDItemKeywords, unicode)
        self.assertIsInstance(CoreServices.kMDItemTitle, unicode)
        self.assertIsInstance(CoreServices.kMDItemAuthors, unicode)
        self.assertIsInstance(CoreServices.kMDItemProjects, unicode)
        self.assertIsInstance(CoreServices.kMDItemWhereFroms, unicode)
        self.assertIsInstance(CoreServices.kMDItemComment, unicode)
        self.assertIsInstance(CoreServices.kMDItemCopyright, unicode)
        self.assertIsInstance(CoreServices.kMDItemLastUsedDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemContentCreationDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemContentModificationDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemDurationSeconds, unicode)
        self.assertIsInstance(CoreServices.kMDItemContactKeywords, unicode)
        self.assertIsInstance(CoreServices.kMDItemVersion, unicode)
        self.assertIsInstance(CoreServices.kMDItemPixelHeight, unicode)
        self.assertIsInstance(CoreServices.kMDItemPixelWidth, unicode)
        self.assertIsInstance(CoreServices.kMDItemColorSpace, unicode)
        self.assertIsInstance(CoreServices.kMDItemBitsPerSample, unicode)
        self.assertIsInstance(CoreServices.kMDItemFlashOnOff, unicode)
        self.assertIsInstance(CoreServices.kMDItemFocalLength, unicode)
        self.assertIsInstance(CoreServices.kMDItemAcquisitionMake, unicode)
        self.assertIsInstance(CoreServices.kMDItemAcquisitionModel, unicode)
        self.assertIsInstance(CoreServices.kMDItemISOSpeed, unicode)
        self.assertIsInstance(CoreServices.kMDItemOrientation, unicode)
        self.assertIsInstance(CoreServices.kMDItemLayerNames, unicode)
        self.assertIsInstance(CoreServices.kMDItemWhiteBalance, unicode)
        self.assertIsInstance(CoreServices.kMDItemAperture, unicode)
        self.assertIsInstance(CoreServices.kMDItemProfileName, unicode)
        self.assertIsInstance(CoreServices.kMDItemResolutionWidthDPI, unicode)
        self.assertIsInstance(CoreServices.kMDItemResolutionHeightDPI, unicode)
        self.assertIsInstance(CoreServices.kMDItemExposureMode, unicode)
        self.assertIsInstance(CoreServices.kMDItemExposureTimeSeconds, unicode)
        self.assertIsInstance(CoreServices.kMDItemEXIFVersion, unicode)
        self.assertIsInstance(CoreServices.kMDItemCodecs, unicode)
        self.assertIsInstance(CoreServices.kMDItemMediaTypes, unicode)
        self.assertIsInstance(CoreServices.kMDItemStreamable, unicode)
        self.assertIsInstance(CoreServices.kMDItemTotalBitRate, unicode)
        self.assertIsInstance(CoreServices.kMDItemVideoBitRate, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudioBitRate, unicode)
        self.assertIsInstance(CoreServices.kMDItemDeliveryType, unicode)
        self.assertIsInstance(CoreServices.kMDItemAlbum, unicode)
        self.assertIsInstance(CoreServices.kMDItemHasAlphaChannel, unicode)
        self.assertIsInstance(CoreServices.kMDItemRedEyeOnOff, unicode)
        self.assertIsInstance(CoreServices.kMDItemMeteringMode, unicode)
        self.assertIsInstance(CoreServices.kMDItemMaxAperture, unicode)
        self.assertIsInstance(CoreServices.kMDItemFNumber, unicode)
        self.assertIsInstance(CoreServices.kMDItemExposureProgram, unicode)
        self.assertIsInstance(CoreServices.kMDItemExposureTimeString, unicode)
        self.assertIsInstance(CoreServices.kMDItemHeadline, unicode)
        self.assertIsInstance(CoreServices.kMDItemInstructions, unicode)
        self.assertIsInstance(CoreServices.kMDItemCity, unicode)
        self.assertIsInstance(CoreServices.kMDItemStateOrProvince, unicode)
        self.assertIsInstance(CoreServices.kMDItemCountry, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSName, unicode)
        self.assertIsInstance(CoreServices.kMDItemDisplayName, unicode)
        self.assertIsInstance(CoreServices.kMDItemPath, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSSize, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSCreationDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSContentChangeDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSOwnerUserID, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSOwnerGroupID, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSExists, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSIsReadable, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSIsWriteable, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSHasCustomIcon, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSIsExtensionHidden, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSIsStationery, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSInvisible, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSLabel, unicode)
        self.assertIsInstance(CoreServices.kMDItemFSNodeCount, unicode)
        self.assertIsInstance(CoreServices.kMDItemTextContent, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudioSampleRate, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudioChannelCount, unicode)
        self.assertIsInstance(CoreServices.kMDItemTempo, unicode)
        self.assertIsInstance(CoreServices.kMDItemKeySignature, unicode)
        self.assertIsInstance(CoreServices.kMDItemTimeSignature, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudioEncodingApplication, unicode)
        self.assertIsInstance(CoreServices.kMDItemComposer, unicode)
        self.assertIsInstance(CoreServices.kMDItemLyricist, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudioTrackNumber, unicode)
        self.assertIsInstance(CoreServices.kMDItemRecordingDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemMusicalGenre, unicode)
        self.assertIsInstance(CoreServices.kMDItemIsGeneralMIDISequence, unicode)
        self.assertIsInstance(CoreServices.kMDItemRecordingYear, unicode)
        self.assertIsInstance(CoreServices.kMDItemOrganizations, unicode)
        self.assertIsInstance(CoreServices.kMDItemLanguages, unicode)
        self.assertIsInstance(CoreServices.kMDItemRights, unicode)
        self.assertIsInstance(CoreServices.kMDItemPublishers, unicode)
        self.assertIsInstance(CoreServices.kMDItemContributors, unicode)
        self.assertIsInstance(CoreServices.kMDItemCoverage, unicode)
        self.assertIsInstance(CoreServices.kMDItemSubject, unicode)
        self.assertIsInstance(CoreServices.kMDItemTheme, unicode)
        self.assertIsInstance(CoreServices.kMDItemDescription, unicode)
        self.assertIsInstance(CoreServices.kMDItemIdentifier, unicode)
        self.assertIsInstance(CoreServices.kMDItemAudiences, unicode)
        self.assertIsInstance(CoreServices.kMDItemNumberOfPages, unicode)
        self.assertIsInstance(CoreServices.kMDItemPageWidth, unicode)
        self.assertIsInstance(CoreServices.kMDItemPageHeight, unicode)
        self.assertIsInstance(CoreServices.kMDItemSecurityMethod, unicode)
        self.assertIsInstance(CoreServices.kMDItemCreator, unicode)
        self.assertIsInstance(CoreServices.kMDItemEncodingApplications, unicode)
        self.assertIsInstance(CoreServices.kMDItemDueDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemStarRating, unicode)
        self.assertIsInstance(CoreServices.kMDItemPhoneNumbers, unicode)
        self.assertIsInstance(CoreServices.kMDItemEmailAddresses, unicode)
        self.assertIsInstance(CoreServices.kMDItemInstantMessageAddresses, unicode)
        self.assertIsInstance(CoreServices.kMDItemKind, unicode)
        self.assertIsInstance(CoreServices.kMDItemRecipients, unicode)
        self.assertIsInstance(CoreServices.kMDItemFinderComment, unicode)
        self.assertIsInstance(CoreServices.kMDItemFonts, unicode)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsRootKey, unicode)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsKeyFilterType, unicode)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopsLoopMode, unicode)
        self.assertIsInstance(CoreServices.kMDItemAppleLoopDescriptors, unicode)
        self.assertIsInstance(CoreServices.kMDItemMusicalInstrumentCategory, unicode)
        self.assertIsInstance(CoreServices.kMDItemMusicalInstrumentName, unicode)

    @min_os_level('10.5')
    def test_constants10_5(self):
        self.assertIsInstance(CoreServices.kMDItemContentTypeTree, unicode)
        self.assertIsInstance(CoreServices.kMDItemEditors, unicode)
        self.assertIsInstance(CoreServices.kMDItemEXIFGPSVersion, unicode)
        self.assertIsInstance(CoreServices.kMDItemAltitude, unicode)
        self.assertIsInstance(CoreServices.kMDItemLatitude, unicode)
        self.assertIsInstance(CoreServices.kMDItemLongitude, unicode)
        self.assertIsInstance(CoreServices.kMDItemSpeed, unicode)
        self.assertIsInstance(CoreServices.kMDItemTimestamp, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSTrack, unicode)
        self.assertIsInstance(CoreServices.kMDItemImageDirection, unicode)
        self.assertIsInstance(CoreServices.kMDItemCFBundleIdentifier, unicode)
        self.assertIsInstance(CoreServices.kMDItemSupportFileType, unicode)
        self.assertIsInstance(CoreServices.kMDItemInformation, unicode)
        self.assertIsInstance(CoreServices.kMDItemDirector, unicode)
        self.assertIsInstance(CoreServices.kMDItemProducer, unicode)
        self.assertIsInstance(CoreServices.kMDItemGenre, unicode)
        self.assertIsInstance(CoreServices.kMDItemPerformers, unicode)
        self.assertIsInstance(CoreServices.kMDItemOriginalFormat, unicode)
        self.assertIsInstance(CoreServices.kMDItemOriginalSource, unicode)
        self.assertIsInstance(CoreServices.kMDItemAuthorEmailAddresses, unicode)
        self.assertIsInstance(CoreServices.kMDItemRecipientEmailAddresses, unicode)
        self.assertIsInstance(CoreServices.kMDItemURL, unicode)

    @min_os_level('10.6')
    def test_constants10_6(self):
        self.assertIsInstance(CoreServices.kMDItemParticipants, unicode)
        self.assertIsInstance(CoreServices.kMDItemPixelCount, unicode)
        self.assertIsInstance(CoreServices.kMDItemNamedLocation, unicode)
        self.assertIsInstance(CoreServices.kMDItemAuthorAddresses, unicode)
        self.assertIsInstance(CoreServices.kMDItemRecipientAddresses, unicode)

    @min_os_level('10.7')
    def test_constants10_7(self):
        self.assertIsInstance(CoreServices.kMDItemDownloadedDate, unicode)
        self.assertIsInstance(CoreServices.kMDItemDateAdded, unicode)
        self.assertIsInstance(CoreServices.kMDItemCameraOwner, unicode)
        self.assertIsInstance(CoreServices.kMDItemFocalLength35mm, unicode)
        self.assertIsInstance(CoreServices.kMDItemLensModel, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSStatus, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSMeasureMode, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDOP, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSMapDatum, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDestLatitude, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDestLongitude, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDestBearing, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDestDistance, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSProcessingMethod, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSAreaInformation, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDateStamp, unicode)
        self.assertIsInstance(CoreServices.kMDItemGPSDifferental, unicode)
        self.assertIsInstance(CoreServices.kMDItemLabelIcon, unicode)
        self.assertIsInstance(CoreServices.kMDItemLabelID, unicode)
        self.assertIsInstance(CoreServices.kMDItemLabelKind, unicode)
        self.assertIsInstance(CoreServices.kMDItemLabelUUID, unicode)
        self.assertIsInstance(CoreServices.kMDItemIsLikelyJunk, unicode)
        self.assertIsInstance(CoreServices.kMDItemExecutableArchitectures, unicode)
        self.assertIsInstance(CoreServices.kMDItemExecutablePlatform, unicode)
        self.assertIsInstance(CoreServices.kMDItemApplicationCategories, unicode)
        self.assertIsInstance(CoreServices.kMDItemIsApplicationManaged, unicode)

    @min_os_level('10.11')
    def test_constants10_11(self):
        self.assertIsInstance(CoreServices.kMDItemHTMLContent, unicode)

if __name__ == "__main__":
    main()