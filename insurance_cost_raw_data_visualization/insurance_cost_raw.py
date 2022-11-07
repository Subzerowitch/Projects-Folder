import csv
import matplotlib.pyplot as plt
import numpy as np

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

with open('insurance.csv', newline='') as insurance_obj:
    insurance_reader = csv.DictReader(insurance_obj)
    for row in insurance_reader:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])


# arranging charges list to have only 2 digits after decimal point
def charges_updater(charges):
    updated_charges = []
    for num in range(len(charges)):
        updated_charges.append(round(float(charges[num]),2))
    return updated_charges


updated_charges = charges_updater(charges)


# making a function to create a dictionary from imported data
def make_dictionary(age, sex, bmi, children, smoker, region, updated_charges):
    insurance_dict = dict()
    for i in range(0, len(age)):
        insurance_dict[i+1] = {'Age': age[i],
                               'Sex': sex[i],
                               'BMI': bmi[i],
                               'Children': children[i],
                               'Smoker': smoker[i],
                               'Region': region[i],
                               'Charges': updated_charges[i]}
    return insurance_dict


# dictionary of insurance.csv
insurance_data = make_dictionary(age, sex, bmi, children, smoker, region, updated_charges)
# print(insurance_data)


# counting average insurance cost for every region
def average_insurance_cost(insurance_data):
    new_dict = {'northeast': [], 'northwest': [], 'southeast': [], 'southwest': []}
    for i in insurance_data:
        if insurance_data[i]['Region'] == 'northeast':
            new_dict['northeast'].append(insurance_data[i]['Charges'])
        elif insurance_data[i]['Region'] == 'northwest':
            new_dict['northwest'].append(insurance_data[i]['Charges'])
        elif insurance_data[i]['Region'] == 'southeast':
            new_dict['southeast'].append(insurance_data[i]['Charges'])
        elif insurance_data[i]['Region'] == 'southwest':
            new_dict['southwest'].append(insurance_data[i]['Charges'])
    for region in new_dict:
        total = 0
        for num in new_dict[region]:
            total += num
        new_dict[region] = [round(total / len(new_dict[region]), 2)]
    return new_dict


average_by_region = average_insurance_cost(insurance_data)
print('The average insurance cost in every region: {}.'.format(average_by_region))


# counting a number of people for every region
def count_region(insurance_data):
    people = dict()
    for i in insurance_data:
        if insurance_data[i]['Region'] not in people:
            people[insurance_data[i]['Region']] = 1
        elif insurance_data[i]['Region'] in people:
            people[insurance_data[i]['Region']] += 1
    return people


people_in_region = count_region(insurance_data)
print('Number of residents in region: {}.'.format(people_in_region))


# counting total genders
def count_gender(insurance_data):
    sex_count = dict()
    for i in insurance_data:
        if insurance_data[i]['Sex'] not in sex_count:
            sex_count[insurance_data[i]['Sex']] = 1
        elif insurance_data[i]['Sex'] in sex_count:
            sex_count[insurance_data[i]['Sex']] += 1
    return sex_count


gender_counter = count_gender(insurance_data)
print('Total number of female/male: {}.'.format(gender_counter))


# counting average insurance cost for each gender
def average_by_gender(insurance_data):
    gender_dict = {'female':[],'male':[]}
    for key in insurance_data:
        if insurance_data[key]['Sex'] == 'female':
            gender_dict['female'].append(insurance_data[key]['Charges'])
        elif insurance_data[key]['Sex'] == 'male':
            gender_dict['male'].append(insurance_data[key]['Charges'])
    for gender in gender_dict:
        total = 0
        for num in gender_dict[gender]:
            total += num
        gender_dict[gender] = [round(total / len(gender_dict[gender]), 2)]
    return gender_dict


average_cost_gender = average_by_gender(insurance_data)
print('The average insurance cost for each gender: {}.'.format(average_cost_gender))


# counting average insurance cost for smokers
def average_smokers(insurance_data):
    smoker_dict = {'smoker': [], 'non-smoker': []}
    for key in insurance_data:
        if insurance_data[key]['Smoker'] == 'yes':
            smoker_dict['smoker'].append(insurance_data[key]['Charges'])
        elif insurance_data[key]['Smoker'] == 'no':
            smoker_dict['non-smoker'].append(insurance_data[key]['Charges'])
    for sm in smoker_dict:
        total = 0
        for i in smoker_dict[sm]:
            total += i
        smoker_dict[sm] = [round(total / len(smoker_dict[sm]), 2)]
    return smoker_dict


average_cost_smoker = average_smokers(insurance_data)
print('The average cost for smokers/non-smokers is: {}.'.format(average_cost_smoker))


# counting average ins cost for parents
def parents_average(insurance_data):
    parents_dict = {'kids': [], 'no-kids': []}
    for key in insurance_data:
        if int(insurance_data[key]['Children']) > 0:
            parents_dict['kids'].append(insurance_data[key]['Charges'])
        elif int(insurance_data[key]['Children']) == 0:
            parents_dict['no-kids'].append(insurance_data[key]['Charges'])
    for parent in parents_dict:
        total = 0
        for i in parents_dict[parent]:
            total += i
        parents_dict[parent] = [round(total / len(parents_dict[parent]), 2)]
    return parents_dict


average_parents = parents_average(insurance_data)
print('The average insurance cost for parents is: {}.'.format(average_parents))


# BMI av cost
def bmi_average(insurance_data):
    healthy = 25
    bmi_dict = {'healthy': [], 'overweight': []}
    for key in insurance_data:
        if float(insurance_data[key]['BMI']) <= healthy:
            bmi_dict['healthy'].append(insurance_data[key]['Charges'])
        elif float(insurance_data[key]['BMI']) > healthy:
            bmi_dict['overweight'].append(insurance_data[key]['Charges'])
    for bmi in bmi_dict:
        total = 0
        for i in bmi_dict[bmi]:
            total += i
        bmi_dict[bmi] = [round(total / len(bmi_dict[bmi]), 2)]
    return bmi_dict


average_bmi = bmi_average(insurance_data)
print('The average cost for healthy/overweight BMI rate is: {}.'.format(average_bmi))


def average_cost_age(insurance_data):
    young_adults = 30  # up to 30
    middle_aged = 45  # from 30 to 45
    age_dict = {'young': [], 'middle': [], 'old': []}
    for key in insurance_data:
        if int(insurance_data[key]['Age']) <= young_adults:
            age_dict['young'].append(insurance_data[key]['Charges'])
        elif int(insurance_data[key]['Age']) <= middle_aged:
            age_dict['middle'].append(insurance_data[key]['Charges'])
        elif int(insurance_data[key]['Age']) > middle_aged:
            age_dict['old'].append(insurance_data[key]['Charges'])
    for age in age_dict:
        total = 0
        for i in age_dict[age]:
            total += i
        age_dict[age] = [round(total / len(age_dict[age]), 2)]
    return age_dict


age_average_cost = average_cost_age(insurance_data)
print('The average insurance cost by age is: {}.'.format(age_average_cost))

max_cost = round(max(updated_charges), 1)
min_cost = round(min(updated_charges), 1)
average_cost = round(sum(updated_charges)/len(updated_charges), 1)
print(max_cost, min_cost, average_cost)

# the most significant factors are age, smoking and BMI rate

# Data visualization part
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize=(12, 8))

# set height of bar
A = [9397.55, 12569.58, 13949.94, 10284.29, 32050.23]
B = [17200.43, 13956.75, 12365.98, 13946.48,  8434.27]

# Set position of bar on x axis
bar1 = np.arange(len(A))
bar2 = [x + barWidth for x in bar1]

# The plot
plt.bar(bar1, A, color='r', width=barWidth,
        edgecolor='grey', label='A')
plt.bar(bar2, B, color ='g', width=barWidth,
        edgecolor='grey', label='B')
# Adding x ticks
plt.xticks([r + barWidth / 2 for r in range(len(A))],
        ['Young/Old', 'Female/Male', 'Kids/No kids', 'BMI healthy/overweight', 'Smoker/Non-smoker'])


# Adding y ticks
plt.ylabel('Insurance Cost', fontweight='bold', fontsize=14)
plt.show()

