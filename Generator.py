import csv
import random

def load_scriptures_from_csv(filename):
    # extrapolate scripture data from a CSV file into a dictionary for rnadom selection
    library = {}
    
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
            
        for row in reader:
            raw_topic = row['Topic'].strip()
            topic_key = raw_topic.lower()
            reference = row['Reference'].strip()
            text = row['Text'].strip()
                
            if topic_key not in library:
                library[topic_key] = []
                
            # Add the scripture to that topic's list
            library[topic_key].append((reference, text))
                
    return library

# get scriptures
scripture_data = load_scriptures_from_csv('scriptures.csv')

# get topic from scripture reference

def get_topic(reference):
    for topic, scriptures in scripture_data.items():
        for ref, _ in scriptures:
            if ref == reference:
                if topic == 'faith':
                    return 'Faith'
                elif topic == 'repentance':
                    return 'Repentance'
                elif topic == 'baptism':
                    return 'Baptism'
                elif topic == 'holy ghost':
                    return 'Holy Ghost'
                elif topic == 'enduring to the end':
                    return 'Enduring to the End'
    return None

# initialize scripture generator
print("Here is a scripture generator for the Doctrine of Christ from Paul's Letters." \
"\nInput a topic from the Doctrine of Christ and receive a scripture from Paul's Letters on that topic" \
"\nType 'random' for a random scripture." \
"\nType 'exit' to quit." \
"\nCreated by Andrew Frandsen" \
"\n")
print("The Doctrine of Christ:", ", ".join([t.title() for t in scripture_data.keys()]))

# continuously prompt user for topics and return random scriptures
while True:
    # get user input
    user_topic = input("\nEnter a topic: ").strip().lower()

    # give an random scripture for that topic
    if user_topic in scripture_data:
        options = scripture_data[user_topic]
    
        selection = random.choice(options)
    
        # separate reference and text
        reference, text = selection
        print(f"\n--- {reference} ---")
        print(f'"{text}"')
    elif user_topic == 'random':
        all_scriptures = [scripture for scriptures in scripture_data.values() for scripture in scriptures]
        selection = random.choice(all_scriptures)

        # state topic
        topic = get_topic(selection[0])
        print(f"\n--- {topic} ---")
        
        # separate reference and text
        
        reference, text = selection
        print(f"\n--- {reference} ---")
        print(f'"{text}"')
    elif user_topic == 'exit':
        print("Exiting the scripture generator. Goodbye!")
        break
    else:
        print(f"\nSorry, no scriptures found for '{user_topic}'.")