import requests

def check_methods(url, methods=["GET", "POST", "PUT", "DELETE", "PATCH", "TRACE", "OPTIONS"]):
  """
  Verifica se i metodi HTTP specificati sono abilitati su una URL.

  Args:
    url: L'URL da testare.
    methods: lista di metodi HTTP da verificare (default: tutti i metodi comuni).

  Returns:
    Un dizionario contenente il metodo e il codice di stato della risposta.
  """

  results = {}
  for method in methods:
    try:
      response = requests.request(method, url)
      results[method] = response.status_code
    except requests.exceptions.RequestException as e:
      results[method] = f"Errore: {e}"
  return results

# Insert data scanning
ip_address = input("INSERT IP: ")
file_path = input("INSERT NAME FILE OR PATH FILE URL TEST: ")
output_file = input("PLEASE INSERT FILE NAME RESULTS: ")

# open file result
with open(output_file, 'w') as file:
    # Iteriamo su ogni directory
    for directory in open(file_path, 'r'):
        url = f"http://{ip_address}/{directory.strip()}"
        risultati = check_methods(url)

        # write result
        for metodo, codice in risultati.items():
            file.write(f"Metodo: {metodo}, URL: {url}, Codice di risposta: {codice}\n")

print(f"Result saved in file {output_file}")