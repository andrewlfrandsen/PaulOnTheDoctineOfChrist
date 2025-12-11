import streamlit as st
import csv
import random

@st.cache_data
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
st.title("THe Doctrine of Christ Scripture Generator")
st.markdown("Created by Andrew Frandsen")
st.write("\nInput a topic from the Doctrine of Christ and receive a scripture from Paul's Letters on that topic" \
"\nType 'random' for a random scripture." \
"\nType 'exit' to quit.")
st.write("The Doctrine of Christ:", ", ".join([t.title() for t in scripture_data.keys()]))

# continuously prompt user for topics and return random scriptures
mode = st.radio("How would you like to choose?", ["Select a Topic", "Random / Surprise Me"])

selected_topic = None

if mode == "Select a Topic":
    # Create a list of nice-looking topic names
    # We capitalize them for the dropdown, but we will use lowercase for the lookup
    topic_options = [t.title() for t in scripture_data.keys()]
    user_selection = st.selectbox("Choose a Doctrine:", topic_options)
        
    # Convert back to lowercase key for the dictionary
    selected_topic = user_selection.lower()

# 5. ACTION BUTTON
if st.button("Get Scripture"):
        
    result_reference = ""
    result_text = ""
    display_topic = ""

    # LOGIC A: Specific Topic
    if mode == "Select a Topic" and selected_topic:
        if selected_topic in scripture_data:
            options = scripture_data[selected_topic]
            selection = random.choice(options)
            result_reference, result_text = selection
            display_topic = selected_topic.title()
        
    # LOGIC B: Random Mode
    elif mode == "Random / Surprise Me":
        # Flatten all lists into one big list of scriptures
        all_scriptures = [s for sublist in scripture_data.values() for s in sublist]
        selection = random.choice(all_scriptures)
            
        result_reference, result_text = selection
        # Find the topic for this random scripture
        display_topic = get_topic(result_reference)

    # 6. DISPLAY RESULTS
    if result_reference:
        st.markdown("---")
        st.subheader(f"{display_topic}") 
        st.markdown(f"### {result_reference}")
        st.info(f'"{result_text}"')
"""
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
"""