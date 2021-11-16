from names_dataset import NameDatasetV1 # https://github.com/philipperemy/name-dataset # pip install names-dataset
import random

random.seed("602888")

m = NameDatasetV1()
first_names = list(m.first_names)
first_names.sort()
random.shuffle(first_names)

#returns a list of first name and last name
def split_full_name(fullname):
    split_name = fullname.split(" ")

# make a fake email from the fullname and a domain address
def make_email(fullname, domain_name):
    email = fullname + "@" + domain_name
    return email

# make a fake name from the first and last names
def next_full_name(first_name, last_name):
    full = next_first_name(first_name)
    full = full + " " + next_last_name(last_name)
    return full

# input a name and get the next name in the dataset
def next_first_name(first_name):
    first = ""
    return first

# input a name and get the next name in the dataset
def next_last_name(last_name):
    last = ""
    return last

if __name__ == "__main__":
    fn = first_names.copy()
    i = fn.index("peter")
    next = fn.pop(i+1)
    print(next)
    next = first_names.pop(i+1)
    print(next)
    print(make_email(next, "fake.kit.jp"))