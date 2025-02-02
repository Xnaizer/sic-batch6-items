input = [
    {
        "nama" : "ayam",
        "rasa" : "manis"
    },
    {
        "nama" : "bebek",
        "rasa" : "asam"
    },
    {
        "nama" : "sapi",
        "rasa" : "manis"
    },
    {
        "nama" : "kambing",
        "rasa" : "asin"
    },
    {
        "nama" : "ikan",
        "rasa" : "asam"
    }
]

rasaManis = list(filter(lambda x: x['rasa'] == "manis", input)) 

print(len(rasaManis))