class CBancaire():
    def __init__(self, solde):
        self.solde = solde

    
    def crediter(self, montant_credit):
        self.solde += montant_credit
        return print(f"Votre solde est de : {self.solde} FCFA")
    
    def debiter (self, montant_debit):
        self.solde -= montant_debit
        return self.solde

    def getSolde (self):
        return print(f"Votre solde est de : {self.solde} FCFA")


    def virerVers(self, cb, montant):
        if self.solde < montant :
            print ("Le solde est insuffisant")
        else:
            self.debiter(montant)
            cb.crediter(montant)
            print(f"Votre nouveau solde est de : {self.solde} FCFA")

    