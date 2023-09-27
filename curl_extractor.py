import re
import argparse
import textwrap
from urllib.parse import urlparse

def extract_urls_grouped_by_domain(filename, exclude_extensions=[]):
    """Extract URLs from the given file and group them by domain name."""
    with open(filename, 'r') as f:
        content = f.read()

    pattern = re.compile(r'curl\s+\'(https?://[^\'\s]+)\'')
    urls = pattern.findall(content)

    domain_paths = {}
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path
        
        # Exclude URL if its extension matches the ones provided
        if any(path.endswith(ext) for ext in exclude_extensions):
            continue
        
        if domain not in domain_paths:
            domain_paths[domain] = set()
        domain_paths[domain].add(path)

    return domain_paths

def find_full_request_for_identifier(filename, idx, all_paths):
    """Find and return the full request for a given global identifier."""
    uri_to_find = all_paths[int(idx) - 1]  # Convert from 1-based index to 0-based
    
    with open(filename, 'r') as f:
        content = f.readlines()

    in_curl_command = False
    full_curl_command = []

    for line in content:
        line_stripped = line.strip()
        if line_stripped.startswith("curl '"):
            if in_curl_command:
                full_curl_command = []
            in_curl_command = True

        if in_curl_command:
            full_curl_command.append(line_stripped)

            if line_stripped.endswith(";"):
                if uri_to_find in "".join(full_curl_command):
                    return "\n".join(full_curl_command)
                full_curl_command = []
                in_curl_command = False

    return None

def decorative_separator(domain):
    """Generate a decorative separator based on the domain name."""
    sep = "=" * (len(domain) + 6)
    return f"== {domain} =="


def handle_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""
        Extract and list URLs from a file containing curl commands, grouped by domain. 
        URLs can be excluded based on their file extensions. 
        Also allows retrieval of the full curl request for a specific global identifier.
        """),
        epilog=textwrap.dedent("""
        Examples:
        1. Extract and list all URLs from a file:
           %(prog)s myfile.txt
           
        2. Exclude URLs with specific extensions:
           %(prog)s myfile.txt --exclude-ext js css png
           
        3. Retrieve the full curl request for a specific global identifier:
           %(prog)s myfile.txt --id 5
           
        Note: Global identifiers are indexed in the order the URLs appear in the input file.
        """),
        formatter_class=argparse.RawDescriptionHelpFormatter  # Maintains formatting in description and epilog
    )

    parser.add_argument("filename", help="The file containing curl commands to process.")
    parser.add_argument("--id", type=int, 
                        help="The global identifier of a URL to retrieve the full curl request.")
    parser.add_argument("--exclude-ext", nargs='*', default=[], metavar="EXT",
                        help="File extensions of URLs to exclude. e.g., --exclude-ext js css png")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = handle_args()

    exclude_extensions = ['.' + ext for ext in args.exclude_ext]
    domain_paths = extract_urls_grouped_by_domain(args.filename, exclude_extensions)
    
    all_paths = []
    for paths in domain_paths.values():
        all_paths.extend(sorted(paths))
    
    if args.id:
        full_request = find_full_request_for_identifier(args.filename, args.id, all_paths)
        if full_request:
            print(full_request)
        else:
            print(f"Identifier {args.id} not found in {args.filename}.")
    else:
        global_idx = 1
        for domain, paths in domain_paths.items():
            print(decorative_separator(domain))
            for path in sorted(paths):
                print(f"{global_idx}: {path}")
                global_idx += 1
            print()
