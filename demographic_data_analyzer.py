import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df["age"].mean()

    # What is the percentage of people who have a Bachelor's degree?
    people_bachelors = (df["education"] == "Bachelors").sum()
    percentage_bachelors = people_bachelors/(len(df["education"]))*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_condition = ((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))
    earning_condition = (df["salary"])  == ">50K"

    lower_education_condition = ((df["education"] != "Bachelors") | (df["education"] != "Masters") | (df["education"] != "Doctorate"))

    # percentage with salary >50K
    higher_education_rich_no_percent = (higher_education_condition & earning_condition).sum()
    higher_education_rich = (higher_education_rich_no_percent/df.shape[0])*100

    lower_education_rich_no_percent = (lower_education_condition & earning_condition).sum()
    lower_education_rich = (lower_education_rich_no_percent/df.shape[0])*100

    rich_people = (df["salary"] == ">50K").sum()
    rich_percentage = rich_people.sum()/df.shape[0]

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = (df["hours-per-week"].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_work_hours
    num_min_workers_rich_no_percent = (num_min_workers & earning_condition).sum()
    num_min_workers_rich = (num_min_workers_rich_no_percent/df.shape[0])*100

    # What country has the highest percentage of people that earn >50K?
    
    each_rich_from_countries = df[df["salary"] == ">50K"].groupby("native-country")
    highest_earning_country = each_rich_from_countries.size().idxmax()

    people_USA = (df["native-country"] == "United-States").sum()
    highest_earning_country_percentage = (each_rich_from_countries.size().max()/people_USA)*100

    # Identify the most popular occupation for those who earn >50K in India.
    rich_IN = (df["salary"] == ">50K").sum()
    occupation = df["occupation"].value_counts().max()
    top_IN_occupation = (rich_IN & occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
