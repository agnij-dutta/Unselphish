import pickle
model = pickle.load(open(r'Application/resources/trained_model.sav', 'rb'))
def execute(emails, model):
    '''emails = [str]
    It is reccomended to only pass 1 email per execution for readabitly and easier debugging experience'''
    prediction = model.predict(emails)
    res = "Cannot be determined"
    for p in prediction:
        if p == 'spam':
            res = "It is a spam"
        else:
            res = "It is not a spam"
    return res