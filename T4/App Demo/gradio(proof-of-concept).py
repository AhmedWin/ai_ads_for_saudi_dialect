import gradio as gr
import random

# Load your dataset file
file_path = 'ad_dialect_data(2).txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        dataset_lines = file.readlines()

except Exception as e:
    print("Error:", e)
    dataset_lines = []

# Function to generate a random ad based on the selected dialect
def generate_random_ad(dialect):
    # Find the corresponding dialect in the dataset
    dialect_prefix = f"{dialect}:"
    dialect_ads = [line.strip() for line in dataset_lines if line.startswith(dialect_prefix)]

    # Choose a random ad from the dataset for the specified dialect
    if dialect_ads:
        selected_ad = random.choice(dialect_ads)
        return f"Selected Dialect: {dialect}\nRandom Ad Text: {selected_ad}"
    else:
        return f"No ads found for the specified dialect: {dialect}"

# Define the dialect options for the drop-down list
dialect_options = ["الحجاز", "نجدي", "مصر"]

iface = gr.Interface(
    fn=generate_random_ad,
    inputs=gr.Dropdown(dialect_options, label="Select Dialect"),
    outputs=gr.Textbox(),
    live=True
)

iface.launch()
