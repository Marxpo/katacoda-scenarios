import json
from datetime import datetime

# Remplacer 'chemin_vers_votre_fichier.json' par le chemin réel vers votre fichier JSON
chemin_fichier_json = 'response.json'
res_file="snapshots_file_time.txt"
# Lire le fichier JSON
with open(chemin_fichier_json, 'r') as fichier:
    datajs = json.load(fichier)

# Accéder au dernier bloc de 'snapshots'
last_bloc = datajs['snapshots'][-1]

# Extraire la valeur de 'endtime'
value_timeflow = last_bloc['endTime']

# Afficher la valeur de 'endtime.'
print(f"La valeur du 'timeflow' du dernier bloc est : {value_timeflow}")

try:
    date_endTime = datetime.strptime(value_timeflow, "%Y-%m-%dT%H:%M:%SZ")
    # Formater 'date_endTime' en 'YYYY-MM-DD'
    valeur_endTime_formattee = date_endTime.strftime("%Y-%m-%d")
    time_to_write = f"UAT4: {valeur_endTime_formattee}"
    print(f"La valeur formatée du 'endTime' du dernier bloc est : {valeur_endTime_formattee}")
    with open(res_file, 'w') as fichier_sortie:
        fichier_sortie.write(time_to_write)
        print(f"the time has been saved in: '{res_file}'.")


except ValueError as e:
    print(f"Erreur lors de la conversion de la date: {e}")
