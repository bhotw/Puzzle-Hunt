import random

def get_secret_letter(number):
    letters = "AIDLFPFCJDOIWOAJDIFORAIDOFL AMVNDIWAPDOFLHAMVNBPAAPSOEKTALDIOF SPDOFLYMVNSUEOOPALCKUAMCIFO QIFKGPNNVMSUIELSPFJCEQIFOLBDAPDOFL\nAPDLFMGAPDLFMOWEIMCP APDLVNTNVIOPDOSAMCNB APCOFLSAMCKFIWAPCLFMIAPCOFLTANCMFIZAPCLFUEEMVNBURQUFILCLAPLMNVAASIDKVNEIFLMBDAILBVN IKFMBNAQIFOLGNHISJFNDOSVHEY IKDHFGACMVILBBQILFHGOMBNQILUIGHVBQTPLDWUG NBCTYGFPLDYFHANVBYRTCRTYUIOENVBREY\nPOLFNBTQUFJNBEIOFJGHNIOFJBN IOSJFBSILOFHGTPLMBNUEQDIFJGPIOFHGISAIDOFC SIFLPQFNVIFKDOPALDKCRQUFIGJWNBIRTYAVBDIFKRQIFLGJDBSICOF\nPFODLFTCNVISOHIWOFKDIIWIFOGRISOFNCTQIDOFIENIGFHDEISOFLCNISOFMC AIDOFXSIFOPACTSPDLCMEEISOFCPADLFKCSISOCKF SFKDCKLASDIFOEBCKDOFFQIDOFCTALDIFC\nAKCLDISANCKDLIDIFOCKXPIDCFO SKDICFSCIDOFITALKDCIECIDOCKPAPDICLSAJCIFO AJDKCLRWIDOFCIOSICODGAPCIDFHCODSFPTICOFIC CIDOFC       \n"
    if number > 0 and number < 750 and number % 7 == 0:
        print(letters[number-1], end='', flush=True)
        return
    rand = random.randint(0, 25)
    print(chr(ord('A') + rand), end='', flush=True)