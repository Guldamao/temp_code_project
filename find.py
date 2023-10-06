import argparse
import subprocess

def search_file_and_save_output(path, file_name, output_file):
               # define the 'find' command
    find_command = ["find", path, "-iname", file_name]

    try:
        # Execute the 'find' command and save the output to the specified file
        with open(output_file, 'w') as f:
            subprocess.run(find_command, stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        print(f"Search results saved to '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a file in the Linux file system and save results to a text file.")
    parser.add_argument("-p", "--path", default="/", help="The directory to start the search (default: /).")
    parser.add_argument("-n", "--file-name", required=True, help="The name of the file to search for.")
    parser.add_argument("-o", "--output-file", default="search_results.txt", help="Name of the output file (default: search_results.txt).")

    args = parser.parse_args()

    search_file_and_save_output(args.path, args.file_name, args.output_file)

