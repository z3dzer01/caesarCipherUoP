'''
    Antoniou Efthimios dit13011@uop.gr
    This is a program tha breaks the original caesar cipher mtc3-esslinger-08.
'''
# Caesar Cipher Hacker

MESSAGE = """JQRRG, JQRRG, TGKVGT JQRRG, JQRRG, TGKVGT,
 YGPP GT HCGNNV, FCPP UEJTGKV GT. HCGNNV GT KP FGP ITCDGP,
 HTGUUGP KJP FKG TCDGP, HCGNNV GT KP FGP UWORH, FCPP OCEJV
 FGT TGKVGT RNWORU! JWORVA FWORVA JWORVA FWORVA UCV QP C YCNN
 JWORVA FWORVA JCF C ITGCV HCNN CNN VJG MKPI'U JQTUGU CPF CNN
 VJG MKPI'U OGP EQWNFP'V RWV JWORVA VQIGVJGT CICKP.
""".upper()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for key in range(len(LETTERS)):


    translated = ''

    for symbol in MESSAGE:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))
