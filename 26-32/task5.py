skills = {
    "one" : {"name": "HTML", "progress" : "90%"},
    "two" : {"name": "CSS", "progress" : "80%"},
    "three" : {"name": "PYTHON", "progress" : "90%"},
}
print(skills["one"]["name"]+" progress is "+skills["one"]["progress"])
print(skills["two"]["name"]+" progress is "+skills["two"]["progress"])
print(skills["three"]["name"]+" progress is "+skills["three"]["progress"])
four = {"name":"GIT HUB", "progress":"20%"}
skills["four"] = four
print(skills["four"]["name"]+" progress is "+skills["four"]["progress"])

