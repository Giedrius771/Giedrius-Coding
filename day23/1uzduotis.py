import json

with open('json_colors.json') as f:
    data = json.load(f)

new_data = {
    "colors": [
        {
            "color": color["color"],
            "rgb": ", ".join(str(c) for c in color["code"]["rgba"][:3]),
            "hex": color["code"]["hex"]
        }
        for color in data["colors"]
        if "code" in color
    ]
}

for color in new_data["colors"]:
    if "code" in color:
        del color["code"]

with open('new.json', 'w') as f:
    json.dump(new_data, f, indent=4)
