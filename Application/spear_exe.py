import pickle
model = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model.sav', 'rb'))
model1 = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model_1.sav', 'rb'))
model3 = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model_3.sav', 'rb'))
model4 = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model_4.sav', 'rb'))
model5 = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model_5.sav', 'rb'))
model6 = pickle.load(open(r'C:\Users\USER\Desktop\Unselphish\Unselphish-main\ML_models\model_6.sav', 'rb'))

def execute(emails, model):

    '''emails = [str]
    It is reccomended to only pass 1 email per execution for readabitly and easier debugging experience'''

    prediction = model.predict(emails)
    pred_percent = model.predict_proba(emails)

    res = "Cannot be determined"
    percent = "Cannot be determined"

    for ind in range(len(list(prediction))):
        p = list(prediction)[ind]

        if p == 0:
            res = "It is a spam"
            percent = pred_percent[ind][0] * 100
            print(res, f'Probability: {round(percent)}%')
            continue

        elif p == 1:
            res = "It is not a spam"
            percent = pred_percent[ind][1] * 100
            print(res, f'Probability: {round(percent)}%')
            continue


email = ['''Subject: You have (3) failed email deliveries
Sender address: noreply@domain.com
Sender ip:
Reply_to:

======================================================

you have (3) failed email deliveries verify your information to deliver your e-mails  brad@malware-traffic-analysis.net  retrieve your mails    please kindly retrieve your email

======================================================''']
execute(email, model)
print('\n')
execute(email, model1)
print('\n')
execute(email, model3)
print('\n')
execute(email, model4)
print('\n')
execute(email, model5)
print('\n')
execute(email, model6)