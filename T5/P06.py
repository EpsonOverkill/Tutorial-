import csv
file = open("data.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["SN", "Name", "Country", "Work", "Year"])
writer.writerow([1, "Linus", "Finland", "Linux", 1991])
writer.writerow([2, "Tim", "England", "WWW", 1990])
writer.writerow([3, "Guido", "Netherlands", "Python", 1991])
file.close()
