#Python3 or later is required
from cryptography.fernet import Fernet as fn
from typing import List

class Description:

    def __init__(
        self, nameOfProgram: str,
        version: str,
        options: List[str],
        comingSoon : List[str]
        ) -> None:

        self.name = nameOfProgram
        self.version = version#'0.0.2'
        self.options = options
        self.expected = comingSoon

    def printLogo(self) -> None:
        logo = f"""
        Presents...


                              .,-:;//;:=,
                          . :H@@@MM@M#H/.,+%;,
                       ,/X+ +M@@M@MM%=,-%HMMM@X/,
                     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
                    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
                  ,%MM@@MH ,@%=             .---=-=:=,.
                  =@#@@@MX.,                -%HX$$%%%:;
                 =-./@M@M$                   .;@MMMM@MM:
                 X@/ -$MM/                    . +MM@@@M$
                ,@M@H: :@:                    . =X#@@@@-
                ,@@@MMX, .                    /H- ;@M@M=
                .H@@@@M@+,                    %MM+..%#$.
                 /MMMM@MMH/.                  XM@MH; =;
                  /%+%$XHH@$=              , .H@@@@MX,
                   .=--------.           -%H.,@@@@@MX,
                   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
                     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
                       =%@M@M#@$-.=$@MM@@@M; %M%=
                         ,:+$+-,/H#MMMMMMM@= =,
                              =++%%%%+/:-.



        ____________________________________________________________
        ____________________________________________________________
        ____________________                    ____________________
        ____________________    PhysTeX labs    ____________________
        ____________________        BSD         ____________________ 
        ____________________________________________________________
        ____________________________________________________________



        ____________________________________________________________
        __________________                        __________________
        __________________ {self.name} ver. {self.version} __________________
        ____________________________________________________________

        """
        print(logo)
    
    def printHelp(self) -> None:
        msg = f"""
        This is {self.name} to encrypt or decrypt text with generated key.
        Some options of this program are listed below...\n"""
        for i in range(len(self.options)):
            msg += '\t\t-' + str(i) + '. ' + self.options[i] + '\n'
        print(msg)

    def printConclusion(self) -> None:
        msg = """\nTrying to exit...\nSaving Data...\nWorking a lot...
    
                Done!
    
                Expected in next versions:\n"""

        for i in range(len(self.expected)):
            msg += '\t\t\t\t- ' + self.expected[i] + '\n'

        msg += """
        ____________________    PhysTeX labs    ____________________
        ____________________________________________________________
                """
        print(msg)


class Encryption:

    def __init__(self):
        self.key = None
        self.text = None
    
    def __str__(self):
        return "key == " + self.key.decode('utf-8')
    
    def printAllEncryptions(encryptions):
        for encryption in encryptions:
            print encryption
    
    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False

    __hash__ = None

    __repr__ = __str__

    def generateKey(self):
        self.key = fn.generate_key()

    def inputAndSaveKey(self):
        try:
            self.key = input("Enter your key:\n")
        # except ValueError:
        #     print("You've entered invalid key...")
        except:
            print("Some error has occured while doing this operation...")
            pass
        else:
            if self.key == None:
                print("Something went wrong...")
            else:
                print("Key has been successfully saved")

    def saveKeyToFile(self):
        f = open('key.txt', 'w+')
        try:
            f.write(self.key.decode('utf-8'))
        except TypeError:
            print("You haven't saved any key yet...")
        f.close()

    def loadKeyFromFile(self):
        try:
            f = open('key.txt', 'r')
        except FileNotFoundError:
            print("There is no file 'key.txt' with key in your local directory...")
        else:
            self.key = f.read().encode()
            f.close()
    
    def toEncrypt(self, text) -> str:
        try:
            f = fn(self.key)
            self.text = text
        except TypeError:
            print("You haven't saved any key yet...")
            return ""
        except AttributeError:
            print("You haven't provided any text to encrypt...")
            return ""
        except:
            print("Some error has occured while doing this operation...")
        else:
            return f.encrypt(self.text).decode('utf-8')

    def toDecrypt(self, text) -> str:
        try:
            f = fn(self.key)
            self.text = text
        except TypeError:
            print("You haven't saved any key yet...")
            return ""
        except AttributeError:
            print("You haven't provided any text to encrypt...")
        except:
            print("Some error has occured while doing this operation...")
        else:
            return f.decrypt(self.text).decode('utf-8')

    def showKey(self):
        try:
            print(self.key.decode('utf-8'))
        except AttributeError:
            print("There is no key yet...")


class Control:
    def __init__(self):
        self.wrongCounter = 0
        self.typedHandler = ''

    def outputResult(self, text, typeOfResult):
        print(typeOfResult,'\n' + 84 * '_' + '\n', text, '\n' + 84 * '_' + '\n')

    def mainLoop(self, de, en):
        de.printLogo()
        de.printHelp()
        while True:
            self.typedHandler = input("Enter your next command here:\n")
            if self.typedHandler in ('G', 'g'): # generatekey
                en.generateKey()

            elif self.typedHandler in ('ES', 'es', 'Es', 'sE'): # entersavekey
                en.inputAndSaveKey()

            elif self.typedHandler in ('S', 's'): # savekeyfile
                en.saveKeyToFile()

            elif self.typedHandler in ('E', 'e'): # encrypt
                try:
                    text = input("Enter text to encrypt:\n").encode()
                except:
                    print("Some error has occured while doing this operation...")
                else:
                    self.outputResult(en.toEncrypt(text), 'Encrypted text:')

            elif self.typedHandler in ('D', 'd'): #decrypt
                try:
                    text = input("Enter text to decrypt:\n").encode()
                except:
                    print("Some error has occured while doing this operation...")
                else:
                    self.outputResult(en.toDecrypt(text), 'Decrypted text:')

            elif self.typedHandler in ('F', 'f', 'q', ':q', 'Q', 'e', 'exit'):
                de.printConclusion()
                return

            elif self.typedHandler in ('LK', 'lk','Lk', 'lK'):
                en.loadKeyFromFile()
                
            elif self.typedHandler in ('H', 'h'):
                de.printHelp()
                
            elif self.typedHandler in ('K', 'k'):
                en.showKey()
            else:
                print("You've entered wrong command! Repeat please...")
                self.wrongCounter += 1
                if self.wrongCounter > 5:
                    self.wrongCounter = 0
                    print("You've entered wrong command multiple times! \
                    If you need help type 'h'")



def main():

    nameOfProgram = 'cryptScript'

    version = '0.0.2'

    options = [
        "To generate and apply new key type G",
        "To enter and save your key type ES",
        "To save your existing key to the file type S",
        "To encrypt your text type E",
        "To decrypt your text type D",
        "To print your current key type K",
        "To load key from file type LK",
        "To get this info again type H",
        "To exit this program type F"
    ]
    
    comingSoon = [
        "Saving key, encrypted and decrypted texts to files  (Done! +/-)",
        "Reading key, texts to encrypt or decrypt from files (Done! +/-)",
        "Cyrillic support                                    (  Done!  )",
        "Copy to buffer"
    ]
    
    de = Description(nameOfProgram, version, options, comingSoon)
    en = Encryption()
    ct = Control()

    ct.mainLoop(de, en)

    # de.printLogo()
    # de.printHelp()
    # de.printConclusion()
    # en.generateKey()
    # en.showKey()

if __name__ == '__main__':
    main()
