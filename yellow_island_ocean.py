# import necessary modules 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# create a dataframe to store information about mindful eating 
df = pd.DataFrame({'Food': ['Fruits', 'Vegetables', 'Whole Grains', 'Lean Protein', 'Low Fat Dairy'], 
                   'Serving Size': [2, 2, 1, 3, 2], 
                   'Calories': [90, 35, 215, 175, 130], 
                   'Health Benefits': ['Vitamins, Minerals, Fiber', 'Vitamins, Minerals, Fiber', 
                                      'Fiber, B-Vitamins, Magnesium', 'Protein, Vitamins, Minerals',
                                      'Calcium, Protein, Potassium']})

# create a function to display nutrition facts for a given food
def display_nutrition_facts(food):
    food_row = df[df['Food'] == food]
    print('\nNutrition Facts for {}\n'.format(food))
    print('Serving size: {}'.format(food_row['Serving Size'].values[0]))
    print('Calories: {}'.format(food_row['Calories'].values[0])) 
    print('Health Benefits: {}'.format(food_row['Health Benefits'].values[0]))
    
    return 

# create a function to print out mindful eating tips
def print_mindful_eating_tips():
    print('\nMindful Eating Tips:\n')
    print('1. Pay attention to your body’s hunger cues.')
    print('2. Take a few breaths before eating.')
    print('3. Eat slowly and savor each bite.')
    print('4. Eat in a quiet, distraction-free setting.')
    print('5. Enjoy more meals cooked at home.')
    print('6. Aim to include a variety of nutritious foods.')
   
    return 

# create a function to calculate nutritional value of a given meal
def calculate_nutritional_value(meal):
    meal_items = meal.split(', ')
    calories = 0
    health_benefits = []
   
    for item in meal_items:
        food_row = df[df['Food'] == item]
        calories += food_row['Calories'].values[0]
        health_benefits += food_row['Health Benefits'].values[0].split(', ')

    print('\nNutritional Value of the Meal:\n')
    print('Calories: {}'.format(calories))
    print('Health Benefits: {}'.format(list(set(health_benefits))))

    return

# create a function to graph calories for different foods 
def graph_calories():
    plt.bar(df['Food'], df['Calories'])
    plt.xlabel('Food')
    plt.ylabel('Calories')
    plt.title('Calories per Serving of Food')
   
    return

# create a function to graph health benefits of various foods 
def graph_benefits():
    benefits = df['Health Benefits'].apply(lambda x: x.split(', ')).tolist() 
    benefits_list = [] 
   
    for b in benefits: 
        for i in b: 
            benefits_list.append(i) 
   
    benefits_list = list(set(benefits_list))
    count_benefits = np.zeros(len(benefits_list))
   
    for i in range(len(benefits)):
        for j in range(len(benefits_list)):
            if benefits_list[j] in benefits[i]:
                count_benefits[j] += 1
   
    plt.bar(benefits_list, count_benefits)
    plt.xlabel('Nutrient')
    plt.ylabel('Number of Foods')
    plt.title('Number of Foods Providing a Nutrient')
   
    return

# call functions
display_nutrition_facts('Fruits')
print_mindful_eating_tips()
calculate_nutritional_value('Fruits, Lean Protein, Low Fat Dairy')
graph_calories()
graph_benefits()