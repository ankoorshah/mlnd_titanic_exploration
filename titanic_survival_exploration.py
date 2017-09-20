import pandas as pd

from IPython.display import display
#import visuals as vs

def main():
    in_file='titanic_data.csv'
    full_data = pd.read_csv(in_file)
    display(full_data.head())
    outcomes, data = extract_drop(full_data, 'Survived')
    #vs.survival_stats(data,outcomes,'Parch',["Sex == 'female'", "Pclass == 3", ])
    predictions = prediction_3(data)
    print (accuracy_score(outcomes,predictions))

def accuracy_score(truth, pred):
    if len(truth) == len(pred):
        return 'Predictions have an accuracy of {:.2f}%.'.format((truth == pred).mean()*100)
    else:
        return 'Number of predictions dont match outcomes'


def extract_drop(all_data, index):
    outcomes = all_data[index]
    data = all_data.drop(index, axis=1)
    return outcomes, data

def prediction_0(data):
    predictions = []
    for _,passenger in data.iterrows():
        predictions.append(0)
    return predictions

def prediction_1(data):
    predictions = []
    for _,passenger in data.iterrows():
        if passenger['Sex'].lower() == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
    return predictions

def prediction_2(data):
    predictions = []
    for _,passenger in data.iterrows():
        if passenger['Sex'].lower() == 'female':
            predictions.append(1)
        elif passenger['Sex'].lower() == 'male':
            if passenger['Age'] <= 10:
                predictions.append(1)
            else:
                predictions.append(0)
    return predictions

def prediction_3(data):
    predictions = []
    for _,passenger in data.iterrows():
        if passenger['Sex'].lower() == 'female':
            if passenger['Parch']>1 and passenger["Pclass"]==3:
                predictions.append(0)
            else:
                predictions.append(1)
        elif passenger['Sex'].lower() == 'male':
            if passenger['Age'] <= 10:
                predictions.append(1)
            else:
                predictions.append(0)
    return predictions

if __name__ == '__main__':
    main()
    
