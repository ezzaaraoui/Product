from abc import ABC, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    def setProduit(self, produit):
        self.__produit = produit

    @property
    def quantite(self):
        return self.__quantite

    def setQuantite(self, quantite):
        self.__quantite = quantite

    def __str__(self):
        return f"le produit est {self.__produit} , et la quantite est {self.__quantite}"

    def __eq__(self, o):
        return self.__quantite == o.quantite
    
    

class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom

    def setNom(self, nom):
        self.__nom = nom

    @property
    def code(self):
        return self.__code

    def setCode(self, code):
        self.__code = code
    
    def __str__(self):
        return f"le nom est {self.__nom} , et la code est {self.__code}"

    def __eq__(self, o):
        return self.__code == o.code

    @abstractmethod
    def getPrixHT(self):
        pass



class Produit_compose(Produit):
    _tva = 0.18
    def __init__(self, nom, code, frais, listcom):
        super().__init__(nom, code)
        self.__frais = frais
        self.__listcom = listcom

    @property
    def frais(self):
        return self.__frais

    def setFrais(self, frais):
        self.__frais = frais

    @property
    def listcom(self):
        return self.__listcom

    def setListcom(self, listcom):
        self.__listcom = listcom

    def __str__(self):
        r = f"Frais: {self.__frais}\n"
        for i in self.__listcom:
            r += i.__str__() + "\n"
        return r

    def getPrixHT(self):
        produitTotalP = 0
        for i in self.__listcom:
            produitTotalP += i.getPrixHT()
        return produitTotalP

    def __eq__(self, o):
        return self.__listcom == o.listcom
    
    

class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"le code est {self.__code} , et le nom est {self.__nom} et le prix d'achat est {self.__prixAchat}"

    def getPrixHT(self):
        return self.__prixAchat

