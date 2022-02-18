import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_df = pd.read_csv('train.csv')

titanic_df ['Survived'] = titanic_df ['Survived'].map({
    0: 'Died',
    1: 'Survived'
})



titanic_df = titanic_df.drop(['Ticket', 'Fare', 'Parch', 'PassengerId', 'SibSp'], axis=1)

titanic_df['Pclass'] = titanic_df['Pclass'].map({
    1: 'Lux',
    2: 'Economy',
    3: 'Lower'
})

print(titanic_df.head(10))


print('\t _____data visulizations_____ \t')

x = sns.countplot(x='Pclass', hue='Survived', palette='Set1', data=titanic_df)
x.set(title='passenger class vs survived ratio', xlabel='Pclass', ylabel='total survived')
plt.show()


x = sns.countplot(x='Sex', hue='Survived', palette='Set2', data=titanic_df)
x.set(title='total survivors acc to sex', xlabel='sex', ylabel='total survived')
plt.show()


ax = sns.countplot(x = 'Embarked', hue = 'Survived', palette = 'Set1', data = titanic_df)
ax.set(title = 'survival distribution according to embarking place')
plt.show()

