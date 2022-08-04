<!-- PROJECT INTRO -->

OrpheusDL - Genius
==================

A Genius module for the OrpheusDL modular archival music program

[Report Bug](https://github.com/Dniel97/orpheusdl-genius/issues)
·
[Request Feature](https://github.com/Dniel97/orpheusdl-genius/issues)


## Table of content

- [About OrpheusDL - Genius](#about-orpheusdl---genius)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
    - [Global](#global)
- [Contact](#contact)


<!-- ABOUT ORPHEUS -->
## About OrpheusDL - Genius

OrpheusDL - Genius is a module written in Python which allows retrieving lyrics from **[Genius](https://genius.com)** for the modular music archival program.


<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get a local copy of Orpheus up and running:

### Prerequisites

* Already have [OrpheusDL](https://github.com/yarrm80s/orpheusdl) installed

### Installation

1. Go to your `orpheusdl/` directory and run the following command:
   ```sh
   git clone https://github.com/Dniel97/orpheusdl-genius.git modules/genius
   ```
2. Execute:
   ```sh
   python orpheus.py
   ```

<!-- USAGE EXAMPLES -->
## Usage

Either set genius as your default lyrics provider in module_defaults, or call orpheus.py with the following option:

```sh
python orpheus.py -lr genius https://open.qobuz.com/album/c9wsrrjh49ftb
```

<!-- CONFIGURATION -->
## Configuration

You can customize every module from Orpheus individually and also set general/global settings which are active in every
loaded module. You'll find the configuration file here: `config/settings.json`

### Global

```json5
"global": {
    "module_defaults": {
        "lyrics": "genius",
        // ...
    },
    "lyrics": {
        "embed_lyrics": true,
        // ...
    },
}
```

| Option             | Info                                                                                                                                              |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| module_defaults    | Lets you select which module to automatically get lyrics/covers/credits from. If selecting default, it will use the main module for the same task |
| embed_lyrics       | Embeds the (unsynced) as a tag inside the FLAC, M4A, MP3, ... file                                                                                |

<!-- Contact -->
## Contact

Yarrm80s - [@yarrm80s](https://github.com/yarrm80s)

Dniel97 - [@Dniel97](https://github.com/Dniel97)

Project Link: [OrpheusDL Genius Public GitHub Repository](https://github.com/Dniel97/orpheusdl-genius)
