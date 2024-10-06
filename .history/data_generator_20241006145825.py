import base64
import os
import json

# Function to encode image as base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to the folder containing Mohanlal's images
image_folder = "Mohanlal"

# Output file where the JSONL data will be saved
output_file = "data.jsonl"

# Prepare the messages structure for each image and write to data.jsonl
with open(output_file, 'w') as outfile:
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)

        # Ensure it's an image file
        if image_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Convert the image to base64
            base64_image = encode_image(image_path)

            # Construct the JSON structure
            data = {
                "messages": [
                    {"role": "system", "content": "You are a bot who is good at recognizing people from their images"},
                    {"role": "user", "content": "Who is this person?"},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    },
                    {"role": "assistant", "content": "Mohanlal"}
                ]
            }

            # Write to JSONL file
            json.dump(data, outfile)
            outfile.write('\n')

print(f"Data saved to {output_file}")
