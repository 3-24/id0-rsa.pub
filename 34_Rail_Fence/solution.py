ciphertext = "WAPSD EXTCO EEREF SELIO RSARC LIETE OIHHP VASTF EGBER IPAPN TOEGI AIATH DDHIY EACYE RQAEN OHRTE TEVME BGHMF EIOWS GFHCL XEUUC OMTOT LERES SDEWW ORCCS HEURE ATTEG ALSEB APXET IURWV RTEEH IOTLO SNACN NULCV LCMTH HHCOH TIOTD ASNAL TSANA CASOR LEKAS TATCW INTLO TRYER YLTND RILER AOMAX OITDE ECOIA HAALS TYIOA DAEHI OTSTE IEYES HHSNG EHCAT SOUAC EHSST TCODN FSOTS TIIGN LTTNL DUBST TCMIM EHTAO IUUPF TSTTI PUEAY OAEOA EEALA LWGWM GNHYU IAAHD TORYA OLVMH RHTGY IHNNM UAARL MMHID HYFCP GRAET MTCNT HIIIO RCVCL BOTSA OFRNR YEHTG IFHEA WLYSC EEEEY UVEIM SOEUE TAYHN NITEK AERAW DSIAE QTDIE HET".replace(" ","")

def getLineLength(l_cipher,line,key):
    n = key
    q = l_cipher // (2*n-2)
    r = l_cipher % (2*n-2)

    assert type(q) is int

    if line == 1:
        return (q+1) if r >= 1   else q
    elif line == key:
        return (q+1) if r >= key else q
    else:
        if r >= (2*n-2) - (line - 2):
            return 2*q + 2
        elif r >= line:
            return 2*q + 1
        else:
            return 2*q


def sumRowIndex(l_cipher,row,key):
    sum = 0
    for line in range (1,row+1):
        sum += getLineLength(l_cipher,line,key)
    return sum



def decrypt(cipher,key):
    plain = ''
    l = len(cipher)

    for i in range (1,l+1):
        # i = nq + r
        n = key
        q = i // (2*n-2)
        r = i % (2*n-2)

        if r >= key + 1:
            row = key - (r-key)
            column = 2*q + 2
        elif r == key:
            row = key
            column = q + 1
        elif r >= 2:
            row = r
            column = 2*q +1
        elif r == 1:
            row = 1
            column = q+1
        else:
            row = 2
            column = 2*q
        print(i, sumRowIndex(l,row-1,key)+column)
        print(plain)
        plain += cipher[sumRowIndex(l,row-1,key)+column-1]

    return plain

test_vector = 'WECRL TEERD SOEEF EAOCA IVDEN'.replace(' ','')
print(decrypt(ciphertext,17))
