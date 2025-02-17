import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMusicEvents(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(AVFoundation.AVMIDIControlChangeMessageType)

        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeBankSelect, 0)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeModWheel, 1)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeBreath, 2)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeFoot, 4)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypePortamentoTime, 5)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeDataEntry, 6)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeVolume, 7)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeBalance, 8)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypePan, 10)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeExpression, 11)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeSustain, 64)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypePortamento, 65)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeSostenuto, 66)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeSoft, 67)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeLegatoPedal, 68)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeHold2Pedal, 69)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeFilterResonance, 71)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeReleaseTime, 72)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeAttackTime, 73)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeBrightness, 74)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeDecayTime, 75)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeVibratoRate, 76)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeVibratoDepth, 77)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeVibratoDelay, 78)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeReverbLevel, 91)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeChorusLevel, 93)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeRPN_LSB, 100)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeRPN_MSB, 101)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeAllSoundOff, 120)
        self.assertEqual(
            AVFoundation.AVMIDIControlChangeMessageTypeResetAllControllers, 121
        )
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeAllNotesOff, 123)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeOmniModeOff, 124)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeOmniModeOn, 125)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeMonoModeOn, 126)
        self.assertEqual(AVFoundation.AVMIDIControlChangeMessageTypeMonoModeOff, 127)

        self.assertIsEnumType(AVFoundation.AVMIDIMetaEventType)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeSequenceNumber, 0x00)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeText, 0x01)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeCopyright, 0x02)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeTrackName, 0x03)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeInstrument, 0x04)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeLyric, 0x05)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeMarker, 0x06)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeCuePoint, 0x07)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeMidiChannel, 0x20)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeMidiPort, 0x21)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeEndOfTrack, 0x2F)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeTempo, 0x51)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeSmpteOffset, 0x54)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeTimeSignature, 0x58)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeKeySignature, 0x59)
        self.assertEqual(AVFoundation.AVMIDIMetaEventTypeProprietaryEvent, 0x7F)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(AVFoundation.AVExtendedNoteOnEventDefaultInstrument, int)
