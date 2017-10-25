'''
    Antoniou Efthimios dit13011@uop.gr
    This is a program tha breaks the modified caesar cipher, alphabet with 62 characters
    (in my solution with less because commas and all other signs i just left them as they
     are maybe it's wrong).
'''
# Caesar Cipher Hacker

MESSAGE = """Xlmw irgvCtxih qiwweki wlepp gpevmjC lsA RSX xs irgvCtx e
 qiwweki xsheC! Izir mj mx Aew wyjjmgmirx efsyx 6444 Cievw eks, sv xs fi
 qsvi tvigmwi mr xli Ciev 88 FG, rsAeheCw mx mw rsx. XsheC iegl ws-geppih
 Wgvmtx Omhhmi Asyph fi efpi xs kix wirwmxmzi mrjsvqexmsr, mj xliC Aivi
 irgvCtxih xlmw AeC.""".upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'


for key in range(len(LETTERS)):


    translated = ''

    for symbol in MESSAGE:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
        elif symbol in NUMBERS:
            num = NUMBERS.find(symbol)
            if key > 10:
                #Because if it exceeds 10 it will create a problem at NUMBERS[num]
                #and it will say out of bounds
                num = num - (key% 10)
            else:
                num = num - key

            if num < 0:
                num = num + len(NUMBERS)

            translated = translated + NUMBERS[num]

        else:
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))
