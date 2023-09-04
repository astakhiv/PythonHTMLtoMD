import markdownify
import os
import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid usage")
    
    file_name = sys.argv[1]

    try:
        url = input("Url: ")
        content = requests.get(url).text
    except requests.RequestException:
        sys.exit("Wrong url")

    md_content = markdownify.markdownify(content)

    f = open(os.path.join(os.getcwd(), f"{file_name}.md"), "w")
    f.write(md_content)
    f.close()

    print("Succesfuly Done")

if __name__ == "__main__":
    main()