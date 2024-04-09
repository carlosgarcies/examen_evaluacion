import pandas as pd

from data_reader import leer_df, filtro_media

def main():
    print(filtro_media(leer_df("datos_examen.csv")))

if __name__ == "__main__":
    main()