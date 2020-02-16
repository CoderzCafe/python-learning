import json

name = "Sudipto Shahin"
print(json.dumps(name))

x = {
    "name": "John",
    "age": "47",
    "married": True,
    "Children": ("Anni", "Billy"),
    "Pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "FORD EDGE", "mpg": 24.1}
    ]
}

print(json.dumps(x))

## print with indent
print(json.dumps(x, indent=1))