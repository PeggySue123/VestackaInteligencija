def krajnjeStanje(trenutnePozicije: list[int], pocetnePozicije: list[int]) -> tuple[bool, int]:
    if (trenutnePozicije[0] == pocetnePozicije[8] and trenutnePozicije[1] == pocetnePozicije[9]):
        return (True, 1)
    if (trenutnePozicije[0] == pocetnePozicije[10] and trenutnePozicije[1] == pocetnePozicije[11]):
        return (True, 1)
    if (trenutnePozicije[2] == pocetnePozicije[8] and trenutnePozicije[3] == pocetnePozicije[9]):
        return (True, 1)
    if (trenutnePozicije[2] == pocetnePozicije[10] and trenutnePozicije[3] == pocetnePozicije[11]):
        return (True, 1)
    if (trenutnePozicije[4] == pocetnePozicije[4] and trenutnePozicije[5] == pocetnePozicije[5]):
        return (True, 2)
    if (trenutnePozicije[4] == pocetnePozicije[6] and trenutnePozicije[5] == pocetnePozicije[7]):
        return (True, 2)
    if (trenutnePozicije[6] == pocetnePozicije[4] and trenutnePozicije[7] == pocetnePozicije[5]):
        return (True, 2)
    if (trenutnePozicije[6] == pocetnePozicije[6] and trenutnePozicije[7] == pocetnePozicije[7]):
        return (True, 2)
    return (False, 0)