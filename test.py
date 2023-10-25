from symdec import Symdec

# path do dataset que irá utilizar
DATA_PATH = "data/Symptom2Disease.csv"

Symdec = Symdec(DATA_PATH)

Symdec.load()

query = "I've been experiencing intense itching all over my skin, and it's driving me crazy."

result = Symdec.run(query)

print("\nDoenças ordenadas através da similaridade da descrição dos sintomas:")


for i in range(0, 5):
    dec = result[i]
    print(dec[0], f"{dec[1]:.2f}")