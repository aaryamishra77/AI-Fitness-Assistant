import json

fn = "data/exercises.json"
try:
    j = json.load(open(fn, "r", encoding="utf-8"))
    assert isinstance(j, list)
    for e in j:
        assert "id" in e and "name" in e
    print("Valid JSON with", len(j), "exercises")
except Exception as ex:
    print("Validation failed:", ex)
