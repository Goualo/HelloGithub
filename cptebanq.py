class CpteBanq:
    def __init__(self,num_compte,solde):
        #self.nom_prenom=nom_prenom
        self.num_compte=num_compte
        self.solde=float(solde)
   # cpte_xx= CompteBank(nom_prenom, num_compte, solde)
        self.getSolde()
    def crediter(self,montant):
        self.solde+=float(montant)
        self.getSolde()
        return #print("Votre nouveau Solde après versement est de", self.solde)
    def debiter(self,montant):
        if montant > self.solde :
            return('Solde insuffisant')
        else:
            self.solde-=float(montant)
            self.getSolde()
            return #print("Votre nouveau Solde après retrait est de", self.solde)      
    def calcul_agios (self):
        self.solde+=float(self.solde)*3/100
        self.getSolde()
        return #print("le montant des agios est de", float(self.solde)*3/100)
    def getSolde(self):
        return print("le solde du compte numero", self.num_compte, "est de :", self.solde)
    def obtenirSolde(self):
        return self.solde
    def virerVersCb(self,cb, montt):
        #numcb=input("Donner le numéro du compte qui où virer l'argent")
        #montt=input("Donner le montant à virer")
        self.debiter(montt)
        cb.crediter(montt)
        return