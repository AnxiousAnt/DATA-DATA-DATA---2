import os

def rename_pd_files(input_dir, output_dir):
  """
  Creates new files with sequential names for .pd files in the input directory
  and stores them in the output directory. Originals remain untouched.

  Args:
    input_dir: Path to the directory containing .pd files.
    output_dir: Path to the directory where renamed files will be created.
  """
  # Get a list of files in the input directory
  files = os.listdir(input_dir)

  # Keep track of used numbers based on existing files in the output directory
  used_numbers = set()
  for filename in os.listdir(output_dir):
    if filename.endswith(".pd"):
      # Extract the number from existing file names (assuming proper numbering)
      try:
        file_num = int(filename.split(".")[0])
        used_numbers.add(file_num)
      except ValueError:
        pass  # Ignore non-numeric filenames

  # Generate a unique sequential number for each file
  start_num = 0
  for i, filename in enumerate(files):
    if filename.endswith(".pd"):
      # Find the first unused number in the sequence
      while start_num + i in used_numbers:
        start_num += 1

      # Create new filename with the unique sequential number
      new_filename = f"{start_num + i}.pd"

      # Construct full paths
      input_path = os.path.join(input_dir, filename)
      output_path = os.path.join(output_dir, new_filename)

      # Open the original file in read binary mode
      with open(input_path, "rb") as input_file:
        # Read the file contents
        data = input_file.read()

      # Open the new file in write binary mode
      with open(output_path, "wb") as output_file:
        # Write the data to the new file
        output_file.write(data)
      print(f"Created new file: {new_filename} (Output Directory)")

input_dir = "patches"
output_dir = "renamed_patches"

rename_pd_files(input_dir, output_dir)
