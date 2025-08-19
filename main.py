from utils import bonjour
from datetime import datetime as dt

if __name__ == "__main__":
    heure = dt.today()
    if heure <= 18 :
        salutation = "Bonjour"
    else:
        salutation = "Bonsoir"
        
    print(salutation("GitHub"))

