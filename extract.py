import os

def read_pd_files(directory, output_file):
  """
  Reads all .pd files in a directory and appends their source code to a text file.

  Args:
    directory: The directory containing the .pd files.
    output_file: The name of the text file to write the source code to.
  """
  with open(output_file, "a") as outfile:
    for filename in os.listdir(directory):
      if filename.endswith(".pd"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as pd_file:
          source_code = pd_file.read()
          outfile.write(f"\n\n=== {filename} ===\n\n")
          outfile.write(source_code)

directory_path = "renamed_patches"  


output_filename = "pd_source_code.txt"

read_pd_files(directory_path, output_filename)

print(f"Successfully extracted source code from .pd files in {directory_path} and saved to {output_filename}")
