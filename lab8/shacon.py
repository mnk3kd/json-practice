import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)


with open('chacon.csv', 'a') as csv_file:
    
    if csv_file.tell() == 0:
        csv_file.write("name,html_url,updated_at,visibility\n")
    
    
    for repo in data[:5]:
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
        
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        
        csv_file.write(line)
