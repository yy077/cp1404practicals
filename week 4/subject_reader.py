# subject_reader.py

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student number to integer
            data.append(parts)
    return data

def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

def main():
    filename = "subject_data.txt"
    data = load_data(filename)
    display_subject_details(data)

if __name__ == "__main__":
    main()