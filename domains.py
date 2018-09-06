import read
import tldextract

df = read.load_data()

domains = df['url'].value_counts(dropna = True)

for name, row in domains[0:99].items():
    print("{0}: {1}".format(name, row))