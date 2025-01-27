import csv
from faker import Faker

def generate_csv(file_name, num_records):
    fake = Faker()
    Faker.seed(0)

    columns = [
        "code",
        "name",
        "creation_date"
    ]

    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)

        for i in range(1, num_records + 1):
            record = [
                i,  # code
                fake.unique.job(),  # name
                fake.date_between(start_date="-15y", end_date="today")  # creation_date
            ]
            writer.writerow(record)

    print(f"CSV file generated: {file_name}")

if __name__ == "__main__":
    num_records = 100  # data quantity
    file_name = "careers.csv"
    generate_csv(file_name, num_records)