import csv
import random
from faker import Faker

def generate_csv(file_name, num_records):
    fake = Faker()
    Faker.seed(0)

    columns = [
        "code",
        "last_name",
        "first_name",
        "age",
        "gender",
        "weight",
        "height",
        "color",
        "province",
        "career_code",
        "entry_date"
    ]

    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)

        for _ in range(num_records):
            record = [
                fake.unique.random_int(min=10000000, max=25999999),  # code
                fake.last_name(),  # last_name
                fake.first_name(),  # first_name
                random.randint(18, 35),  # age
                random.choice(["M", "F"]),  # gender
                round(random.uniform(45, 100), 2),  #  weight (kg)
                round(random.uniform(1.4, 2.0), 2),  # height (m)
                fake.color_name(),  # color
                fake.state(), #province
                random.randint(1, 100),  # career_code
                fake.date_between(start_date="-15y", end_date="today")  # entry_date
            ]
            writer.writerow(record)

    print(f"CSV file generated: {file_name}")

if __name__ == "__main__":
    num_records = 100000 # data quantity
    file_name = "students.csv"
    generate_csv(file_name, num_records)
