
# Curl Extractor

Curl Extractor is a powerful Python script that extracts and lists URLs from files containing curl commands. The URLs are grouped by domain for easy analysis and review. Additionally, users can exclude specific file extensions and retrieve full curl requests for specific global identifiers.

## Features

- Extract URLs from files containing curl commands
- Group URLs by domain
- Exclude URLs with specific file extensions
- Retrieve the full curl request for a specific global identifier

## Usage

Curl Extractor is easy to use and offers flexible options for different needs. Here are the basic usage instructions and examples.

### Basic Usage

```sh
python3 curl_extractor.py myfile.txt
```

### Exclude Specific File Extensions

```sh
python3 curl_extractor.py myfile.txt --exclude-ext js css png
```

### Retrieve Full Curl Request for Specific Identifier

```sh
python3 curl_extractor.py myfile.txt --id 5
```

## Installation

1. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

2. Clone the Curl Extractor repository:

```sh
git clone https://github.com/dacharron/curl_extractor.git
```

3. Navigate to the `curl_extractor` directory:

```sh
cd curl_extractor
```

4. Make the script executable:

```sh
chmod +x curl_extractor.py
```

5. Move the script to `/usr/bin/curl_extractor`:

```sh
sudo mv curl_extractor.py /usr/bin/curl_extractor
```

6. Create a shortcut for the binary called `ce`. Add the following alias to your `.bashrc`, `.zshrc`, or appropriate profile file depending on the shell you use:

```sh
echo "alias ce='/usr/bin/curl_extractor'" >> ~/.bashrc
```

For Zsh users, replace `.bashrc` with `.zshrc`. If you use a different shell, add the alias to the appropriate configuration file.

7. Apply the changes:

```sh
source ~/.bashrc
```

Or for Zsh users:

```sh
source ~/.zshrc
```

8. Now, you can use `Curl Extractor` either with the full path:

```sh
/usr/bin/curl_extractor myfile.txt
```

Or using the `ce` shortcut:

```sh
ce myfile.txt
```

9. Enjoy extracting and organizing URLs with ease!

### Note:

Ensure the script is well tested before moving it to `/usr/bin/`, as it will be globally accessible from any directory and should be free of critical bugs or issues.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to discuss any additional features or improvements.

## License

Curl Extractor is open-source software, licensed under [MIT](LICENSE).