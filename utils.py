class Utils:

    def __init__(self):
        self.personal_pronouns = ["Je", "Tu", "Il(Elle)", "Nous", "Vous", "Ils(Elles)"]
        self.voyels = ["é", "e", "a", "i", "o", "u", "y", "î"]
        self.PRESENT = "PRESENT"
        self.IMPARFAIT = "IMPARFAIT"
        self.FUTURE_SIMPLE = "FUTURE SIMPLE"
        self.PASSE_SIMPLE = "PASSE SIMPLE"
        self.FUTURE_DU_PASSE = "FUTURE DU PASSE"

        self.PASSE_COMPOSE = "PASSE COMPOSE"
        self.PLUS_QUE_PARFAIT = "PLUS-QUE-PARFAIT"
        self.FUTURE_ANTERIEUR = "FUTURE ANTERIEUR"
        self.PASSE_ANTERIEUR = "PASSE ANTERIEUR"
        self.FUTUR_ANTERIEUR_DU_PASSE = "FUTUR ANTERIEUR DU PASSE"
        self.SIMPLE_TIMES = [self.PRESENT, self.IMPARFAIT, self.FUTURE_SIMPLE, self.PASSE_SIMPLE, self.FUTURE_DU_PASSE]
        self.COMPOSED_TIMES = [self.PASSE_COMPOSE, self.PLUS_QUE_PARFAIT, self.FUTURE_ANTERIEUR, self.PASSE_ANTERIEUR, self.FUTUR_ANTERIEUR_DU_PASSE]
        
        self.STATE_VERBS = ["", ""]


    def verbRadical(self, verb:str):
        return verb[0:(len(verb) - 2)]
    def verbPastParticiple(self, verb:str):
        return self.verbRadical(verb=verb)+ "é";