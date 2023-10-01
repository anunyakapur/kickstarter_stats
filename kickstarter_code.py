import csv
with open("ks-projects-201801.csv", "r", encoding='utf-8') as file_in:

    reader = csv.DictReader(file_in)
    category_dict = {}

    for line in reader:
        category = line["category"]
        state = line["state"]
        country = line["country"]
        currency = line["currency"]
        name = line["name"]
        deadline = line["deadline"]
        goal = line["goal"]
        pledged = line["pledged"]
        backers = line["backers"]
        
        kickstarter_entry = [state, country, currency, name, deadline, goal, pledged, backers]

        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append(kickstarter_entry)
    
    successful = 0
    failed = 0
    total = 0
    for key in category_dict:
        for entry in category_dict[key]:
            total += 1
            if entry[0] == "successful":
                successful += 1
            elif entry[0] == "failed":
                failed += 1
        success_percent = successful/total*100
        failed_percent = failed/total*100
        print(f'Category: {key}, Success: {success_percent:3.1f}%, Failed: {failed_percent:3.1f}%')

