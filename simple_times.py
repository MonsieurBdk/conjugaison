from utils import *


class SimpleTime:
    utils = Utils()
    def __init__(self, verb:str):
         self.verb = verb
    def getSuffixe(self, time:str, person:int, verb:str):
        suffix = ""
        utils = SimpleTime.utils
        radical = SimpleTime.utils.verbRadical(verb=self.verb)
        if radical.lower().endswith("g"):
            if (time == utils.IMPARFAIT and (person <= 3 or person == 6)) or time == utils.PASSE_SIMPLE and (person <= 5):
                suffix += "e"
        
        time = time.upper()
        if type(person) == int:
            match person:
                case 1:  
                    if time == utils.PRESENT:
                        suffix += "e"
                    elif time == utils.IMPARFAIT or time == utils.FUTURE_DU_PASSE:
                        suffix += "ais"
                
                    else:
                        suffix += "ai"   
                    
                case 2:
                        if time == utils.PRESENT:
                            suffix += "es"
                        elif time == utils.IMPARFAIT or time == utils.FUTURE_DU_PASSE:
                            suffix += "ais"
                        else:
                            suffix += "a"
                case 3:
                        if time == utils.PRESENT:
                            suffix += "e"
                        elif time == utils.IMPARFAIT or  time == utils.FUTURE_DU_PASSE:
                            suffix += "ait"
                        else:
                            suffix += "a"
                case 4:
                        if time == utils.PRESENT or time == utils.FUTURE_SIMPLE:
                            suffix += "ons"
                        elif time == utils.IMPARFAIT or  time == utils.FUTURE_DU_PASSE:
                            suffix += "ions"
                        elif time == utils.PASSE_SIMPLE:
                            suffix += "âmes"
                case 5:
                        if time == utils.PRESENT or time == utils.FUTURE_SIMPLE:
                            suffix += "ez"
                        elif time == utils.IMPARFAIT or  time == utils.FUTURE_DU_PASSE:
                            suffix += "iez"
                        else:
                            suffix += "âtes"
                case 6:
                        if time == utils.PRESENT:
                            suffix += "ent"
                        elif time == utils.IMPARFAIT or  time == utils.FUTURE_DU_PASSE:
                            suffix += "aient"
                        elif time == utils.FUTURE_SIMPLE:
                            suffix += "ont" 
                        else:
                            suffix += "èrent"
                case _:
                    return "-"
            
        return suffix
        
    def conjugateTime(self,  time:str, ):
        self.verb = self.verb.lower()
        utils = SimpleTime.utils
        radical = SimpleTime.utils.verbRadical(verb=self.verb)
        print(time)
        print()
        for i in range (len(utils.personal_pronouns)):
            pronoun = utils.personal_pronouns[i]
            sufix = self.getSuffixe(person=i+1, verb=self.verb, time=time)
            radical = utils.verbRadical(verb=self.verb)
            if(time == utils.FUTURE_SIMPLE or time == utils.FUTURE_DU_PASSE):
                radical = self.verb
            if(i==0):
                for voyel in utils.voyels:
                    if self.verb.startswith(voyel):
                        pronoun = "J'"
            print(pronoun + " " + radical + sufix)
        print("-"*15)
        print()

    def conjugateAllTimes(self):
        print("LES TEMPS SIMPLES")
        print(' - '*15)
        print()
        for time in SimpleTime.utils.SIMPLE_TIMES:
            self.conjugateTime(time=time)
        print('*'*20)