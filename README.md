# Lubuntu to Remember

A personal collection of useful Linux commands, terminal notes, configuration references, and small utilities for Lubuntu and Ubuntu-based systems.

This repository serves as a practical reference for everyday Linux usage and a place to keep useful commands and scripts in one location.

## Contents

| File | Description |
|---|---|
| `ubuntu_commands_to_remember.txt` | A reference for useful Ubuntu commands and packages. |
| `note.txt` | General notes and information worth keeping. |
| `myvimrcfile.txt` | A reference copy of my Vim configuration. |
| `copyfile` | A Bash utility for copying a file's contents to the system clipboard. |

The collection may grow as I learn more about Linux, Bash scripting, and terminal-based workflows.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/prosperlpx/lubuntu_to_remember.git
```

Enter the project directory:

```bash
cd lubuntu_to_remember
```

You can read the reference files using a terminal pager such as `less`:

```bash
less ubuntu_commands_to_remember.txt
less note.txt
less myvimrcfile.txt
```

Press `q` to exit `less`.

## CopyFile Utility

The `copyfile` script copies the contents of a file to the system clipboard.

### Requirements

- Linux
- Bash
- `xclip`
- A compatible graphical clipboard environment

### Usage

Make the script executable:

```bash
chmod +x copyfile
```

Pass a file path as an argument:

```bash
./copyfile example.txt
```

You can also run the script without an argument:

```bash
./copyfile
```

It will prompt you to enter a file path.

### Installing xclip

If `xclip` is missing, the script can offer to install it.

Automatic installation is configured for systems using APT, DNF, or YUM. Installation requires `sudo` privileges.

Automatic installation through Pacman is not currently configured.

**Note:** `xclip` is primarily intended for X11-based graphical environments. Other desktop environments may require a different clipboard utility or additional configuration.

## Contributing

Suggestions, corrections, and improvements are welcome.

If you find an incorrect command or have a useful Linux tip to add, feel free to open an issue or submit a pull request.

## License

No license has been specified yet. Please check the repository for licensing information before redistributing or reusing its contents.
