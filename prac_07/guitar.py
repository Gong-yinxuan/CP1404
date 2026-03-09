FILENAME = 'guitars.csv'
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        vintage = "(vintage)" if self.is_vintage() else ""
        return f"{self.name}  ({self.year}){vintage} :  {self.cost}"

    def get_age(self):
        import datetime
        age = datetime.datetime.now().year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year

def main():
    guitars = load_guitars(FILENAME)
    print_guitar(guitars)
    guitars_sorted = sort_guitars_by_age(guitars)
    print_guitar(guitars_sorted)

def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def sort_guitars_by_age(guitars):
    return sorted(guitars)

def print_guitar(guitar):
    for guitar in guitar:
        print(guitar)

if __name__ == '__main__':
   main()








