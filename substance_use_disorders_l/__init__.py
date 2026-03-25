"""Substance use disorders database for 14 Latin American countries (2000–2024): al
DOI:https://github.com/juanmoisesd/substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://github.com/juanmoisesd/substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Substance use disorders database for 14 Latin American count"
def info():print("DOI: https://github.com/juanmoisesd/substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024\nGitHub: https://github.com/juanmoisesd/substance-use-disorders-latin-america-alcohol-cannabis-cocaine-2000-2024")
