import os
import shutil

print("===== JPG FILE AUTOMATION =====")

# Get folder paths
source_folder = input("Enter source folder path: ").strip()
destination_folder = input("Enter destination folder path: ").strip()

# Check source folder
if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    exit()

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created.")

# Count moved files
moved_count = 0

# Check files in source folder
for filename in os.listdir(source_folder):

    # Check for JPG files
    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(
            source_folder,
            filename
        )

        destination_path = os.path.join(
            destination_folder,
            filename
        )

        # Make sure it is a file
        if os.path.isfile(source_path):

            shutil.move(
                source_path,
                destination_path
            )

            print("Moved:", filename)

            moved_count += 1


print("\nAutomation completed!")
print("Total JPG files moved:", moved_count)