import pandas as pd
import math

url = 'https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx'

if __name__ == '__main__':
    tables = pd.read_html('Download de Resultados - Portal Loterias _ CAIXA.html', )
    df = tables[0]
    df.info()
    print(df)
    with open('results.md', 'w') as writer:
        for row in df.iterrows():
            if not math.isnan(row[1]["Bola1"]):
                writer.write(f'{int(row[1]["Bola1"])},')
                writer.write(f'{int(row[1]["Bola2"])},')
                writer.write(f'{int(row[1]["Bola3"])},')
                writer.write(f'{int(row[1]["Bola4"])},')
                writer.write(f'{int(row[1]["Bola5"])},')
                writer.write(f'{int(row[1]["Bola6"])},')
                writer.write(f'{int(row[1]["Bola7"])},')
                writer.write(f'{int(row[1]["Bola8"])},')
                writer.write(f'{int(row[1]["Bola9"])},')
                writer.write(f'{int(row[1]["Bola10"])},')
                writer.write(f'{int(row[1]["Bola11"])},')
                writer.write(f'{int(row[1]["Bola12"])},')
                writer.write(f'{int(row[1]["Bola13"])},')
                writer.write(f'{int(row[1]["Bola14"])},')
                writer.write(f'{int(row[1]["Bola15"])}\n')

