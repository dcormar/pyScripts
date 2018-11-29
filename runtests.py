#!/usr/bin/env python
import CharacterReplacement as script1
import StringFormat as script2

if __name__ == "__main__":
    assert script1.rot13("Test") == "Grfg", "Oh no! script 1 failed!"

    assert script2.format_duration (1232323) == "14 days, 6 hours, 18 minutes and 43 seconds", "Oh no! script 2 failed!"

