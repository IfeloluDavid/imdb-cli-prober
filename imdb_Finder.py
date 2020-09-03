import csv
import sys

while (len(sys.argv) < 3):
	print("Usage: python imdb_Scrutiny NAME STARTYEAR")
	sys.exit()

user_name_choice = str(sys.argv[1])
user_year_choice = str(sys.argv[2])

counts = {}

with open("title.basics.tsv", "r") as imdb_file:
	reader = csv.DictReader(imdb_file, delimiter="\t")

	with open("imdb_Results", "w") as results:
		writer = csv.writer(results)

		writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

		for row in reader:

			if row["titleType"] == "tvSeries" and row["isAdult"] == "0" and row["originalTitle"].lower() == user_name_choice:
				if row["startYear"] != "\\N":
					genres = row["genres"] if row["genres"] != "\\N" else None
					if int(row["startYear"]) >= user_year_choice:

						writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"], genres])
			else:
				writer.writerow("Not Found")
				sys.exit
