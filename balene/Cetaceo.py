class Cetaceo:
    #Ordine è "Cetacea"
    #TODO: tenere solo nome, nome scientifico, sottordine (anche nel file txt)
    def __init__(self, nome, sottordine, famiglia, genere, nome_scientifico):
        self.nome = nome #es. "Focena comune"
        self.sottordine = sottordine #es. "Odontoceto"
        self.famiglia = famiglia #es. "Delphinidae"
        self.genere = genere #es. "Phocoena" 
        self.nome_scientifico = nome_scientifico #es. "Phocoena Phocoena"

    def __init__(self, stringone):
        #Sottordine-Famiglia-Genere-Nome_comune-Nome_scientifico
        ##TODO: sfruttare il costruttore di sopra con 5 argomenti
        parametri = stringone.split("-")
        self.sottordine = parametri[0]
        self.famiglia = parametri[1]
        self.genere = parametri[2]
        self.nome = parametri[3]
        self.nome_scientifico = parametri[4]
        
    def __str__(self):
        return f"{self.nome} ({self.nome_scientifico}), {self.sottordine}"

