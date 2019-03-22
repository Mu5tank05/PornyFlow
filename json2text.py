import json
import validators


total = 0
with open('data.json') as json_file:
    data = json.load(json_file)
    f = open("data.txt", "a")
    for p in data['comments']:
        if validators.url(p['comment']):
            print("URL Removed" + p['comment'])
        else:
            total = total + 1
            comment = str(p['comment'])
            f.write(comment.lower() + "\n")
    print("Comments Converted: " + str(total))

